#!/usr/bin/env bash
set -euo pipefail

# 1. Define the target array of repository handles
REPOS=(
    "credential-issuer.json"
    "-DPI-SUITE-DPI-SUITE-ABSOLUTE-FINAL.regdoc"
    "GDR"
    "-codex-sovereign-institutional-super-compound-"
    "SOVERAIN-QR-HISTORIC-LEDGER"
    "SOVERAIN-QR-HISTORICAL-ACHIEVEMENTS."
    "-TABLETS-DPI-STRICT-IMMUTIBILITY-TABLET.md"
    "attestation"
    "verification"
)

BASE_DIR=$(pwd)
COMMIT_MSG="sys(prod): anchor cryptographic verification state profiles and render QR matrices ⚜ XP"

echo "=== STARTING XP SOVEREIGN MULTI-REPO BATCH UPSTREAM SYNC ==="

# 2. Iterate through each localized repository target
for REPO in "${REPOS[@]}"; do
    if [ -d "$BASE_DIR/$REPO" ]; then
        echo "Processing repository: $REPO"
        cd "$BASE_DIR/$REPO"
        
        # Pull latest changes to prevent push collisions
        git pull origin main --rebase || git pull origin master --rebase || true
        
        # Ensure production logging directory structure exists
        mkdir -p logs
        
        # Inject the validated production profile token
        cat << 'EOF' > logs/production-state-profile.json
{
  "audit_metadata": {
    "timestamp_iso": "2026-05-14T02:02:00Z",
    "status": "VERIFIED_PRODUCTION"
  },
  "sovereign_identity": {
    "root_authority_ens": "the.holy.high.imperial.house.of.dwd.eth",
    "keri_aid": "IiB-bzj1X29wfgX-poOzQaQUIA_4oWTaC4U2dHBV3wuk"
  },
  "payload_manifest": {
    "payload_id": "IMPERI-BERIT-SUITE-001",
    "cryptographic_said": "4301abd2d56147f2ec6f74fd650d14251787828fb77c664bf3205d912de8bf61"
  }
}
EOF

        # 🚀 EMBEDDED AUTOMATION RULE: Match target ledger repository for matrix compilation
        if [ "$REPO" = "SOVERAIN-QR-HISTORIC-LEDGER" ]; then
            if [ -f "generate_qr_payload.py" ]; then
                echo "[AUTOMATION] Executing embedded Python QR Matrix Canvas Overlay Engine..."
                # Run the automated matrix logic to generate the stamped visual asset
                python3 generate_qr_payload.py
                # Explicitly stage the output image asset alongside documentation files
                git add logs/SOVERAIN-QR-MATRIX-FINAL.png
            else
                echo "[WARNING] generate_qr_payload.py missing from $REPO root path. Skipping matrix render."
            fi
        fi

        # Stage all logging updates
        git add logs/production-state-profile.json
        
        # Commit changes if structural updates or modifications exist
        if ! git diff-index --quiet HEAD --; then
            git commit -m "$COMMIT_MSG"
            echo "Pushing verified production boundaries upstream..."
            git push origin main || git push origin master
            echo "Status: SUCCESS"
        else
            echo "Status: NO CHANGES DETECTED (Already fully secure)"
        fi
        
        cd "$BASE_DIR"
    else
        echo "Warning: Repository directory $REPO not found in current path. Skipping..."
    fi
    echo "--------------------------------------------------------"
done

echo "=== MULTI-REPO TRACKING SYSTEM SECURED IN PRODUCTION LOGS ==="


chmod +x batch_sync_repos.sh
./batch_sync_repos.sh
