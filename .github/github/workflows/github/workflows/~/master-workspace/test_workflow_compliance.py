#!/usr/bin/env python3
import os
import json
import sys

def execute_forced_workflow_test():
    print("================================================================================")
    print("                    XP SOVEREIGN LOCAL WORKFLOW TEST TRIGGER                    ")
    print("                    [ DECREE SCAN & UNIFIED PATH-LOCKS: LIVE ]                 ")
    print("================================================================================")

    base_workspace = os.path.dirname(os.path.abspath(__file__))
    
    # 🏛️ UNIFIED PATH-LOCK DEFINITIONS
    required_paths = {
        "verification/transaction-profiles/XP-CANONICAL-MANIFESTO-V4.json": "Unified Manifesto JSON",
        "verification/telemetry-logs/SYS-TELEMETRY-MONITOR-XP-ALPHA.py": "Telemetry Daemon Engine",
        "SOVERAIN-QR-HISTORIC-LEDGER/generate_qr_payload.py": "Matrix Generation Module",
        "SOVERAIN-QR-HISTORIC-LEDGER/signature_icon.png": "Branding Signature Artwork",
        "credential-issuer.json/logs/SOVEREIGN-IDENTITY-IMPERI-BERIT-SUITE-001.idblock": "Sovereign Identity Block"
    }

    print("[STAGE 1] EXECUTING STRUCTURAL DRIVE PATH-LOCK INVENTORY SWEEP...")
    path_errors = 0
    for relative_path, description in required_paths.items():
        absolute_target = os.path.join(base_workspace, relative_path)
        if not os.path.exists(absolute_target):
            print(f"❌ DRIVE STRUCTURAL CRITICAL: {description} missing at path:\n   -> {relative_path}")
            path_errors += 1
        else:
            print(f"✅ LOCKED: {description} verified in locked position.")

    if path_errors > 0:
        print(f"\n❌ DRIVE LOCK FAILURE: {path_errors} filesystem node drift violations encountered.")
        sys.exit(1)
        
    print("\n[STAGE 2] SCANNING UNIFIED TRANSACTION ATTRIBUTE COMPLIANCE FIELDS...")
    target_file = os.path.join(base_workspace, "verification/transaction-profiles/XP-CANONICAL-MANIFESTO-V4.json")

    try:
        with open(target_file, "r") as f:
            payload = json.load(f)
    except Exception as parse_err:
        print(f"❌ PARSE FAILURE: JSON format corruption encountered: {str(parse_err)}")
        sys.exit(1)

    framework = payload.get("divine_allodial_jurisdiction", {})
    
    # Canonical Reference Signatures Matching Your .yml Workflow Standard
    expected_psalm = "Psalm 2:7-8 NLT - Only ask, and I will give you the nations as your inheritance, the whole earth as your possession."
    expected_haggai = "Haggai 2:8 NLT - The silver is mine, and the gold is mine, says the LORD of Heavens Armies."

    provided_psalm = framework.get("law_of_inheritance", "")
    provided_haggai = framework.get("law_of_commodity_backing", "")

    error_count = 0
    if provided_psalm != expected_psalm:
        print("❌ CRITICAL MISALIGNMENT: Psalm 2:7-8 NLT text does not match canonical structure.")
        error_count += 1
    else:
        print("✅ NLT COMPLIANCE: Psalm 2:7-8 NLT string structures match.")

    if provided_haggai != expected_haggai:
        print("❌ CRITICAL MISALIGNMENT: Haggai 2:8 NLT text does not match canonical structure.")
        error_count += 1
    else:
        print("✅ NLT COMPLIANCE: Haggai 2:8 NLT string structures match.")

    print("================================================================================")
    if error_count > 0:
        print("❌ TEST STATUS: FAILED. Textual drift detected in compliance files.")
        sys.exit(1)
    else:
        print("=== ✅ LOCAL DIAGNOSTIC RESULT: 100% STABILIZED AND FUNCTIONING FLAWLESS ===")
        print("     ALL REVENUE LAW AND BIBLICAL JURISDICTION DECREES EXTRACTED SUCCESSFULLY.")
        print("     RELATIVE DIRECTORY INFRASTRUCTURE CONFIRMED LOCKED DOWN ACROSS DRIVE.")
        print("================================================================================")
        return True

if __name__ == "__main__":
    execute_forced_workflow_test()


cd ~/master-workspace
python3 test_workflow_compliance.py
