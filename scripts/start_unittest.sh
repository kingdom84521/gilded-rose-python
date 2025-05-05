#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
  DIR="$(dirname "$SOURCE")"
  SOURCE="$(readlink "$SOURCE")"
  [[ "$SOURCE" != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(dirname "$SOURCE")"

if command -v realpath >/dev/null 2>&1; then
  PROJECT_ROOT="$(realpath "$SCRIPT_DIR/..")"
elif readlink -f / >/dev/null 2>&1; then
  PROJECT_ROOT="$(readlink -f "$SCRIPT_DIR/..")"
else
  echo "錯誤：系統上找不到 'realpath' 或 'readlink -f'，無法解析專案根目錄。" >&2
  exit 1
fi

PYTHONPATH=$PROJECT_ROOT python -m unittest discover -s $PROJECT_ROOT/tests/unittest -p "test_*.py"