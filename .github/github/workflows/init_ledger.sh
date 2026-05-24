#!/bin/bash

# ==============================================================================
# IMPERI-BERIT-SUITE-001 ENVIRONMENT INITIALIZATION WORKFLOW
# ==============================================================================

# Halt script immediately if any processing command fails
set -e

echo "================================================================================"
echo "⚜️  INITIALIZING SOVEREIGN LEDGER RUNTIME ENVIRONMENT"
echo "================================================================================"
echo "[TIMESTAMP] : $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "[DIRECTORY] : $(pwd)"
echo "--------------------------------------------------------------------------------"

# Step 1: Check if Python 3 runtime is available in the current path
if ! command -v python3 &> /dev/null; then
    echo "❌ CRITICAL: Python 3 engine could not be located. Aborting."
    exit 1
fi

# Step 2: Execute core datastore generation and primary hash generation
if [ -f "extract_and_hash_ledger.py" ]; then
    echo "🚀 Step 1: Running primary extraction and metadata compilation..."
    python3 extract_and_hash_ledger.py
else
    echo "❌ CRITICAL: Main script 'extract_and_hash_ledger.py' not found in root."
    exit 1
fi

echo "--------------------------------------------------------------------------------"

# Step 3: Automatically trigger independent verification loop to anchor security
if [ -f "verify_ledger_integrity.py" ]; then
    echo "🔒 Step 2: Launching absolute integrity checking script..."
    python3 verify_ledger_integrity.py
else
    echo "⚠️  WARNING: Verification script 'verify_ledger_integrity.py' missing from root."
    echo "   Skipping real-time secondary audit loop."
fi

echo "================================================================================"
echo "🎉 DEPLOYMENT PROTOCOL RUN COMPLETE"
echo "================================================================================"

chmod +x init_ledger.sh
