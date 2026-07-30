#!/usr/bin/env bash
set -euo pipefail

# --- Config ---
DOWNLOADS="$HOME/Descargas"
DESTINO="/home/ale/university/ZPROPIO/PAPER/NOTION-INVESTIGACION/MODELO LIF"
TEMP_DIR=$(mktemp -d)

cleanup() {
    rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

# --- Find latest zip in Downloads ---
LATEST_ZIP=$(ls -t "$DOWNLOADS"/*.zip 2>/dev/null | head -1)
if [ -z "$LATEST_ZIP" ]; then
    echo "No se encontró ningún archivo .zip en $DOWNLOADS"
    exit 1
fi

echo "1. Procesando: $LATEST_ZIP"

# --- First extraction ---
echo "2. Primera descompresión..."
unzip -q "$LATEST_ZIP" -d "$TEMP_DIR/primer_nivel"

# --- Find inner zip ---
INNER_ZIP=$(find "$TEMP_DIR/primer_nivel" -name '*.zip' | head -1)
if [ -z "$INNER_ZIP" ]; then
    echo "No se encontró un zip interno. Quizás no es un export de Notion."
    exit 1
fi

# --- Second extraction ---
echo "3. Segunda descompresión..."
unzip -q "$INNER_ZIP" -d "$TEMP_DIR/segundo_nivel"

# --- Find the .md file and its companion folder ---
MD_FILE=$(find "$TEMP_DIR/segundo_nivel" -maxdepth 1 -name '*.md' | head -1)
if [ -z "$MD_FILE" ]; then
    echo "No se encontró archivo .md en el export."
    exit 1
fi

# The folder with same basename as the .md file (without extension)
BASENAME=$(basename "$MD_FILE" .md)
DATA_DIR="$TEMP_DIR/segundo_nivel/$BASENAME"

echo "4. Copiando archivos al destino..."
cp "$MD_FILE" "$DESTINO/"

if [ -d "$DATA_DIR" ]; then
    cp -r "$DATA_DIR" "$DESTINO/"
fi

# --- Remove the original zip from Downloads ---
echo "5. Eliminando zip de Descargas..."
rm "$LATEST_ZIP"

echo "6. Hecho. Archivos copiados a:"
echo "   $DESTINO"
echo ""
ls -la "$DESTINO"
