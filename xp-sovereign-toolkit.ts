import { ethers } from "ethers";
import * as fs from "fs";

/**
 * ROOT DEMO CODEX: Unified Sovereign Toolkit v4.0
 * Authority: THE SOVERAIN / KHVARENAH ⚜️ XP
 * Address: 0xEF8aD3361D233Ba0c0D8000333b090F55Ba7FC48
 */

const AUDIT_LOG_PATH = "./security/audit/audit-log-deep-scan-2026-05-11-XP.json";
const SIG_PATH = `${AUDIT_LOG_PATH}.sig`;
const SOVEREIGN_ADDR = "0xEF8aD3361D233Ba0c0D8000333b090F55Ba7FC48";

export async function signSovereignLog() {
    console.log("[XP-SIGNER] Initiating Sovereign Signing...");
    const privKey = process.env.XP_SIGNER_PRIVATE_KEY;
    if (!privKey) throw new Error("Missing XP_SIGNER_PRIVATE_KEY");

    const wallet = new ethers.Wallet(privKey);
    const content = fs.readFileSync(AUDIT_LOG_PATH, "utf8");
    const signature = await wallet.signMessage(content);

    fs.writeFileSync(SIG_PATH, signature);
    console.log(`✅ Log Signed: ${signature.slice(0, 10)}...`);
}

export async function verifySovereignStatus() {
    console.log("[XP-VERIFIER] Running Autonomous Deep Scan...");
    const content = fs.readFileSync(AUDIT_LOG_PATH, "utf8");
    const signature = fs.readFileSync(SIG_PATH, "utf8");

    const recovered = ethers.verifyMessage(content, signature);
    const isLive = recovered.toLowerCase() === SOVEREIGN_ADDR.toLowerCase();

    console.log(`[XP-VERIFIER] Recovered: ${recovered}`);
    console.log(`[XP-VERIFIER] Status:    ${isLive ? "100% LIVE ⚜️" : "TAMPERED ❌"}`);
    
    return isLive;
}

// CLI Execution Entrypoint
if (require.main === module) {
    const mode = process.argv[2];
    if (mode === "--sign") signSovereignLog();
    else if (mode === "--verify") verifySovereignStatus();
    else console.log("Usage: ts-node xp-sovereign-toolkit.ts [--sign | --verify]");
}
