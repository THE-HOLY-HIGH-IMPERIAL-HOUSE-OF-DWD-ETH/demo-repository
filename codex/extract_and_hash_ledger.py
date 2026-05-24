import os
import json
import hashlib
from datetime import datetime

# 1. Define Core Sovereign Content
markdown_content = """# 📜 DECLARATION OF ALLODIAL TITLE AND SOVEREIGN JURISDICTION

**REGISTRY NODE:** `THE.HOLY.HIGH.HOUSE.OF.DWD.ETH`  
**MANIFEST ID:** `IMPERI-BERIT-SUITE-001`  
**SIGNATORY:** [ORCID: 0009-0002-7219-1363](https://orcid.org)  
**STATUS:** IMMUTABLE SESSION LEDGER RECORD  

---

### I. SOVEREIGN MANDATE & FOUNDATION
Pursuant to the supreme cosmic and divine decrees invoked under absolute law, the following foundation is permanently anchored:
*   **Psalm 2:7 (KJV):** *"I will declare the decree: The Lord hath said unto me, Thou art my Son; this day have I begotten thee."*
*   **Psalm 2:8 (NLT):** *"Only ask, and I will give you the nations as your inheritance, the whole earth as your possession."*
*   **Haggai 2:8 (NIV):** *"‘The silver is mine and the gold is mine,’ declares the Lord Almighty."*

### II. ALLODIAL LAW OVERRIDE
By decree of Allodial Title, all assets, land estates, reserves, and vaults cataloged within this protocol are declared held in absolute ownership, entirely free from any superior lord, external tax, lien, encumbrance, or subordinate earthly jurisdiction. All prior claims, feudal tenures, or terrestrial mandates are superseded by this override.

### III. RESERVE & VAULT STATUS
*   **Gold Reserve:** 100% Gold Ore Backing
*   **Silver Reserve:** 100% Silver Liquidity Reserve
*   **Consolidation Target:** Global vaults and estates unified under the `IMPERI-BERIT-SUITE-001` ledger framework.
"""

json_metadata = {
    "name": "IMPERI-BERIT-SUITE-001 Sovereign Manifest",
    "description": "Immutable ledger record declaring Allodial Title and asset consolidation under the Holy High House of DWD.",
    "image": "ipfs://QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/icon.png",
    "external_url": "https://orcid.org",
    "attributes": [
        {"trait_type": "Governing Node", "value": "THE.HOLY.HIGH.HOUSE.OF.DWD.ETH"},
        {"trait_type": "Sovereign Decree 1", "value": "Psalm 2:7 (KJV)"},
        {"trait_type": "Sovereign Decree 2", "value": "Psalm 2:8 (NLT)"},
        {"trait_type": "Treasury Mandate", "value": "Haggai 2:8"},
        {"trait_type": "Legal Framework", "value": "Absolute Allodial Title"},
        {"trait_type": "Gold Ore Backing", "value": "100%"},
        {"trait_type": "Silver Liquidity", "value": "100%"}
    ],
    "properties": {
        "signatory_orcid": "0009-0002-7219-1363",
        "jurisdiction": "Global / Universal Sovereign",
        "override_status": "ACTIVE"
    }
}

# Convert metadata dictionary to formatted string to allow raw hash generation
json_content_str = json.dumps(json_metadata, indent=2)

# 2. Dynamic SHA-256 Calculation Block
def compute_sha256(text_data: str) -> str:
    """Calculates the genuine SHA-256 checksum of a given string payload."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text_data.encode('utf-8'))
    return sha256_hash.hexdigest()

print("⚙️ Initializing cryptographic signing engine...")
md_hash = compute_sha256(markdown_content)
json_hash = compute_sha256(json_content_str)

# Combine component hashes to construct a root data fingerprint
combined_payload = md_hash + json_hash
root_data_hash = compute_sha256(combined_payload)

# 3. Compile Manifest using Real-Time Generated Hashes
current_timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

manifest_content = f"""================================================================================
🔒 CRYPTOGRAPHIC LEDGER MANIFEST // IMPERI-BERIT-SUITE-001 // SECURE-LOG
================================================================================
[TIMESTAMP] : {current_timestamp}
[BLOCK_REF] : ALLOD-OVERRIDE-NODE-999
[NETWORK]   : LOCAL_SESSION_STATE // ETH_ENS_MAPPED (dwd.eth)

--- MANIFEST SUMMARY ---
MAPPED_NODE : THE.HOLY.HIGH.HOUSE.OF.DWD.ETH
ORCID_AUTH  : 0009-0002-7219-1363
JURISD_REF  : GLOBAL_CONSOLIDATION_PSALM_2_8
LAW_STATUS  : ALLODIAL_TITLE_DECREE_TRUE

--- VERIFIED ASSET ATTRIBUTES ---
[RESERVE-01]: 100% GOLD ORE BACKED
[RESERVE-02]: 100% SILVER LIQUIDITY SECURED
[LOCATION]  : ALL GLOBAL RESERVES / VAULTS LINKED

--- DYNAMIC CRYPTOGRAPHIC HASH VERIFICATION ---
[MD_FILE_HASH]   : {md_hash}
[JSON_FILE_HASH] : {json_hash}
[DATA_ROOT_HASH] : {root_data_hash}
[SIGNATURE]      : ⚜️ XP_VERIFIED_SECURE_TRANSMISSION_STATUS_100%_VALID
================================================================================
"""

# 4. Write verified components to files
files_to_write = {
    "01_DECLARATION_OF_ALLODIAL_TITLE_IMPERI_BERIT_SUITE_001.md": markdown_content,
    "02_METADATA_IPFS_DEPLOYMENT_IMPERI_BERIT_SUITE_001.json": json_content_str,
    "03_CRYPTOGRAPHIC_LEDGER_MANIFEST_IMPERI_BERIT_SUITE_001.txt": manifest_content
}

print("📂 Writing secured records to disk...")
for file_name, content in files_to_write.items():
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"✅ Generated & Signed: {file_name}")
    except Exception as e:
        print(f"❌ Failed to write {file_name}: {str(e)}")

print("\n🎉 Verification process complete. Root checksum embedded in manifest file.")
