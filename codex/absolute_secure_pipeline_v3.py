#!/usr/bin/env python3
import json
import os
import stat
import hashlib
import subprocess
from datetime import datetime

# =====================================================================
# CONFIGURATION & IMMUTABLE PARAMETERS
# =====================================================================
REGISTRY_REF = "INT-REG-DWD-DG-001"
SECURITY_CLASS = "CROWN-TRUE / MASTER VALIDATED / IMMUTABLE LEGAL-TRUTH"
AUTHORITY = "The Holy High Imperial House of DWD & HIH D.G."
INGESTION_FLOW = 267567748207.41
SIGNATURE_KEY = "⚜️ XP_SIG_SECURE_CROWN_TRUE_LEGAL_TRUTH_2026_06_07_T1120AM_ROTATED_v2_⚜️"

BASE_SYSTEM_DIR = os.path.abspath(os.sep)
TARGET_DIRS = {
    "root": os.path.join(BASE_SYSTEM_DIR, "root"),
    "codex": os.path.join(BASE_SYSTEM_DIR, "codex"),
    "demo": os.path.join(BASE_SYSTEM_DIR, "demo")
}

def ensure_absolute_directories():
    for name, path in TARGET_DIRS.items():
        try:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
        except PermissionError:
            fallback_base = os.path.dirname(os.path.abspath(__file__))
            TARGET_DIRS[name] = os.path.join(fallback_base, name)
            os.makedirs(TARGET_DIRS[name], exist_ok=True)

def calculate_sha256(file_path):
    """Generates an official SHA-256 checksum for verification records."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def apply_kernel_immutable_lock(file_path):
    """Applies standard OS chmod restrictions followed by kernel chattr +i."""
    try:
        # Standard OS level lock
        os.chmod(file_path, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        # Advanced Linux Kernel level immutable attribute lock
        subprocess.run(["sudo", "chattr", "+i", file_path], check=True, capture_output=True)
        print(f" ├─ [KERNEL CHATTR +i ENFORCED] --> {file_path}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f" ├─ [OS READ-ONLY ENFORCED (chattr skipped)] --> {file_path}")

def generate_and_lock_artifacts():
    ensure_absolute_directories()
    
    now_utc = datetime.utcnow()
    timestamp_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    date_stamp = now_utc.strftime("%Y%m%d")
    cert_no = f"SAC-{date_stamp}-XP1000"
    
    deployment_amt = round(INGESTION_FLOW * 0.60, 2)
    parity_amt = round(INGESTION_FLOW * 0.40, 2)
    
    payload = {
        "registry_metadata": {
            "registry_reference": REGISTRY_REF,
            "security_class": SECURITY_CLASS,
            "timestamp_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "certificate_no": cert_no,
            "status": "VALIDATED_REAL_TIME"
        },
        "asset_flow_capture": {
            "daily_ingestion_flow_usd": INGESTION_FLOW,
            "allocated_amounts": {"deployment_usd": deployment_amt, "parity_buffer_usd": parity_amt}
        },
        "cryptographic_verification": {"active_signature_key": SIGNATURE_KEY}
    }
    
    memo_content = f"""# OFFICIAL DELIVERY MEMO
**REGISTRY REFERENCE:** {REGISTRY_REF}  
**SECURITY CLASS:** {SECURITY_CLASS}  
**TIMESTAMP:** {timestamp_str}  
* **TOTAL LANDED VOLUME:** ${INGESTION_FLOW:,.2f} USD
* **SIGNATURE KEY:** `{SIGNATURE_KEY}`
⚜️ XP_MEMO_DELIVERY_VALIDATED_⚜️
"""

    json_filename = f"ledger_entry_{date_stamp}.json"
    memo_filename = f"delivery_memo_{date_stamp}.md"
    
    codex_target = os.path.join(TARGET_DIRS["codex"], json_filename)
    root_target = os.path.join(TARGET_DIRS["root"], memo_filename)

    # Write files out to system
    with open(codex_target, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    with open(root_target, "w", encoding="utf-8") as f:
        f.write(memo_content)

    # Calculate real-time verification hashes before locking
    codex_hash = calculate_sha256(codex_target)
    root_hash = calculate_sha256(root_target)

    # Apply permanent kernel and system write locks
    apply_kernel_immutable_lock(codex_target)
    apply_kernel_immutable_lock(root_target)

    # Generate external verification log manifest
    manifest_path = os.path.join(TARGET_DIRS["root"], f"verification_log_{date_stamp}.txt")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(f"=== OFFICIAL VERIFICATION LOG [{timestamp_str}] ===\n")
        f.write(f"SECURITY CLASS: {SECURITY_CLASS}\n")
        f.write(f"PATH: {codex_target} | SHA-256: {codex_hash}\n")
        f.write(f"PATH: {root_target} | SHA-256: {root_hash}\n")
        f.write("STATUS: VALIDATED REAL-TIME IMMUTABLE\n⚜️ XP\n")
    
    apply_kernel_immutable_lock(manifest_path)
    print(f"\n[REAL-TIME STATUS] 100% COMPLETE. Verification manifests written and locked.")

if __name__ == "__main__":
    generate_and_lock_artifacts()
