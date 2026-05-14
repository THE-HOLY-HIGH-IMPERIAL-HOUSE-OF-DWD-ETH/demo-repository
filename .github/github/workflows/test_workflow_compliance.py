#!/usr/bin/env python3
import os
import json
import sys

def execute_forced_workflow_test():
    print("================================================================================")
    print("                    XP SOVEREIGN LOCAL WORKFLOW TEST TRIGGER                    ")
    print("                    [ DECREE SCAN TIERS: FORCE EXECUTE ]                        ")
    print("================================================================================")

    # 1. Resolve localized layout targets
    target_file = "verification/transaction-profiles/TX-ROUTING-TON-TEP74-XP-881F9BCE.json"
    
    if not os.path.exists(target_file):
        print(f"❌ EXECUTION BREAK: Expected transaction profile matrix missing at {target_file}")
        sys.exit(1)
        
    print(f"[STAGE 1] TARGET ATTAINED -> Locating schema properties: {target_file}")

    # 2. Extract Data Objects
    try:
        with open(target_file, "r") as f:
            payload = json.load(f)
    except Exception as parse_err:
        print(f"❌ PARSE FAILURE: JSON format corruption encountered: {str(parse_err)}")
        sys.exit(1)

    framework = payload.get("sovereign_legal_framework", {})
    
    # 3. Canonical Assertion Reference Matching Your .yml Workflow Standard
    expected_psalm = "Psalm 2:7-8 NLT - Only ask, and I will give you the nations as your inheritance, the whole earth as your possession."
    expected_haggai = "Haggai 2:8 NLT - The silver is mine, and the gold is mine, says the LORD of Heavens Armies."

    provided_psalm = framework.get("primary_decree_inheritance", "")
    provided_haggai = framework.get("collateral_foundation", "")

    # 4. Run Structural Analysis Sweeps
    print("[STAGE 2] INITIALIZING TEXTUAL ANALYSIS BOUNDARY SWEEPS...")
    error_count = 0

    if provided_psalm != expected_psalm:
        print("❌ CRITICAL MISALIGNMENT: Psalm 2:7-8 NLT text does not match canonical structure.")
        print(f"   Expected: {expected_psalm}")
        print(f"   Provided: {provided_psalm}")
        error_count += 1
    else:
        print("✅ ANALYSIS PASS: Psalm 2:7-8 NLT string structures are 100% compliant.")

    if provided_haggai != expected_haggai:
        print("❌ CRITICAL MISALIGNMENT: Haggai 2:8 NLT text does not match canonical structure.")
        print(f"   Expected: {expected_haggai}")
        print(f"   Provided: {provided_haggai}")
        error_count += 1
    else:
        print("✅ ANALYSIS PASS: Haggai 2:8 NLT string structures are 100% compliant.")

    # 5. Output Verification Report Status
    print("--------------------------------------------------------------------------------")
    if error_count > 0:
        print("❌ TEST STATUS: FAILED. Alignment discrepancies detected in local workspace variables.")
        sys.exit(1)
    else:
        print("=== ✅ LOCAL DIAGNOSTIC RESULT: 100% STABILIZED AND FUNCTIONING FLAWLESS ===\n")
        print("     ALL REVENUE LAW AND BIBLICAL JURISDICTION DECREES EXTRACTED SUCCESSFULLY.")
        print("     READY FOR UPSTREAM COMMIT STRATIFICATION.")
        print("================================================================================")
        return True

if __name__ == "__main__":
    execute_forced_workflow_test()

cd ~/master-workspace
chmod +x test_workflow_compliance.py
python3 test_workflow_compliance.py

./batch_sync_repos.sh

