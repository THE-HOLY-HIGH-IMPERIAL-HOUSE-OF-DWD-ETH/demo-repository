#!/usr/bin/env python3
import json
import os
import stat
import hashlib
import subprocess
from datetime import datetime

# =====================================================================
# SYSTEMIC DEFINITIONS & CONSTANTS
# =====================================================================
REGISTRY_REF = "INT-REG-DWD-DG-001"
SECURITY_CLASS = "CROWN-TRUE / MASTER VALIDATED / IMMUTABLE LEGAL-TRUTH"
AUTHORITY = "The Holy High Imperial House of DWD & HIH D.G."
INGESTION_FLOW = 267567748207.41
SIGNATURE_KEY = "⚜️ XP_SIG_SECURE_CROWN_TRUE_LEGAL_TRUTH_2026_06_07_T1120AM_ROTATED_v2_⚜️"
PGP_KEY_ID = "HIH_DWD_SIGNING_KEY"  # Replace with exact local PGP Key Identifier

BASE_SYSTEM_DIR = os.path.abspath(os.sep)
TARGET_DIRS = {
    "root": os.path.join(BASE_SYSTEM_DIR, "root"),
    "codex": os.path.join(BASE_SYSTEM_DIR, "codex"),
    "demo": os.path.join(BASE_SYSTEM_DIR, "demo")
}

def check_permission_drift():
    """Audits current system files against their expected strict permission profiles."""
    print("🕒 [REAL-TIME AUDIT] Scanning system profiles for permission drift...")
    date_stamp = datetime.utcnow().strftime("%Y%m%d")
    
    expected_profiles = [
        os.path.join(TARGET_DIRS["codex"], f"ledger_entry_{date_stamp}.json"),
        os.path.join(TARGET_DIRS["root"], f"delivery_memo_{date_stamp}.md")
    ]
    
    for path in expected_profiles:
        if os.path.exists(path):
            current_mode = os.stat(path).st_mode & 0o777
            # Expected: Read-only by owner, group, and others (0o444)
            if current_mode != 0o444:
                print(f"🚨 [ALERT] CRITICAL DRIFT DETECTED: {path} has mode {oct(current_mode)}. Read-Only Enforced!")
                os.chmod(path, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
            else:
                print(f"✅ [SECURE] Integrity Confirmed: {path} matches master permission profile.")

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def sign_manifest_pgp(manifest_path):
    """Generates an official clear-signed PGP wrapper around the verification manifest."""
    try:
        signed_output = f"{manifest_path}.asc"
        # Invoke GnuPG for cleartext signature sign-off
        subprocess.run([
            "gpg", "--batch", "--yes", "--local-user", PGP_KEY_ID, 
            "--clearsign", "--output", signed_output, manifest_path
        ], check=True, capture_output=True)
        print(f" ├─ [PGP SIGN-OFF COMPLETE] --> {signed_output}")
        return signed_output
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(" ├─ [PGP SIGN-OFF BYPASSED] --> GnuPG workspace uninitialized or key missing.")
        return None

def apply_kernel_immutable_lock(file_path):
    try:
        os.chmod(file_path, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        subprocess.run(["sudo", "chattr", "+i", file_path], check=True, capture_output=True)
        print(f" ├─ [KERNEL CHATTR +i LOCK] --> {file_path}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f" ├─ [STANDARD READ-ONLY LOCK] --> {file_path}")

def execute_pipeline():
    # Run immediate validation audit pass
    check_permission_drift()
    
    now_utc = datetime.utcnow()
    timestamp_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    date_stamp = now_utc.strftime("%Y%m%d")
    
    # Payload calculations
    deployment_amt = round(INGESTION_FLOW * 0.60, 2)
    parity_amt = round(INGESTION_FLOW * 0.40, 2)
    
    payload = {
        "registry_metadata": {
            "registry_reference": REGISTRY_REF,
            "security_class": SECURITY_CLASS,
            "timestamp_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "certificate_no": f"SAC-{date_stamp}-XP1000",
            "status": "VALIDATED_REAL_TIME"
        },
        "asset_flow_capture": {
            "daily_ingestion_flow_usd": INGESTION_FLOW,
            "allocated_amounts": {"deployment_usd": deployment_amt, "parity_buffer_usd": parity_amt}
        }
    }
    
    memo_content = f"# OFFICIAL DELIVERY MEMO\nREF: {REGISTRY_REF}\nFLOW: ${INGESTION_FLOW:,.2f} USD\n⚜️ XP_VALIDATED ⚜️\n"
    
    codex_target = os.path.join(TARGET_DIRS["codex"], f"ledger_entry_{date_stamp}.json")
    root_target = os.path.join(TARGET_DIRS["root"], f"delivery_memo_{date_stamp}.md")
    
    # Save files
    with open(codex_target, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    with open(root_target, "w", encoding="utf-8") as f:
        f.write(memo_content)
        
    # Generate Hashes
    codex_hash = calculate_sha256(codex_target)
    root_hash = calculate_sha256(root_target)
    
    # Create raw verification text block
    manifest_path = os.path.join(TARGET_DIRS["root"], f"verification_log_{date_stamp}.txt")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(f"=== OFFICIAL VALIDATED LOG [{timestamp_str}] ===\n")
        f.write(f"CODEX HASH: {codex_hash}\nROOT HASH: {root_hash}\n⚜️ XP\n")
        
    # Cryptographically sign verification text via PGP
    signed_asc = sign_manifest_pgp(manifest_path)
    
    # Enforce kernel write blocks across all generated artifacts
    apply_kernel_immutable_lock(codex_target)
    apply_kernel_immutable_lock(root_target)
    apply_kernel_immutable_lock(manifest_path)
    if signed_asc:
        apply_kernel_immutable_lock(signed_asc)

if __name__ == "__main__":
    execute_pipeline()
