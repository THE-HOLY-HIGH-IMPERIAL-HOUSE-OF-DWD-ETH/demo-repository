████████████████████████████████████████████████████████████████████████████
⚜  C H E C K S U M – B O U N D   H E A D E R  —  D E M O  ⚜
This DEMO mirror reflects the canonical ROOT version.

Canonical identifiers (ROOT‑only):

• payload_id: imperi-berit-suite-001
• checksum (SHA‑256 hex): 016e919ee4f6aeb7771972e86276c580ebd747f7dd9b09b40937b8f7066d6a09
• checksum (Base64): Z4kWy3rCWNEPI+hqWSmYDphvTIKZWIN7l4M2CJWdiG8=
• registry_cid: bafybeicezgomih2k34lmfijovowgt7swfcpxad5rtyow3bziats7td74tm

This DEMO file is NOT checksum‑canonical.  
ROOT remains sovereign and authoritative.
████████████████████████████████████████████████████████████████████████████


████████████████████████████████████████████████████████████████████████████
⚜  S O V E R A I N   A U T O N O M O U S   R E S E R V E   L O O P  —  D E M O  ⚜
████████████████████████████████████████████████████████████████████████████

## SOVERAIN AUTONOMOUS RESERVE LOOP (DEMO MIRROR)

This DEMO version mirrors the ROOT protocol for public witness and demonstration.  
It does **not** carry checksum authority.  
ROOT remains sovereign and canonical.

---

## Autonomy Definition

Within this protocol, **autonomous and live** means:

1. The SOVERAIN QR payload is:
   - permanently bound to a reserve identity
   - continuously priced against GOLD and SILVER reference feeds
   - continuously attestable via registry and checksum anchors.

2. The RESERVE LOOP runs independently of:
   - any single bank
   - any single payment network
   - any single commercial platform

3. External systems (banks, institutions, commerce networks) **subscribe** to
   the SOVERAIN RESERVE LOOP; they do not define it.

---

## Loop Behavior

- On every QR session:
  - resolve RESERVE identity (GOLD/SILVER/IMPERI)
  - fetch latest reserve attestations and reference prices
  - emit a **SOVERAIN_RESERVE_STATE** event into the universal commerce feed.

**The QR is the pointer.  
The RESERVE is the substance.  
The LOOP is the autonomous, live covenant state.**

```json
{
  "stream_type": "soverain_universal_commerce",
  "event_id": "uuid-...",
  "source": "soverain_hub",
  "payload": {
    "qr_session_id": "uuid-...",
    "merchant_ref": "merchant-xyz",
    "amount": { "value": "125.00", "currency": "USD" },
    "bank_status": "SETTLED",
    "gold_reference": {
      "value_in_oz": "0.055",
      "spot_price_usd": "2275.00"
    },
    "reserves": {
      "coverage_ratio": "1.12",
      "reserve_pool_id": "gold-reserve-01"
    },
    "timestamps": {
      "created_utc": "...",
      "bank_settled_utc": "...",
      "last_update_utc": "..."
    }
  }
}
