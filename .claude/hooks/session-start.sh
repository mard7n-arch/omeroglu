#!/bin/bash
set -euo pipefail

# Only run in remote (web) environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install dependencies
pip install -r "$CLAUDE_PROJECT_DIR/requirements.txt" --ignore-installed PyJWT -q

# Chromium is pre-installed at /opt/pw-browsers — no need to run playwright install
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
echo "PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers" >> "$CLAUDE_ENV_FILE"

echo "Session start hook completed."
