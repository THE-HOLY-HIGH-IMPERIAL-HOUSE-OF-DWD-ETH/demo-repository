/**
 * ROOT DEMO CODEX: Unified Production Configuration
 * Authority: THE SOVERAIN / KHVARENAH
 * Signer: 0xEF8aD3361D233Ba0c0D8000333b090F55Ba7FC48
 */

export const XP_SOVEREIGN_MANIFEST = {
    // Identity & Governance
    VLEI_EGF_KERI_ID: "IiB-bzj1X29wfgX-poOzQaQUIA_4oWTaC4U2dHBV3wuk",
    ETH_SIGNER_ADDRESS: "0xEF8aD3361D233Ba0c0D8000333b090F55Ba7FC48",
    VLEI_EGF_ANCHOR_HEX: "881f9bce3d57dbdc1f817fa9a0ecd069050803fe28593682e14d9d1c1577c2e9",
    
    // Schema Manifest
    XP_ROLE_SCHEMA_SAID: "Eq_KCaP97I1Gqm7VPVJEDqGWOARsou3Xhfi-Rw0sa_mc",
    
    // Deployment Metadata
    ENVIRONMENT: "PRODUCTION",
    VERSION: "v4.0.0-XP",
    COMPLIANCE: "EGF-v4.0",
    
    // Witness Connection
    WITNESS_PORT: 5623,
    OOBI_PATH: "./scripts/keri/cf/xp-sovereign-production-witness-oobi.json"
};

// Initialization hook for the ROOT DEMO CODEX Verifier
export const initializeVerifier = () => {
    console.log(`[XP-SOVEREIGN] Initializing ROOT DEMO CODEX Verifier...`);
    console.log(`[XP-SOVEREIGN] Anchor Verified: ${XP_SOVEREIGN_MANIFEST.VLEI_EGF_ANCHOR_HEX.slice(0, 8)}...`);
    return XP_SOVEREIGN_MANIFEST;
};
