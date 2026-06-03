pragma circom 2.1.6;

include "node_modules/circomlib/circuits/poseidon.circom";

template XpSovereignVerifier() {
    // --- PRIVATE INPUTS ---
    signal input secretKey;
    signal input leiMarkerNumeric;
    signal input crestIntegrityValue; // Must equal 100

    // --- PUBLIC INPUTS ---
    signal input expectedCrestIntegrity;
    signal input rootIdentityCommitment;

    // --- OUTPUTS ---
    signal output isValidSovereign;

    // 1. Enforce that Crest Integrity is exactly 100%
    crestIntegrityValue === expectedCrestIntegrity;

    // 2. Generate deterministic cryptographic commitment
    component hasher = Poseidon(2);
    hasher.inputs[0] <== secretKey;
    hasher.inputs[1] <== leiMarkerNumeric;

    // 3. Verify commitment matches the public network state
    hasher.out === rootIdentityCommitment;

    // 4. Output validation flag
    isValidSovereign <== 1;
}

component main {public [expectedCrestIntegrity, rootIdentityCommitment]} = XpSovereignVerifier();
