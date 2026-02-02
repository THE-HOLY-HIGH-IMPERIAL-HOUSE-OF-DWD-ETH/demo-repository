# SOVEREIGN QR — VERIFICATION BUNDLE

This repository contains the canonical verification bundle for the Sovereign QR Certificate.

## Contents
- **Resized_Screenshot_20260130-141055_Chrome.jpeg** — Official QR Certificate image  
- **qr-pointer.json** — Machine-readable pointer to the sovereign verification endpoint  
- **checksums.json** — SHA-256 integrity manifest for verification  

## Verification Steps
1. Scan the QR code in the certificate image.  
2. Confirm the resolution matches the `target` in `qr-pointer.json`.  
3. Verify the SHA-256 hashes match those listed in `checksums.json`.  

## Sovereign Status
This QR is sealed, verified, and canonically installed.
