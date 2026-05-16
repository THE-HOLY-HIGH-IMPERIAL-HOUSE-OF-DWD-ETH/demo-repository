#!/usr/bin/env bash
# ==============================================================================
# ARCHITECTURE DEPLOYMENT SCRIPT: IMPERIAL-WE / SOVEREIGN SYSTEM
# GOVERNANCE COMPONENT: CODEX & DEMO SANDBOX PIPELINE ROUTING
# ==============================================================================

set -euo pipefail

# 1. Define targeted directory structure paths
PROJECT_ROOT=$(pwd)
ROOT_DIR="${PROJECT_ROOT}/root"
DEMO_DIR="${PROJECT_ROOT}/demo-sandbox"
CODEX_DIR="${DEMO_DIR}/codex"
RUNTIME_DIR="${DEMO_DIR}/runtime"

echo "⚜️  Initializing Sovereign Sandbox Environment Setup..."

# 2. Programmatically generate the target directory nodes
mkdir -p "${ROOT_DIR}"
mkdir -p "${CODEX_DIR}"
mkdir -p "${RUNTIME_DIR}"

# 3. Create the Codex Schema Reference File (sovereign-context.jsonld)
cat << 'EOF' > "${CODEX_DIR}/sovereign-context.jsonld"
{
  "@context": [
    "https://w3.org",
    "https://schema.org",
    "https://github.com"
  ],
  "type": ["VerifiablePresentation", "CombinedTransactionPresentation"],
  "id": "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "verifiableCredential": [
    {
      "comment": "PART 1: THE INSTITUTIONAL SOVEREIGN IDENTITY (vLEI Root)",
      "type": ["VerifiableCredential", "LegalEntityOfficialCredential"],
      "issuer": "did:vlei:gleif:984500c58a9e71d30834",
      "credentialSubject": {
        "id": "did:xp:imperial-we:0x71C00000000000000000000000000000000003a9",
        "legalEntity": {
          "lei": "984500C58A9E71D30834",
          "name": "Imperial Sovereign Trust"
        },
        "officialRole": "Sovereign Signatory",
        "clearanceLevel": "Alpha-XP",
        "externalAnchor": "https://orcid.org"
      }
    }
  ]
}
EOF

# 4. Create the Live Runtime Target File (combined-transaction-presentation.min.json)
# This file is strictly minified (no spaces or comments) for QR matrix deployment
cat << 'EOF' > "${RUNTIME_DIR}/combined-transaction-presentation.min.json"
{"@context":["https://w3.org","https://schema.org","https://github.com"],"type":["VerifiablePresentation","CombinedTransactionPresentation"],"id":"urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6","verifiableCredential":[{"type":["VerifiableCredential","LegalEntityOfficialCredential"],"issuer":"did:vlei:gleif:984500c58a9e71d30834","credentialSubject":{"id":"did:xp:imperial-we:0x71C00000000000000000000000000000000003a9","legalEntity":{"lei":"984500C58A9E71D30834","name":"Imperial Sovereign Trust"},"officialRole":"Sovereign Signatory","clearanceLevel":"Alpha-XP","externalAnchor":"https://orcid.org"},"proof":{"type":"Ed25519Signature2020","verificationMethod":"did:vlei:gleif:984500c58a9e71d30834#key-1","proofValue":"z6MkmPlaceholderSignatureValueXyZ"}}],"paymentClearance":{"transactionId":"tx_9081273918237","currency":"XP-RESERVE-USD","amount":"14500.00","sourceWallet":"did:xp:imperial-we:0xEF8aD3361D233Ba0c0D8000333b090F55Ba7FC48","destinationMerchant":"did:merchant:fbo-luxury-terminal:0x3b1000000000000000000000000000000000081c","paymentMechanism":{"type":"CryptographicCovenantSettlement","networkRoot":"xp.reserve","clearingChannel":"Atomic-Instant-Gross-Settlement"},"expiresAt":"2026-05-16T10:57:00Z"},"proof":{"type":"JsonWebSignature2020","created":"2026-05-16T10:55:00Z","verificationMethod":"did:xp:imperial-we:0xEF8aD3361D233Ba0c0D8000333b090F55Ba7FC48#master-key","proofPurpose":"assertionMethod","challenge":"merchant_nonce_891237","jws":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.MockMasterSignatureString"}}
EOF

# 5. Execute filesystem verification checks
echo "--------------------------------------------------"
echo "Checking deployed tree structure:"
if command -v tree &> /dev/null; then
    tree "${PROJECT_ROOT}/demo-sandbox"
else
    ls -R "${PROJECT_ROOT}/demo-sandbox"
fi

echo "--------------------------------------------------"
echo "Checking payload syntax integrity:"
if command -v jq &> /dev/null; then
    jq '.' "${RUNTIME_DIR}/combined-transaction-presentation.min.json" > /dev/null
    echo "✅ Success: Runtime JSON presentation structure is valid."
else
    echo "⚠️  Warning: 'jq' tool not found. Skipping validation check."
fi
echo "⚜️  Deployment loop complete. Sandbox environments are armed."


# Make the deployment automation script executable
chmod +x deploy-sandbox.sh

# Run the routing protocol script
./deploy-sandbox.sh


# Start an instantaneous local HTTP server routing out your workspace configuration files
python3 -m http.server 8080

