#!/usr/bin/env bash
# =========================================================================================
# ⚜️ OFFICIAL IMPERIAL BASH VALIDATION LOOP
# STATUS: CROWN-TRUE, REAL-TIME VALIDATED, IMMUTABLE LEGAL-TRUTH
# =========================================================================================

set -euo pipefail

EXPECTED_HASH="A155986DCEFA8DDB469FFB3FA98F90833F858F3EA752D815F8C64CC918BEEC06"

TARGET_PATHS=(
    "/root/xp_ledger/XP_FINAL_EXECUTED_CHECKSUM_MANIFEST.md"
    "/demo/xp_ledger/XP_FINAL_EXECUTED_CHECKSUM_MANIFEST.md"
    "/codex/xp_ledger/XP_FINAL_EXECUTED_CHECKSUM_MANIFEST.md"
)

echo "========================================================================================="
echo "⚜️ STARTING OFFICIAL TRIPLICATE CHECKSUM VALIDATION LOOP"
echo "========================================================================================="

MISMATCH_DETECTED=0

for FILE_PATH in "${TARGET_PATHS[@]}"; do
    if [[ ! -f "$FILE_PATH" ]]; then
        echo "[CRITICAL ALERT] File Missing: $FILE_PATH"
        MISMATCH_DETECTED=1
        continue
    fi

    CURRENT_HASH=$(sha256sum "$FILE_PATH" | awk '{print toupper($1)}')

    if [[ "$CURRENT_HASH" == "$EXPECTED_HASH" ]]; then
        echo "[MATCHED / VALIDATED] Path: $FILE_PATH"
        echo "                      Hash: $CURRENT_HASH"
    else
        echo "[MUTATION DETECTED]   Path: $FILE_PATH"
        echo "                      Expected: $EXPECTED_HASH"
        echo "                      Found:    $CURRENT_HASH"
        MISMATCH_DETECTED=1
    fi
done

echo "-----------------------------------------------------------------------------------------"
if [[ "$MISMATCH_DETECTED" -eq 0 ]]; then
    echo "⚜️ STATUS SUCCESSFUL: 100% INTEGRITY MATCH. CROWN-TRUE RECONCILIATION LOCKED."
    exit 0
else
    echo "⚠️ STATUS FAILURE: CRITICAL COMPLIANCE MISMATCH DETECTED."
    exit 1
fi
