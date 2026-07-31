## UNIVERSIDAD - Backup y sincronización con GitHub

### ¿Qué hace este script?

El comando `backup` realiza dos cosas:
1. **Copia de seguridad local** en `~/.unibackup/` usando `rsync`
2. **Subida a GitHub** del repositorio Universidad, incluyendo las notas de Obsidian

### Prerrequisitos

- Tener git instalado
- Tener una cuenta en GitHub con un repositorio llamado `Universidad`
- Tener una clave SSH configurada y vinculada a GitHub
- Tener el repositorio clonado localmente

### Archivos involucrados

| Archivo | Propósito |
|---|---|
| `~/.unibackup/` | Backup local unificado |
| Script en `~/bin/backup` | Script que orquesta todo |
| Repositorio local (ej: `~/universidad/`) | Carpeta con los archivos de la facultad |
| Vault de Obsidian (según cada dispositivo) | Notas de Obsidian que se sincronizan a `Obsidian/` dentro del repo |

### Configuración inicial (por dispositivo)

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:alexistpe/Universidad.git ~/universidad
   cd ~/universidad
   ```

2. **Crear el script de backup** en `~/bin/backup` con el siguiente contenido:

   ```bash
   #!/bin/bash
   BACKUP_DIR="$HOME/.unibackup"
   REPO_DIR="$HOME/universidad"
   OBSIDIAN_SRC="$HOME/ruta/local/de/tu/vault/obsidian/"
   HOST="$(hostname)"
   DATE=$(date '+%Y-%m-%d %H:%M')

   echo "Iniciando respaldo de Universidad..."

   mkdir -p "$BACKUP_DIR/obsidian" "$BACKUP_DIR/home"
   rsync -avh --delete "$OBSIDIAN_SRC" "$BACKUP_DIR/obsidian/"
   rsync -avh --delete "$REPO_DIR/" "$BACKUP_DIR/home/"

   rsync -avh --delete "$OBSIDIAN_SRC" "$REPO_DIR/Obsidian/"

   cd "$REPO_DIR" || exit 1
   if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
       git add -A
       git commit -m "backup automatico - $DATE - $HOST"
       git push origin main
       echo "Respaldo subido a GitHub correctamente."
   else
       echo "Sin cambios nuevos. No se realizó commit."
   fi

   echo "¡Backup completado!"
   ```

   > **Importante:** Cambiar `OBSIDIAN_SRC` por la ruta real del vault de Obsidian en cada dispositivo.

3. **Dar permisos de ejecución:**
   ```bash
   chmod +x ~/bin/backup
   ```

4. **Verificar que `~/bin/` esté en el `PATH`** para que el comando `backup` funcione desde cualquier terminal. Agregar esto al `~/.bashrc` o `~/.zshrc` si no está:
   ```bash
   export PATH="$HOME/bin:$PATH"
   ```

### Uso diario

Simplemente ejecutar en la terminal:
```bash
backup
```

### Notas importantes

- No requiere `*.pdf` en `.gitignore` (los PDFs se suben al repo)
- `*.directory` sí está ignorado (metadatos de KDE que no aportan)
- El mensaje de commit sigue el formato: `backup automatico - YYYY-MM-DD HH:MM - NOMBRE_DEL_PC`
- Si no hay cambios nuevos, el script avisa y no crea un commit vacío
- Las notas de Obsidian se ubican dentro del repo en una carpeta llamada `Obsidian/`
