const canonize = require('rdf-canonize');
const crypto = require('crypto');
const fs = require('fs');

async function verifyPayload(filePath, expectedCid) {
  try {
    // 1. Load the Verifiable Credential
    const vc = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    // 2. RDFC-1.0 Canonicalization
    // RDFC-1.0 is the primary algorithm for normalizing RDF datasets
    const canonical = await canonize.canonize(vc, {
      algorithm: 'RDFC-1.0'
    });

    // 3. SHA-256 Hashing
    // Verification depends on hashing the canonicalized form
    const hash = crypto.createHash('sha256').update(canonical).digest('hex');

    console.log(`Computed Hash: ${hash}`);
    
    // 4. Integrity Check
    if (hash === expectedCid || expectedCid.includes(hash)) {
      console.log("✅ INTEGRITY VERIFIED: Zero Variance Detected.");
      process.exit(0);
    } else {
      console.error("❌ INTEGRITY FAILURE: CID Master Root Mismatch.");
      process.exit(1);
    }
  } catch (error) {
    console.error(`Verification Error: ${error.message}`);
    process.exit(1);
  }
}

// Execution from CLI
const args = process.argv.slice(2);
verifyPayload(args[1], args[0]);
