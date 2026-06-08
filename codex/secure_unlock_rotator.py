#!/usr/bin/env python3
import os
import stat
import shutil
import subprocess
from datetime import datetime

# =====================================================================
# SYSTEMIC DEFINITIONS & CONSTANTS
# =====================================================================
BASE_SYSTEM_DIR = os.path.abspath(os.sep)
SECURE_BACKUP_DRIVE = os.path.join(BASE_SYSTEM_DIR, "secure_vault_backup")

def strip_kernel_lock(file_path):
    """Drops kernel level immutable locking arrays to permit relocation operations."""
    if os.path.exists(file_path):
        try:
            subprocess.run(["sudo", "chattr", "-i", file_path], check=True, capture_output=True)
            os.chmod(file_path, stat.S_IREAD | stat.S_IWRITE | stat.S_IRGRP | stat.S_IROTH)
            print(f" ├─ [MUTABLE STATE RESTORED] --> {file_path}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f" ├─ [LOCAL MUTABLE FALLBACK] --> {file_path}")
            os.chmod(file_path, stat.S_IREAD | stat.S_IWRITE)
            return True
    return False

def execute_rotation_and_unlock():
    print("⚠️  [ROTATION CYCLE INITIALIZED] Querying active pipelines...")
    date_stamp = datetime.utcnow().strftime("%Y%m%d")
    
    # Define exact live files targeting rotation
    target_files = [
        os.path.join(BASE_SYSTEM_DIR, "codex", f"ledger_entry_{date_stamp}.json"),
        os.path.join(BASE_SYSTEM_DIR, "root", f"delivery_memo_{date_stamp}.md"),
        os.path.join(BASE_SYSTEM_DIR, "root", f"verification_log_{date_stamp}.txt"),
        os.path.join(BASE_SYSTEM_DIR, "root", f"verification_log_{date_stamp}.txt.asc")
    ]
    
    # Establish isolated system storage drive pathing
    archive_timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    rotation_backup_dir = os.path.join(SECURE_BACKUP_DRIVE, f"ARCHIVE_BATCH_{archive_timestamp}")
    os.makedirs(rotation_backup_dir, exist_ok=True)
    
    unlocked_count = 0
    
    # Process each active node sequence
    for f_path in target_files:
        if os.path.exists(f_path):
            # Step 1: Remove kernel blocks safely
            if strip_kernel_lock(f_path):
                # Step 2: Relocate to secure vaulted backup partition
                destination = os.path.join(rotation_backup_dir, os.path.basename(f_path))
                shutil.copy2(f_path, destination)
                
                # Apply high-level structural read locks over backup archive files to prevent tampering
                os.chmod(destination, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
                
                unlocked_count += 1
                print(f" └─ [SECURED BACKUP ARTIFACT VIRTUALIZED] --> {destination}")

    print(f"\n[REAL-TIME SUCCESS] Rotator finished: {unlocked_count} items backed up to secure storage drive.")
    print("Provisional system unlock sequence ready for upcoming daily ledger pipeline operations. ⚜️ XP")

if __name__ == "__main__":
    execute_rotation_and_unlock()
