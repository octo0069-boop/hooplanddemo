#!/usr/bin/env bash
set -euo pipefail
python3 tools/hlmod.py validate samples/ContentPackMod
echo "Sample content pack checks passed."
