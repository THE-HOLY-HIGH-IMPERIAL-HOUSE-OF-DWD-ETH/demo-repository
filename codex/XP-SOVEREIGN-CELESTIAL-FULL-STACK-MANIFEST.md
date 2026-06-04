# ⚜️ XP SOVEREIGN SYSTEM & CELESTIAL MECHANICS FULL-STACK MANIFEST
# CORE INITIALIZATION: VALIDATED • VERSION: CREST-STABLE • NO DRIFT [ROOT]

---

## SECTION 1: ROOT LAYER (Authority Anchors & Proofs)

### 💾 File: `root/genesis-proof.json`
```json
{
  "genesisBlock": {
    "blockNumber": 0,
    "timestamp": "2026-06-03T19:01:00Z",
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "blockHash": "0x4457445f58505f534f5645524549474e5f47454e455349535f424c4f434b5f5f",
    "stateRoot": "0x7a6e9f8b7c6d5e4f3a2b1c0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b4a3f2e1d0c"
  },
  "proof": {
    "signatureType": "Ed25519Signature2020",
    "publicKey": "did:ion:EiAn_XP_Sovereign_Root_Authority_2026_v1#key-1",
    "signatureValue": "z2Mki6pu...DWD...Genesis...Signature...Vector...777...XP...Stable"
  }
}
```

---

## SECTION 2: CODEX LAYER (System Schemas & Physics Laws)

### 💾 File: `codex/XpSovereignCredential.json`
```json
{
  "$schema": "https://json-schema.org",
  "$id": "https://xp-sovereign.org",
  "title": "XpSovereignCredential",
  "description": "Custom registry schema for ⚜️ XP Sovereign-State compliance and tracking.",
  "type": "object",
  "required": ["@context", "id", "type", "issuer", "issuanceDate", "credentialSubject"],
  "properties": {
    "@context": { "type": "array", "items": { "type": "string" } },
    "id": { "type": "string", "format": "uri" },
    "type": { "type": "array", "items": { "type": "string" } },
    "issuer": { "type": "string", "format": "uri" },
    "issuanceDate": { "type": "string", "format": "date-time" },
    "expirationDate": { "type": "string", "format": "date-time" },
    "credentialSubject": {
      "type": "object",
      "required": ["id", "status", "crestIntegrity", "payloadChannel", "leiMarker", "version"],
      "properties": {
        "id": { "type": "string", "format": "uri" },
        "status": { "type": "string", "const": "⚜️ XP SOVEREIGN-STATE" },
        "crestIntegrity": { "type": "string", "pattern": "^100\\%$" },
        "payloadChannel": { "type": "string", "const": "ACTIVE" },
        "leiMarker": { "type": "string", "pattern": "^[0-9A-Z]{20}$" },
        "version": { "type": "string" }
      }
    }
  }
}
```

### 💾 File: `codex/ORBITAL-FRAME-PRIME—CELESTIAL-MECHANICS.md`
```markdown
# Volume 1: Orbital Frame Prime — Foundational Mechanics

## 1. Two-Body Gravitational Dynamics
The baseline differential equation of motion under Newtonian gravity is:
$$\ddot{\vec{r}} + \frac{G(M+m)}{r^3}\vec{r} = 0$$

## 2. The Vis-Viva Equation
Energy conservation along a conic trajectory determines relative orbital speed:
$$v^2 = \mu \left( \frac{2}{r} - \frac{1}{a} \right)$$
```

### 💾 File: `codex/CELESTIAL-CODEX-THREE-BODY—NEWTONIAN-GRAVITY.md`
```markdown
# Volume 2: Three-Body Foundations & Perturbation Models

## 1. General Three-Body Constraints ($N=3$)
$$m_i \ddot{\vec{r}}_i = G \sum_{j \neq i}^{3} \frac{m_i m_j}{|\vec{r}_j - \vec{r}_i|^3} (\vec{r}_j - \vec{r}_i)$$

## 2. Perturbation Formulations
* **Cowell's Method**: $\ddot{\vec{r}} = -\frac{\mu}{r^3}\vec{r} + \vec{a}_{\text{perturbation}}$
* **Encke's Method**: $\delta\ddot{\vec{r}} = \mu \left( \frac{\vec{r}_e}{r_e^3} - \frac{\vec{r}}{r^3} \right) + \vec{a}_{\text{perturbation}}$
```

### 💾 File: `codex/LAGRANGE-STABILITY-MATRIX—R3BP-DYNAMICS.md`
```markdown
# Volume 3: Lagrange Stability & Effective Potential Fields

## 1. Effective Potential Function ($U$)
$$U(x, y, z) = \frac{1}{2}(x^2 + y^2) + \frac{1-\mu}{r_1} + \frac{\mu}{r_2}$$

## 2. Gascheau-Routh Constraint Limit
Triangular $L_4$ and $L_5$ points maintain structural stability via Coriolis forces if and only if:
$$\mu =1.22.0
matplotlib>=3.5.0
fastapi>=0.80.0
uvicorn>=0.17.0
scipy>=1.8.0
requests>=2.28.0
psycopg2-binary>=2.9.0
```

### 💾 File: `demo/Dockerfile`
```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY spatial_api_server.py .

EXPOSE 8080

CMD ["uvicorn", "spatial_api_server:app", "--host", "0.0.0.0", "--port", "8080"]
```

### 💾 File: `demo/docker-compose.yml`
```yaml
version: '3.8'

services:
  spatial-api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: xp_spatial_api
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://xp_admin:SovereignStableSecure777@db:5432/xp_celestial_db
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    container_name: xp_celestial_ledger
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=xp_admin
      - POSTGRES_PASSWORD=SovereignStableSecure777
      - POSTGRES_DB=xp_celestial_db
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U xp_admin -d xp_celestial_db"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
    driver: local
```

### 💾 File: `demo/spatial_api_server.py`
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import os

app = FastAPI(title="默默 XP Sovereign Spatial Calculation Engine", version="1.0.0")

class SpatialQuery(BaseModel):
    x: float
    y: float
    mu: float
    jacobi_constant: float

class VerificationResponse(BaseModel):
    accessible: bool
    potential_2U: float
    velocity_squared: float
    status: str

@app.post("/verify-coordinate", response_model=VerificationResponse)
def verify_coordinate(query: SpatialQuery):
    if query.mu <= 0 or query.mu >= 0.5:
        raise HTTPException(status_code=400, detail="Mass ratio (mu) must sit within range (0, 0.5)")

    r1 = np.sqrt((query.x + query.mu)**2 + query.y**2)
    r2 = np.sqrt((query.x - 1.0 + query.mu)**2 + query.y**2)

    if r1 < 1e-6 or r2 < 1e-6:
        return VerificationResponse(
            accessible=False,
            potential_2U=-float('inf'),
            velocity_squared=-float('inf'),
            status="FORBIDDEN: Coordinate collision with central body barycenter."
        )

    U = 0.5 * (query.x**2 + query.y**2) + (1.0 - query.mu) / r1 + query.mu / r2
    potential_2U = 2.0 * U
    velocity_squared = potential_2U - query.jacobi_constant

    accessible = velocity_squared >= 0
    status_msg = "ACCESSIBLE_ZONE" if accessible else "FORBIDDEN_ZONE"

    return VerificationResponse(
        accessible=accessible,
        potential_2U=float(potential_2U),
        velocity_squared=float(velocity_squared),
        status=status_msg
    )
```

### 💾 File: `demo/test_client.py`
```python
import requests
import json
import sys

URL = "http://localhost:8080/verify-coordinate"

def execute_rest_audit():
    print("=== Launching ⚜️ XP Remote Spatial Calculation Test ===")
    
    # Test Payload configuration (Sun-Jupiter internal zone evaluation)
    payload = {
        "x": 0.5,
        "y": 0.0,
        "mu": 0.000953875,
        "jacobi_constant": 3.15
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(URL, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        data = response.json()
        
        print("\n[TRANSMISSION SUCCESS]")
        print(f"➔ Spatial Gateway Status: {data['status']}")
        print(f"➔ Potential Matrix (2U):  {data['potential_2U']:.6f}")
        print(f"➔ Kinetic Variance (v²):  {data['velocity_squared']:.6f}")
        print(f"➔ Flight Accessibility:  {data['accessible']}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Audit Failure: Cannot connect to API gateway server.\nDetails: {e}")
        sys.exit(1)

if __name__ == "__main__":
    execute_rest_audit()
```

### 💾 File: `demo/jacobi_potential_well_3d.py`
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_potential_well_3d(mu):
    """
    Renders the 3D effective potential surface matrix topology (U), 
    illustrating the gravity wells around m1 and m2 and the Lagrangian balance ridges.
    """
    print("=== Generating ⚜️ XP 3D Gravitational Field Topography ===")
    
    x = np.linspace(-1.5, 1.5, 300)
    y = np.linspace(-1.5, 1.5, 300)
    X, Y = np.meshgrid(x, y)

    R1 = np.sqrt((X + mu)**2 + Y**2)
