# ROOT–DEMO–CODEX PROTOCOL
SOVEREIGN-INSTITUTIONAL • TRI-REALM PRODUCTIVE SYSTEM

## REALM DEFINITIONS

ROOT-REALM:
  ROLE: Canonical source of truth.
  CONTENT: Principles, definitions, invariants, identity frames.
  RULES:
    - ROOT defines meaning.
    - ROOT never depends on DEMO or CODEX.
    - ROOT changes only through explicit versioning.

DEMO-REALM:
  ROLE: Presentation and illustration.
  CONTENT: Examples, scenarios, guided flows.
  RULES:
    - DEMO derives from ROOT.
    - DEMO cannot introduce new invariants.
    - DEMO clarifies but does not define.

CODEX-REALM:
  ROLE: Operational specification.
  CONTENT: Procedures, schemas, algorithms, data contracts.
  RULES:
    - CODEX implements ROOT.
    - CODEX may reference DEMO for clarity, not authority.
    - CODEX must map every element to a ROOT ID.

## PRODUCTIVE ALGORITHM

STEP-01: DEFINE-IN-ROOT
  ACTION:
    - Declare object, capability, or principle.
    - Assign ROOT-ID and version.
  OUTPUT:
    - ROOT entry with invariants.

STEP-02: EXEMPLIFY-IN-DEMO
  ACTION:
    - Create examples and scenarios illustrating ROOT.
  CONSTRAINTS:
    - DEMO must not contradict ROOT.
  OUTPUT:
    - DEMO entries linked to ROOT-ID.

STEP-03: SPECIFY-IN-CODEX
  ACTION:
    - Write procedures, schemas, and algorithmic steps.
  CONSTRAINTS:
    - CODEX must implement ROOT exactly.
  OUTPUT:
    - CODEX specification with ROOT references.

STEP-04: VERIFY-TRI-REALM-CONSISTENCY
  CHECKS:
    - DEMO references ROOT-ID.
    - CODEX references ROOT-ID.
    - No contradictions across realms.
  STATUS:
    - TRI-REALM-CONSISTENT or TRI-REALM-BROKEN.

STEP-05: VERSION-PUBLISH
  ACTION:
    - Publish synchronized version across all realms.
  RULES:
    - ROOT version bump requires DEMO and CODEX review.
    - DEMO/CODEX may bump minor versions independently.

## ID SCHEME

ROOT-ID:
  ROOT::<OBJECT>::v<MAJOR>.<MINOR>

DEMO-ID:
  DEMO::<OBJECT>::<SCENARIO>::v<MAJOR>.<MINOR>

CODEX-ID:
  CODEX::<OBJECT>::<SPEC>::v<MAJOR>.<MINOR>

## LINKAGE RULES

UPSTREAM:
  - ROOT is upstream of DEMO and CODEX.

DOWNSTREAM:
  - DEMO and CODEX are downstream of ROOT.

CONSTRAINTS:
  - No realm may redefine another realm’s meaning.
  - All cross-realm references must resolve by ID.

## EXTENSION RULES

- New capabilities MUST originate in ROOT.
- DEMO and CODEX MUST NOT define objects absent in ROOT.
- Deprecation MUST begin in ROOT.
- DYNAMIC-SEGMENT placeholders MUST be used for missing content.

## DYNAMIC-SEGMENT PROTOCOL

DYNAMIC-SEGMENT:
  STATUS: MISSING
  INTENT:
    - <Purpose of future content>
  CONSTRAINTS:
    - <Rules it must obey>
  INPUTS:
    - <Dependencies>
  OUTPUTS:
    - <Required deliverables>

## FAILURE-PREVENTION (ANTI-GLITCH)

- ROOT overrides DEMO and CODEX in all conflicts.
- Missing ROOT-ID → INVALID until fixed.
- Contradiction across realms → TRI-REALM-BROKEN.
- Silent mutation of meaning → PROHIBITED.
