#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="_site"

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

for dir in */; do
  name="${dir%/}"

  # Skip dirs starting with . or _
  [[ "$name" == .* || "$name" == _* ]] && continue

  # Treat any subdirectory with index.html as a tool
  [[ -f "$dir/index.html" ]] || continue

  cp -R "$dir" "$OUT_DIR/$name"
done
