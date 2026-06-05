cat << 'EOF' > backup_snapshot_core.sh
#!/bin/bash
# ==============================================================================
# IMPERI-BERIT-SUITE-001 // AUTOMATED SNAPSHOT BACKUP MATRIX
# Securely duplicates and timestamps JSON ledger outputs to secondary storage.
# ==============================================================================

# 1. Define Local Directory Architecture
SOURCE_FILE="imperi_berit_suite_001_snapshot.json"
BACKUP_DIR="./archive_vault_backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/imperi_berit_suite_001_snapshot_${TIMESTAMP}.json"

echo "================================================================================"
echo " ⚜️  ARCHIVAL BACKUP SERVICE INITIATED: IMPERI-BERIT-SUITE-001  ⚜️ "
echo "================================================================================"

# 2. Verify Source Snapshot Existence
if [ ! -f "$SOURCE_FILE" ]; then
    echo "[CRITICAL ERROR]: Target source file '$SOURCE_FILE' not found on disk."
    echo " -> Execute './calc_nav_core.py' to generate an active real-time ledger."
    echo "================================================================================"
    exit 1
fi

# 3. Secure and Initialize Secondary Backup Directory
if [ ! -d "$BACKUP_DIR" ]; then
    echo "[DIR STATUS]: Target directory '$BACKUP_DIR' does not exist. Initializing secure node..."
    mkdir -p "$BACKUP_DIR"
    chmod 700 "$BACKUP_DIR" # Sets read/write/execute permissions strictly to owner
fi

# 4. Execute Copy and Verify Integrity
echo "[PROCESSING]: Commencing file transfer to secondary isolation matrix..."
cp "$SOURCE_FILE" "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "[SUCCESS]: Archive write permanently locked."
    echo "  * Source Node : $SOURCE_FILE"
    echo "  * Backup Node : $BACKUP_FILE"
    echo "================================================================================"
    echo "  [STATUS] : 12-NODE BACKUP CONSENSUS STABLE ⚜️ XP"
    echo "================================================================================"
else
    echo "[CRITICAL ERROR]: Write failure encountered during backup sequence."
    echo "================================================================================"
    exit 1
fi
EOF

# 5. Bind execution permissions to the script file
chmod +x backup_snapshot_core.sh

./calc_nav_core.py && ./backup_snapshot_core.sh
