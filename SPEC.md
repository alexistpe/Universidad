# SPEC VideoGen - Generador Automático de Videos

## 1. Overview del Proyecto

| Atributo | Descripción |
|----------|-------------|
| **Nombre** | VideoGen |
| **Tipo** | CLI Tool para generación automática de videos |
| **Funcionalidad** | Genera videos horizontales 1920x1080 a partir de un prompt textual usando LLM local, descarga medios de Pixabay y genera voiceover con Coqui TTS |
| **Target** | usuarios que quieren crear videos explicativos rápidos sin costo de cloud |

---

## 2. Requisitos del Sistema

### Hardware Mínimo
- CPU: 4 núcleos
- RAM: 8GB (12GB recomendado si hay GPU)
- Almacenamiento: 10GB libres
- OS: Linux/macOS/Windows (WSL)

### Software Requerido
- Python 3.9 - 3.11 (NO usar 3.12, incompatible con Coqui TTS)
- FFmpeg (sistema)
- Ollama (para LLM local)

---

## 3. Instalación Completa

### 3.1 Preparación del Sistema

```bash
# Crear directorio del proyecto
mkdir -p ~/Files/Proyectos
cd ~/Files/Proyectos

# Instalar FFmpeg
# Linux (Debian/Ubuntu)
sudo apt update && sudo apt install -y ffmpeg

# macOS
brew install ffmpeg

# Windows (WSL o descargar de https://ffmpeg.org)
```

### 3.2 Entorno Virtual

```bash
# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Actualizar pip
pip install --upgrade pip
```

### 3.3 Dependencias Python

```bash
# Core principal (INSTALAR PRIMERO)
pip install moviepy requests pillow python-dotenv tqdm

# IMPORTANTE: Coqui TTS requiere torch CPU primero
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install torchaudio

# Coqui TTS (después de torch)
pip install coqui-tts
```

### 3.4 Ollama

```bash
# Instalar Ollama (https://ollama.ai)
curl -fsSL https://ollama.ai/install.sh | sh

# Iniciar servicio
ollama serve

# Descargar modelo recomendado
ollama pull llama3
# Modelos alternativos: gemma:2b, phi3
```

### 3.5 API Key de Pixabay

1. Ir a https://pixabay.com/api/
2. Registrarse (gratis)
3. Copiar API key

---

## 4. Estructura de Archivos

```
~/Files/Proyectos/
├── main.py                 # Entry point original
├── vid                    # CLI command global
├── setup.sh               # Script de instalación
├── requirements.txt     # Dependencias Python
├── .env.example         # Template de configuración
├── README.md            # Documentación
│
├── src/
│   ├── __init__.py
│   ├── config.py        # Configuraciones globales
│   ├── coordinator.py  # Orquestador principal
│   │
│   ├── llm/
│   │   └── ollama_client.py
│   │
│   ├── media/
│   │   └── pixabay_client.py
│   │
│   ├── audio/
│   │   └── tts_engine.py
│   │
│   └── video/
│       └── renderer.py
│
├── assets/
│   ├── voices/        # Voces pre-definidas (opcional)
│   └── fonts/         # Fuentes para texto (opcional)
│
├── output/            # Videos generados
├── logs/             # Logs de ejecución
└── .cache/           # Cache de medios
```

---

## 5. Código Completo

### 5.1 requirements.txt

```
moviepy>=2.0.0
requests>=2.31.0
pillow>=10.0.0
python-dotenv>=1.0.0
tqdm>=4.66.0
torch>=2.0.0
torchaudio>=2.0.0
coqui-tts>=0.22.0
```

### 5.2 src/config.py

```python
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class VideoConfig:
    width: int = 1920
    height: int = 1080
    fps: int = 30
    codec: str = "libx264"
    audio_codec: str = "aac"
    bitrate: str = "5000k"


@dataclass
class LLMConfig:
    base_url: str = "http://localhost:11434"
    model: str = "llama3"
    temperature: float = 0.7
    timeout: int = 180


@dataclass
class PixabayConfig:
    api_key: Optional[str] = None
    base_url: str = "https://pixabay.com/api"
    per_page: int = 10


@dataclass
class TTSConfig:
    model_name: str = "tts_models/multilingual/multi-dataset/xtts_v2"
    language: str = "es"
    voice: str = "female"
    sample_rate: int = 24000
    device: str = "auto"


@dataclass
class PathsConfig:
    base_dir: Path = Path(__file__).parent.parent
    assets_dir: Path = base_dir / "assets"
    voices_dir: Path = assets_dir / "voices"
    fonts_dir: Path = assets_dir / "fonts"
    output_dir: Path = base_dir / "output"
    logs_dir: Path = base_dir / "logs"
    cache_dir: Path = base_dir / ".cache"
    temp_dir: Path = base_dir / ".tmp"


@dataclass
class Config:
    video: VideoConfig = VideoConfig()
    llm: LLMConfig = LLMConfig()
    pixabay: PixabayConfig = PixabayConfig()
    tts: TTSConfig = TTSConfig()
    paths: PathsConfig = PathsConfig()
    verbose: bool = False
    max_duration_minutes: int = 10


def get_config() -> Config:
    config = Config()
    
    config.pixabay.api_key = os.getenv("PIXABAY_API_KEY")
    config.llm.base_url = os.getenv("OLLAMA_URL", config.llm.base_url)
    config.llm.model = os.getenv("OLLAMA_MODEL", config.llm.model)
    config.verbose = os.getenv("VIDEOGEN_VERBOSE", "").lower() == "true"
    
    for directory in [config.paths.output_dir, config.paths.logs_dir, 
                       config.paths.cache_dir, config.paths.temp_dir]:
        directory.mkdir(parents=True, exist_ok=True)
    
    return config


CONFIG = get_config()
```

### 5.3 src/llm/ollama_client.py

```python
import json
import requests
from typing import Optional
from dataclasses import dataclass


SYSTEM_PROMPT = """Eres un escritor de guiones profesionales para videos explicativos.
Tu tarea es generar un guion estructurado para un video basado en el tema proporcionado.

Requisitos del guion:
- Resolución del video: 1920x1080 horizontal
- Duración máxima: {max_duration} minutos
- Idioma: español
- Cada segmento debe durar entre 15-45 segundos

Formato de salida STRICTAMENTE como JSON (sin texto adicional):
{{
  "title": "Título del video",
  "description": "Breve descripción del contenido",
  "duration": "Duración total estimada (MM:SS)",
  "segments": [
    {{
      "id": 1,
      "start": "MM:SS",
      "end": "MM:SS",
      "script": "Texto para voiceover de este segmento",
      "media_query": "Búsqueda para video (en inglés, 2-4 palabras)",
      "mood": "Tono emocional (informativo/motivacional/curioso/serio/dinámico)"
    }}
  ]
}}

IMPORTANTE: Solo devuelve JSON válido, sin markdown ni texto explicativo"""


@dataclass
class ScriptSegment:
    id: int
    start: str
    end: str
    script: str
    media_query: str
    mood: str


@dataclass
class VideoScript:
    title: str
    description: str
    duration: str
    segments: list


class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", 
                 model: str = "llama3", timeout: int = 180):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout
        self.verbose = False
    
    def generate_script(self, prompt: str, max_duration: int = 10, 
                       verbose: bool = False) -> VideoScript:
        self.verbose = verbose
        if verbose:
            print(f"[LLM] Generando guion con: {self.model}")
        
        full_prompt = f"{SYSTEM_PROMPT.format(max_duration=max_duration)}\n\nTema: {prompt}\n\nJSON:"
        
        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "format": "json",
            "stream": False,
        }
        
        raw_response = ""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            raw_response = data.get("response", "")
            
            return self._parse_response(raw_response)
            
        except requests.exceptions.Timeout:
            raise TimeoutError(f"LLM timeout después de {self.timeout}s")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"No se puede conectar a Ollama en {self.base_url}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Respuesta inválida del LLM: {e}")
    
    def _parse_response(self, raw: str) -> VideoScript:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            start_idx = raw.find('{')
            end_idx = raw.rfind('}') + 1
            if start_idx >= 0 and end_idx > start_idx:
                data = json.loads(raw[start_idx:end_idx])
            else:
                raise ValueError(f"No se pudo parsear JSON")
        
        segments = [
            ScriptSegment(
                id=s["id"],
                start=s["start"],
                end=s["end"],
                script=s["script"],
                media_query=s.get("media_query", ""),
                mood=s.get("mood", "informativo")
            )
            for s in data.get("segments", [])
        ]
        
        return VideoScript(
            title=data.get("title", "Untitled"),
            description=data.get("description", ""),
            duration=data.get("duration", "00:00"),
            segments=segments
        )
    
    def is_available(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except Exception:
            return False
    
    def list_models(self) -> list[str]:
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return [m["name"] for m in data.get("models", [])]
        except Exception:
            return []
        return []
```

### 5.4 src/media/pixabay_client.py

```python
import os
import hashlib
import requests
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from tqdm import tqdm


@dataclass
class MediaResult:
    id: int
    type: str
    title: str
    url: str
    thumbnail: str
    width: int
    height: int
    duration: Optional[int] = None


class PixabayClient:
    def __init__(self, api_key: Optional[str] = None,
                 base_url: str = "https://pixabay.com/api",
                 per_page: int = 10,
                 cache_dir: Optional[Path] = None):
        self.api_key = api_key or os.getenv("PIXABAY_API_KEY")
        if not self.api_key:
            raise ValueError("Se requiere API key de Pixabay")
        
        self.base_url = base_url
        self.per_page = min(per_page, 20)
        self.cache_dir = cache_dir or Path.home() / ".cache" / "videogen"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "videogen/1.0"})
    
    def _make_cache_key(self, query: str, image_type: str = "all") -> str:
        key = f"{query}_{image_type}"
        return hashlib.md5(key.encode()).hexdigest()[:12]
    
    def _download_file(self, url: str, dest: Path, desc: str = "Descargando") -> bool:
        try:
            response = self.session.get(url, stream=True, timeout=60)
            response.raise_for_status()
            total_size = int(response.headers.get("content-length", 0))
            
            with open(dest, "wb") as f, tqdm(desc=desc, total=total_size, 
                                             unit="B", unit_scale=True) as pbar:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
            return True
        except Exception as e:
            print(f"[ERROR] {e}")
            if dest.exists():
                dest.unlink()
            return False
    
    def search_images(self, query: str, min_width: int = 1280,
                     orientation: str = "horizontal") -> list[MediaResult]:
        params = {
            "key": self.api_key,
            "q": query,
            "image_type": "photo",
            "orientation": orientation,
            "min_width": min_width,
            "per_page": self.per_page
        }
        
        try:
            response = self.session.get(f"{self.base_url}/", params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for hit in data.get("hits", []):
                results.append(MediaResult(
                    id=hit["id"],
                    type="image",
                    title=hit.get("tags", ""),
                    url=hit.get("largeImageURL", hit.get("webformatURL", "")),
                    thumbnail=hit.get("previewURL", ""),
                    width=hit.get("imageWidth", 0),
                    height=hit.get("imageHeight", 0)
                ))
            return results
        except Exception as e:
            print(f"[ERROR] {e}")
            return []
    
    def search_videos(self, query: str) -> list[MediaResult]:
        params = {"key": self.api_key, "q": query, "per_page": self.per_page}
        
        try:
            response = self.session.get(f"{self.base_url}/videos/", params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for hit in data.get("hits", []):
                videos = hit.get("videos", {})
                url = videos.get("fullHD", {}).get("url", "") or \
                     videos.get("hd", {}).get("url", "")
                if url:
                    results.append(MediaResult(
                        id=hit["id"],
                        type="video",
                        title=hit.get("tags", ""),
                        url=url,
                        thumbnail=hit.get("picture_id", ""),
                        width=hit.get("width", 1920),
                        height=hit.get("height", 1080)
                    ))
            return results
        except Exception as e:
            print(f"[ERROR] {e}")
            return []
    
    def search_media(self, query: str, prefer_video: bool = False) -> list[MediaResult]:
        if prefer_video:
            results = self.search_videos(query)
            if not results:
                results = self.search_images(query)
        else:
            results = self.search_images(query)
            if not results:
                results = self.search_videos(query)
        return results
    
    def download_best_match(self, query: str, output_dir: Optional[Path] = None,
                          prefer_video: bool = False) -> Optional[Path]:
        results = self.search_media(query, prefer_video=prefer_video)
        
        if not results:
            alt_queries = query.replace(" ", ",").split(",")[:3]
            for alt in alt_queries:
                results = self.search_media(alt, prefer_video=prefer_video)
                if results:
                    break
        
        if results:
            output_dir = output_dir or self.cache_dir
            output_dir.mkdir(parents=True, exist_ok=True)
            
            result = results[0]
            ext = ".mp4" if result.type == "video" else ".jpg"
            dest = output_dir / f"{result.id}{ext}"
            
            if self._download_file(result.url, dest, desc=f"Descargando {result.type}"):
                return dest
        return None
    
    def is_available(self) -> bool:
        try:
            response = self.session.get(
                f"{self.base_url}/", 
                params={"key": self.api_key, "q": "test", "per_page": 1},
                timeout=10
            )
            return response.status_code in (200, 400)
        except Exception:
            return False
```

### 5.5 src/audio/tts_engine.py

```python
import os
import torch
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


VOICES = {
    "female": {"en": "samples/en/female.wav", "es": "samples/es/female.wav"},
    "male": {"en": "samples/en/male.wav", "es": "samples/es/male.wav"},
    "narrator": {"en": "samples/en/narrator.wav", "es": "samples/es/narrator.wav"}
}


@dataclass
class TTSResult:
    audio_path: Path
    duration: float
    text: str


class CoquiTTSEngine:
    def __init__(self, model_name: str = "tts_models/multilingual/multi-dataset/xtts_v2",
                 voices_dir: Optional[Path] = None, language: str = "es",
                 device: str = "auto", sample_rate: int = 24000):
        self.model_name = model_name
        self.voices_dir = voices_dir or Path(__file__).parent.parent.parent / "assets" / "voices"
        self.language = language
        self.sample_rate = sample_rate
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = None
        self._loaded = False
    
    def load(self, verbose: bool = False) -> bool:
        if self._loaded:
            return True
        try:
            from TTS.api import TTS
            if verbose:
                print(f"[TTS] Cargando modelo: {self.model_name}")
            self.tts = TTS(self.model_name).to(self.device)
            self._loaded = True
            if verbose:
                print("[TTS] Modelo cargado")
            return True
        except Exception as e:
            print(f"[ERROR] {e}")
            return False
    
    def synthesize(self, text: str, output_path: Path, voice: str = "female",
                speed: float = 1.0, verbose: bool = False) -> Optional[TTSResult]:
        if not self._loaded:
            self.load(verbose=verbose)
        if not self.tts:
            return None
        
        voice_path = self._get_voice_path(voice)
        
        try:
            self.tts.tts_to_file(
                text=text,
                speaker_wav=str(voice_path) if voice_path and voice_path.exists() else None,
                language=self.language,
                file_path=str(output_path),
                speed=speed
            )
            duration = self._get_audio_duration(output_path)
            return TTSResult(audio_path=output_path, duration=duration, text=text)
        except Exception as e:
            print(f"[ERROR] {e}")
            return None
    
    def synthesize_segments(self, segments: list, output_dir: Path,
                        voice: str = "female", speed: float = 1.0,
                        verbose: bool = False) -> list[TTSResult]:
        results = []
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for i, segment in enumerate(segments):
            text = segment.script if hasattr(segment, 'script') else segment.get('script', '')
            if not text:
                continue
            output_path = output_dir / f"segment_{i:03d}.wav"
            result = self.synthesize(text, output_path, voice, speed, verbose)
            if result:
                results.append(result)
        return results
    
    def _get_voice_path(self, voice_type: str) -> Optional[Path]:
        voice_map = VOICES.get(voice_type, VOICES["female"])
        voice_file = voice_map.get(self.language, voice_map.get("default"))
        if voice_file:
            voice_path = self.voices_dir / voice_file
            if voice_path.exists():
                return voice_path
        for root, dirs, files in os.walk(self.voices_dir):
            for file in files:
                if file.endswith('.wav'):
                    return Path(root) / file
        return None
    
    def _get_audio_duration(self, audio_path: Path) -> float:
        try:
            import torchaudio
            if audio_path.exists():
                info = torchaudio.info(str(audio_path))
                return info.num_frames / info.sample_rate
        except Exception:
            pass
        return 0.0
    
    def is_available(self) -> bool:
        try:
            from TTS.api import TTS
            return True
        except ImportError:
            return False
```

### 5.6 src/video/renderer.py

```python
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class SegmentData:
    id: int
    start: str
    end: str
    script: str
    media_query: str
    mood: str
    media_path: Optional[Path] = None
    audio_path: Optional[Path] = None


@dataclass
class RenderConfig:
    width: int = 1920
    height: int = 1080
    fps: int = 30
    codec: str = "libx264"
    audio_codec: str = "aac"
    bitrate: str = "5000k"


class VideoRenderer:
    def __init__(self, config: Optional[RenderConfig] = None,
                temp_dir: Optional[Path] = None):
        self.config = config or RenderConfig()
        self.temp_dir = temp_dir or Path("/tmp/videogen")
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            from moviepy import *
            from moviepy.editor import *
            self.moviepy_available = True
        except ImportError:
            self.moviepy_available = False
            print("[WARNING] MoviePy no disponible")
    
    def render_segment(self, segment: SegmentData, output_path: Path,
                    verbose: bool = False) -> bool:
        if not self.moviepy_available:
            return False
        
        try:
            from moviepy.editor import ColorClip, AudioFileClip
            
            duration = self._parse_timestamp(segment.end) - self._parse_timestamp(segment.start)
            
            if segment.media_path and segment.media_path.exists():
                if segment.media_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                    from moviepy.editor import ImageClip
                    clip = ImageClip(str(segment.media_path), duration=duration)
                    clip = clip.resize(height=self.config.height)
                elif segment.media_path.suffix.lower() in ['.mp4', '.avi', '.mov']:
                    from moviepy.editor import VideoFileClip
                    clip = VideoFileClip(str(segment.media_path), audio=False)
                    if clip.duration > duration:
                        clip = clip.subclip(0, duration)
                    clip = clip.resize(height=self.config.height)
            else:
                clip = ColorClip(size=(self.config.width, self.config.height),
                              color=(0, 0, 0), duration=duration)
            
            if segment.audio_path and segment.audio_path.exists():
                audio = AudioFileClip(str(segment.audio_path))
                if audio.duration > duration:
                    audio = audio.subclip(0, duration)
                clip = clip.with_audio(audio)
            
            clip.write_videofile(str(output_path), fps=self.config.fps, codec=self.config.codec,
                          audio_codec=self.config.audio_codec, bitrate=self.config.bitrate,
                          logger=None)
            return True
        except Exception as e:
            print(f"[ERROR] {e}")
            return False
    
    def render_video(self, segments: list[SegmentData], output_path: Path,
                  title: Optional[str] = None, verbose: bool = False) -> bool:
        if not self.moviepy_available:
            return False
        
        try:
            from moviepy.editor import VideoFileClip, concatenate_videoclips
            
            segment_files = []
            for i, segment in enumerate(segments):
                segment_file = self.temp_dir / f"segment_{i:03d}.mp4"
                if self.render_segment(segment, segment_file, verbose):
                    segment_files.append(segment_file)
            
            if not segment_files:
                print("[ERROR] No hay segmentos")
                return False
            
            if verbose:
                print(f"[Renderer] Combinando {len(segment_files)} segmentos...")
            
            clips = [VideoFileClip(str(f)) for f in segment_files]
            final_clip = concatenate_videoclips(clips, method="compose")
            
            if title:
                from moviepy.editor import TextClip
                title_clip = TextClip(title, fontsize=60, color="white",
                                   method="caption", size=(self.config.width - 100, None),
                                   duration=final_clip.duration)
                title_clip = title_clip.with_position(("center", "bottom"))
                from moviepy.editor import CompositeVideoClip
                final_clip = CompositeVideoClip([final_clip, title_clip])
            
            final_clip.write_videofile(str(output_path), fps=self.config.fps,
                                 codec=self.config.codec, audio_codec=self.config.audio_codec,
                                 bitrate=self.config.bitrate, logger="bar")
            
            for f in segment_files:
                if f.exists():
                    f.unlink()
            
            return True
        except Exception as e:
            print(f"[ERROR] {e}")
            return False
    
    def _parse_timestamp(self, timestamp: str) -> float:
        parts = timestamp.split(":")
        if len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        elif len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        return 0.0
```

### 5.7 src/coordinator.py

```python
import json
import uuid
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

from src.config import get_config


@dataclass
class VideoJob:
    job_id: str
    prompt: str
    script = None
    segments = []
    output_path: Optional[Path] = None
    status: str = "pending"
    error: Optional[str] = None


class VideoCoordinator:
    def __init__(self, verbose: bool = False, config = None):
        self.verbose = verbose
        self.config = config or get_config()
        self.llm = None
        self.media_client = None
        self.tts_engine = None
        self.renderer = None
    
    def initialize(self) -> bool:
        if self.verbose:
            print("[Coordinator] Inicializando...")
        
        try:
            from src.llm.ollama_client import OllamaClient
            self.llm = OllamaClient(
                base_url=self.config.llm.base_url,
                model=self.config.llm.model,
                timeout=self.config.llm.timeout
            )
            if self.verbose:
                print(f"[Coordinator] LLM: {self.config.llm.model}")
        except Exception as e:
            print(f"[ERROR] {e}")
        
        try:
            from src.media.pixabay_client import PixabayClient
            self.media_client = PixabayClient(
                api_key=self.config.pixabay.api_key,
                cache_dir=self.config.paths.cache_dir
            )
        except Exception as e:
            print(f"[ERROR] {e}")
        
        try:
            from src.audio.tts_engine import CoquiTTSEngine
            self.tts_engine = CoquiTTSEngine(
                model_name=self.config.tts.model_name,
                voices_dir=self.config.paths.voices_dir,
                language=self.config.tts.language,
                device=self.config.tts.device
            )
        except Exception as e:
            print(f"[ERROR] {e}")
        
        try:
            from src.video.renderer import VideoRenderer, RenderConfig
            render_config = RenderConfig(
                width=self.config.video.width,
                height=self.config.video.height,
                fps=self.config.video.fps,
                codec=self.config.video.codec,
                audio_codec=self.config.video.audio_codec,
                bitrate=self.config.video.bitrate
            )
            self.renderer = VideoRenderer(
                config=render_config,
                temp_dir=self.config.paths.temp_dir
            )
        except Exception as e:
            print(f"[ERROR] {e}")
        
        return True
    
    def generate_script(self, prompt: str, max_duration: int = 10) -> Optional[any]:
        if not self.llm:
            return None
        try:
            script = self.llm.generate_script(prompt, max_duration, self.verbose)
            if self.verbose:
                print(f"[Coordinator] Guion: {script.title} ({len(script.segments)} segmentos)")
            return script
        except Exception as e:
            print(f"[ERROR] {e}")
            return None
    
    def download_media(self, segments: list, output_dir: Path) -> list:
        if not self.media_client:
            return segments
        output_dir.mkdir(parents=True, exist_ok=True)
        results = []
        
        for segment in segments:
            try:
                query = segment.media_query if hasattr(segment, 'media_query') else segment.get('media_query', '')
                if not query:
                    results.append(segment)
                    continue
                
                if self.verbose:
                    print(f"[Media] Buscando: {query}")
                
                media_path = self.media_client.download_best_match(query, output_dir, prefer_video=True)
                if media_path:
                    segment.media_path = media_path
            except Exception as e:
                print(f"[WARNING] {e}")
            results.append(segment)
        return results
    
    def generate_audio(self, segments: list, output_dir: Path, voice: str = "female") -> list:
        if not self.tts_engine:
            return segments
        output_dir.mkdir(parents=True, exist_ok=True)
        results = []
        
        for i, segment in enumerate(segments):
            text = segment.script if hasattr(segment, 'script') else segment.get('script', '')
            if not text:
                results.append(segment)
                continue
            
            try:
                if self.verbose:
                    print(f"[TTS] Generando audio segmento {i+1}...")
                
                result = self.tts_engine.synthesize(text, output_dir / f"segment_{i:03d}.wav",
                                          voice, verbose=self.verbose)
                if result:
                    segment.audio_path = result.audio_path
            except Exception as e:
                print(f"[WARNING] {e}")
            results.append(segment)
        return segments
    
    def render_final(self, segments: list, output_path: Path, title: Optional[str] = None) -> bool:
        if not self.renderer:
            return False
        
        from src.video.renderer import SegmentData
        
        segment_data = []
        for seg in segments:
            if hasattr(seg, 'script'):
                segment_data.append(SegmentData(
                    id=seg.id,
                    start=seg.start,
                    end=seg.end,
                    script=seg.script,
                    media_query=seg.media_query,
                    mood=seg.mood,
                    media_path=getattr(seg, 'media_path', None),
                    audio_path=getattr(seg, 'audio_path', None)
                ))
        
        return self.renderer.render_video(segment_data, output_path, title, self.verbose)
    
    def run(self, prompt: str, max_duration: int = 10, voice: str = "female",
          output_filename: Optional[str] = None) -> Optional[Path]:
        self.initialize()
        
        script = self.generate_script(prompt, max_duration)
        if not script:
            return None
        
        job_dir = self.config.paths.cache_dir / uuid.uuid4().hex[:8]
        
        media_segments = self.download_media(script.segments, job_dir / "media")
        
        audio_segments = self.generate_audio(media_segments, job_dir / "audio", voice)
        
        if not output_filename:
            safe_title = "".join(c for c in script.title if c.isalnum() or c in " -_").strip()[:50]
            output_filename = f"{safe_title}.mp4"
        
        output_path = self.config.paths.output_dir / output_filename
        
        success = self.render_final(audio_segments, output_path, script.title)
        
        return output_path if success else None
    
    def check_dependencies(self) -> dict:
        deps = {}
        deps["ollama"] = self.llm.is_available() if self.llm else False
        deps["pixabay_api"] = bool(self.config.pixabay.api_key)
        deps["coqui_tts"] = self.tts_engine.is_available() if self.tts_engine else False
        deps["moviepy"] = True
        return deps


def create_coordinator(verbose: bool = False) -> VideoCoordinator:
    return VideoCoordinator(verbose=verbose)
```

### 5.8 vid (CLI Global)

```python
#!/usr/bin/env python3
"""
VideoGen CLI - Comando global 'vid'
Uso: vid "tu prompt aquí" [opciones]
"""

import sys
import os
from pathlib import Path

PROJECT_DIR = Path("/home/alexis/Files/Proyectos")
sys.path.insert(0, str(PROJECT_DIR))


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="VideoGen")
    parser.add_argument("prompt", nargs="?", help="Prompt del video")
    parser.add_argument("-d", "--duration", type=int, default=10)
    parser.add_argument("-v", "--voice", choices=["female", "male", "narrator"], default="female")
    parser.add_argument("-o", "--output", type=str, default=None)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--check-deps", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    
    if args.check_deps:
        print("\n=== Verificando dependencias ===\n")
        deps = {}
        try:
            from src.llm.ollama_client import OllamaClient
            deps["Ollama"] = OllamaClient().is_available()
        except:
            deps["Ollama"] = False
        deps["Pixabay API"] = bool(os.getenv("PIXABAY_API_KEY"))
        try:
            from moviepy import VideoFileClip
            deps["MoviePy"] = True
        except:
            deps["MoviePy"] = False
        try:
            from TTS.api import TTS
            deps["Coqui TTS"] = True
        except:
            deps["Coqui TTS"] = False
        for name, ok in deps.items():
            print(f"  {'✓' if ok else '✗'} {name}")
        return 0
    
    if not args.prompt:
        print("Uso: vid 'tu prompt aquí'")
        return 1
    
    print(f"\n🏁 Generando: {args.prompt}\n")
    
    try:
        from src.coordinator import create_coordinator
        from src.config import get_config
        
        config = get_config()
        config.verbose = args.verbose
        coordinator = create_coordinator(verbose=args.verbose)
        
        output_path = coordinator.run(
            prompt=args.prompt,
            max_duration=args.duration,
            voice=args.voice,
            output_filename=args.output
        )
        
        if output_path and output_path.exists():
            size = output_path.stat().st_size / 1024 / 1024
            print(f"\n✅ Video generado!")
            print(f"   📁 {output_path}")
            print(f"   📊 {size:.2f} MB")
            return 0
        else:
            print("\n❌ Error al generar")
            return 1
    except KeyboardInterrupt:
        print("\n⚠️ Cancelado")
        return 130
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        if args.verbose:
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

### 5.9 .env.example

```bash
# VideoGen Configuration

# Ollama (LLM local)
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3

# Pixabay API (gratis en https://pixabay.com/api/)
PIXABAY_API_KEY=tu_api_key_aqui

# Opciones
VIDEOGEN_VERBOSE=false
```

---

## 6. Uso

### 6.1 Configuración Inicial

```bash
# 1. Activar entorno
cd ~/Files/Proyectos
source venv/bin/activate

# 2. Crear archivo .env
cp .env.example .env

# 3. Editar .env con tu API key de Pixabay
nano .env
# Cambiar: PIXABAY_API_KEY=tu_api_key_aqui

# 4. Verificar dependencias
vid --check-deps
```

### 6.2 Generar Video

```bash
# Básico
vid "Historia de la programación"

# Con opciones
vid "Cambio climático" -d 5 -v female --verbose

# Verificar estado
vid --check-deps
```

### 6.3 Comandos Útiles

| Comando | Descripción |
|---------|-------------|
| `vid "prompt"` | Generar video |
| `vid --check-deps` | Verificar instalaciones |
| `ollama serve` | Iniciar Ollama |
| `ollama list` | Ver modelos disponibles |

---

## 7. Solución de Problemas

### Ollama no conecta
```bash
# Verificar servicio
curl http://localhost:11434/api/tags

# Iniciar si no está corriendo
ollama serve
```

### Sin memoria
- Usar modelo más pequeño: `ollama pull gemma:2b`
- Reducir duración del video

### Pixabay sin resultados
- Verificar API key en `.env`
- Usar queries más genéricas

### TTS lento
- Usar versión CPU de torch (ya configurada)
- Reducir texto por segmento

---

## 8. Notas Importantes

1. **Python 3.9-3.11 ONLY** - Coqui TTS no funciona con Python 3.12+
2. **VIP**: Siempre activar el venv antes de usar `vid`
3. **OUTPUT**: Videos se guardan en `~/Files/Proyectos/output/`

---

## 9. Licencia

MIT - Libre uso y modificación

---

*Documento generado: VideoGen Specification*
