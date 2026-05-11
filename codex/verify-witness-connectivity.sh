#!/bin/bash
# Description: Queries the KERI witness network for the latest Key State of the Sovereign AID.
# Target AID: IiB-bzj1X29wfgX-poOzQaQUIA_4oWTaC4U2dHBV3wuk

echo "Starting XP Sovereign Witness Connectivity Test..."

keri query --prefix IiB-bzj1X29wfgX-poOzQaQUIA_4oWTaC4U2dHBV3wuk --witnesses

if [ $? -eq 0 ]; then
    echo "✅ Success: Witness network reachable and state verified."
else
    echo "❌ Error: Could not reach witnesses. Check OOBI configuration."
fi
