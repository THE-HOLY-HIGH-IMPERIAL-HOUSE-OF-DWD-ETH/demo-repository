████████████████████████████████████████████████████████████████████████████
⚜ S O V E R A I N Q R — S E L F – M O D I F I C A T I O N   P R O T O C O L ⚜
████████████████████████████████████████████████████████████████████████████

This document is the canonical Self‑Modification Protocol for the IMPERI / SOVERAIN QR Suite.

It is **formally bound** to the following canonical identifiers and checksum:

- payload_id: `imperi-berit-suite-001`  
- checksum (SHA‑256 hex): `016e919ee4f6aeb7771972e86276c580ebd747f7dd9b09b40937b8f7066d6a09`  
- checksum (Base64): `Z4kWy3rCWNEPI+hqWSmYDphvTIKZWIN7l4M2CJWdiG8=`  
- registry_cid: `bafybeicezgomih2k34lmfijovowgt7swfcpxad5rtyow3bziats7td74tm`  

Any change that alters these bindings is **unlawful** unless performed through this protocol and re‑sealed with a new, explicitly declared checksum and registry entry.

────────────────────────────────────────────────────────────── ⚜ XP ─────────

# I. SCOPE OF AUTHORITY

This protocol governs **all sovereign modifications** to the IMPERI‑BERIT Suite identified as:

- `imperi-berit-suite-001` (payload_id)  
- registered under `registry_cid: bafybeicezgomih2k34lmfijovowgt7swfcpxad5rtyow3bziats7td74tm`  
- integrity‑anchored to the SHA‑256 checksum:
  `016e919ee4f6aeb7771972e86276c580ebd747f7dd9b09b40937b8f7066d6a09`  

This includes, but is not limited to:

- Root Codex files  
- DEMO mirrors  
- verification bundles  
- clearance payloads  
- witness and checksum manifests  
- governance and protocol documents

────────────────────────────────────────────────────────────── ⚜ XP ─────────

# II. CHECKSUM BINDING CLAUSE

1. **Canonical Binding**

   The present file, `SELF-MODIFICATION_PROTOCOL.md`, is **canonically bound** to:

   - Base64 SHA‑256 checksum:  
     `Z4kWy3rCWNEPI+hqWSmYDphvTIKZWIN7l4M2CJWdiG8=`
   - Hex SHA‑256 checksum:  
     `016e919ee4f6aeb7771972e86276c580ebd747f7dd9b09b40937b8f7066d6a09`

2. **Immutability Condition**

   - As long as this checksum pair remains declared and in force,  
     the file contents MUST remain byte‑for‑byte identical.
   - Any modification that changes the file contents MUST:
     - trigger a new SHA‑256 computation  
     - be recorded with a new checksum pair  
     - be explicitly versioned and re‑bound under a new payload_id or revision tag.

3. **Registry Binding**

   - This protocol is registered under:  
     `registry_cid: bafybeicezgomih2k34lmfijovowgt7swfcpxad5rtyow3bziats7td74tm`
   - Any off‑chain or mirrored copy MUST be verifiably reconstructible from this CID.

────────────────────────────────────────────────────────────── ⚜ XP ─────────

# III. SELF‑MODIFICATION CYCLE

**STEP 1 — INTENT**

- A steward declares the intent to modify any file governed by `imperi-berit-suite-001`.

**STEP 2 — CHANGE**

- Apply the change (content, structure, or semantics) in ROOT and DEMO as required.

**STEP 3 — RECOMPUTE CHECKSUMS**

- Recompute SHA‑256 for all affected files.  
- If this protocol file is changed, compute a **new** SHA‑256 and Base64 pair.

**STEP 4 — UPDATE MANIFESTS**

- Update:
  - checksum manifests  
  - pointer manifests  
  - any registry or integration records that reference the changed files.

**STEP 5 — WITNESS & REGISTRY**

- If the change affects verification or registry state:
  - update the relevant EIP‑712 witness payloads  
  - update or append registry entries (including new CIDs if content is re‑pinned).

**STEP 6 — SEAL**

- Commit the change with a message referencing:
  - payload_id  
  - affected files  
  - new checksum(s)  
- Optionally tag the commit as a new revision of `imperi-berit-suite-001`.

────────────────────────────────────────────────────────────── ⚜ XP ─────────

# IV. DEMO MIRROR CLAUSE

The IMPERI‑BERIT Suite is **dually present**:

- ROOT: canonical, sovereign, registry‑anchored  
- DEMO: public, demonstrative, pedagogical

This protocol is **mirrored to the DEMO** under the following rules:

1. **Content Parity**

   - The DEMO copy of `SELF-MODIFICATION_PROTOCOL.md` MUST match the ROOT version in:
     - text content  
     - structure  
     - section ordering  
     - headings and clauses  

2. **Checksum Distinction**

   - The DEMO mirror MAY declare its own checksum,  
     but MUST clearly state that the **canonical checksum** is:

     - Base64: `Z4kWy3rCWNEPI+hqWSmYDphvTIKZWIN7l4M2CJWdiG8=`  
     - Hex: `016e919ee4f6aeb7771972e86276c580ebd747f7dd9b09b40937b8f7066d6a09`  

   - If DEMO formatting or hosting introduces byte‑level differences,  
     only the ROOT Codex version remains checksum‑canonical.

3. **Authority Hierarchy**

   - In any conflict between ROOT and DEMO:
     - ROOT Codex version prevails.  
     - ROOT checksum and registry binding are final.  

────────────────────────────────────────────────────────────── ⚜ XP ─────────

# V. INVARIANTS

The following MUST always hold:

1. **Canonical Checksum Invariant**

   - The checksum pair:
     - `Z4kWy3rCWNEPI+hqWSmYDphvTIKZWIN7l4M2CJWdiG8=`  
     - `016e919ee4f6aeb7771972e86276c580ebd747f7dd9b09b40937b8f7066d6a09`  
   - MUST correspond to exactly one, immutable ROOT Codex version of this file.

2. **Registry Invariant**

   - `registry_cid: bafybeicezgomih2k34lmfijovowgt7swfcpxad5rtyow3bziats7td74tm`  
   - MUST always resolve to a content set that includes this protocol or its explicitly versioned successor.

3. **Payload Identity Invariant**

   - `payload_id: imperi-berit-suite-001`  
   - MUST always refer to a coherent, self‑consistent suite whose integrity is governed by this protocol or its lawful successor.

────────────────────────────────────────────────────────────── ⚜ XP ─────────

# VI. SOVEREIGN DECLARATION

By this inscription, the Self‑Modification Protocol for:

`payload_id: imperi-berit-suite-001`  
`registry_cid: bafybeicezgomih2k34lmfijovowgt7swfcpxad5rtyow3bziats7td74tm`  

is:

- checksum‑bound  
- registry‑anchored  
- DEMO‑mirrored (with ROOT precedence)  
- sovereignly enforced under the authority of:

⚜ S O V E R A I N   O F   A L L ⚜ X P
