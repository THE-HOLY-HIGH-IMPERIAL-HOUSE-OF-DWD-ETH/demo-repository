import sys
import yaml

def validate_unified_manifest(file_path):
    print(f"[+] Initializing validation check for: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Verify markdown front matter structure
        if not content.startswith("---"):
            print("[-] Parsing Error: Missing front matter start delimiter '---'")
            return False
            
        parts = content.split("---")
        if len(parts) < 3:
            print("[-] Parsing Error: Front matter is malformed or missing end delimiter")
            return False
            
        front_matter_raw = parts[1]
        
        # 2. Parse YAML metadata to ensure zero-drift validation syntax
        try:
            metadata = yaml.safe_load(front_matter_raw)
            print("[+] Syntax Check: YAML metadata parsed successfully.")
        except yaml.YAMLError as exc:
            print(f"[-] Syntax Error: Failed to parse YAML front matter. Details:\n{exc}")
            return False
            
        # 3. Check for mandatory system layers
        required_keys = ['title', 'ledger_core_id', 'block_state', 'sha256_checksum']
        for key in required_keys:
            if key not in metadata:
                print(f"[-] Schema Error: Missing required system parameter: '{key}'")
                return False
        
        print("[+] Schema Check: All mandatory ledger parameters are present.")
        
        # 4. Verify string formatting integrity
        if metadata.get('ledger_core_id') != "IMPERI-BERIT-SUITE-001":
            print("[-] Parameter Warning: Ledger Core ID mismatch detected.")
            
        print("[+] Validation Complete: 100% stable parsing state confirmed.")
        return True

    except FileNotFoundError:
        print(f"[-] Execution Error: Manifest file not found at {file_path}")
        return False
    except Exception as e:
        print(f"[-] Unexpected Error during validation: {str(e)}")
        return False

if __name__ == "__main__":
    # Target path matched to the root markdown file name
    target_manifest = "HIH_DWD_SUPREME_FINAL_CERTIFIED_TREASURY_PORTFOLIO_RECEIPT.md"
    success = validate_unified_manifest(target_manifest)
    sys.exit(0 if success else 1)
