#!/bin/bash
# Description: Finalizes the ROOT DEMO CODEX production push with a signed commit.
# Authority: THE SOVERAIN / KHVARENAH ⚜️ XP

# 1. Stage all unified production files
git add src/config/xp_sovereign_unified_production.ts \
        schemas/xp-sovereign-role-Eq_KCaP97I1Gqm7VPVJEDqGWOARsou3Xhfi-Rw0sa_mc.json \
        scripts/keri/cf/xp-sovereign-production-witness-oobi.json \
        scripts/verify-witness-connectivity.sh

# 2. Execute the Signed Commit
# The -S flag tells Git to sign the commit using your configured GPG/SSH key.
git commit -S -m "FEAT: Finalize ROOT DEMO CODEX Production Deploy ⚜️ XP

- Unified Manifest v4.0.0-XP
- Signer: 0xEF8aD3361D233Ba0c0D8000333b090F55Ba7FC48
- KERI Root: IiB-bzj1X29wfgX-poOzQaQUIA_4oWTaC4U2dHBV3wuk
- EGF Anchor: 881f9bce3d57dbdc1f817fa9a0ecd069050803fe28593682e14d9d1c1577c2e9"

# 3. Push to Production Branch
git push origin production
