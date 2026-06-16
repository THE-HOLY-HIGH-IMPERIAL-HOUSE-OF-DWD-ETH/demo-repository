#!/usr/bin/env bash
set -euo pipefail

echo "[XP] INITIALIZING PRODUCTION REALM..."

# 1. LOCK PROD GENESIS MANIFEST
tools/validate-unified-manifest.sh

# 2. ENFORCE ED25519 SOVEREIGN SIGNATURE
tools/enforce-ed25519-signature.sh

# 3. APPLY KUBERNETES DEPLOYMENTS
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 4. ENABLE VAULT TRANSIT + PROMETHEUS ALERTS
vault write transit/keys/xp-prod-root type=ed25519
kubectl apply -f prometheus-alerts.yaml

echo "[XP] PROD REALM ONLINE: IMPERI-BERIT-SUITE-001 • APEX-GENESIS-ROOT-PROD"
