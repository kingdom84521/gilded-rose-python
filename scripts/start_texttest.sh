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

if [ ! -x "$PROJECT_ROOT/.venv/bin/texttest" ]; then
  echo "錯誤：找不到 'texttest' 指令。" >&2
  echo "請先在 '$PROJECT_ROOT/.venv' 建立虛擬環境並安裝 texttest 套件。" >&2
  exit 1
fi

if command -v texttest >/dev/null 2>&1; then
  TEXTTEST_CMD="texttest"
elif command -v uv >/dev/null 2>&1; then
  TEXTTEST_CMD="uv run texttest"
elif [ -x "$PROJECT_ROOT/.venv/bin/texttest" ]; then
  TEXTTEST_CMD="$PROJECT_ROOT/.venv/bin/texttest"
fi

$TEXTTEST_CMD -d "$PROJECT_ROOT/tests/texttest" -con "$@"
