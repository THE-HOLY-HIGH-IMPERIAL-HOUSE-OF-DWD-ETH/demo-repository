import { ethers } from "ethers";
import * as fs from "fs";

async function signLog() {
    // Load the audit log content
    const auditLogPath = "./security/audit/audit-log-deep-scan-2026-05-11-XP.json";
    const logContent = fs.readFileSync(auditLogPath, "utf8");

    // Replace with your private key (securely managed via env variables)
    const privateKey = process.env.XP_SIGNER_PRIVATE_KEY;
    const wallet = new ethers.Wallet(privateKey);

    // Generate the signature
    const signature = await wallet.signMessage(logContent);

    console.log(`XP Sovereign Signature: ${signature}`);
    
    // Save signature to a separate file for verification
    fs.writeFileSync(`${auditLogPath}.sig`, signature);
}

signLog();
