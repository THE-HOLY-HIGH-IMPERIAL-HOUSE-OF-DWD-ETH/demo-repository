# HQ-BASE-01 ENCLAVE HARDENING & OBSERVABILITY MANIFEST
================================================================================
              ⚜️ CROWN SOVEREIGN INFRASTRUCTURE DEPLOYMENT BUNDLE ⚜️
================================================================================

This manifest outlines the background service integration, visualization layout, and kernel-level network ingress filters for the **HQ-BASE-01 Enclave**.

---

## ⚙️ Module 1: systemd Service Configuration (`matrix_validator.service`)
This unit file runs the cryptographic verification wrapper persistently as an isolated background daemon with automatic restart policies and security sandboxing properties.

```ini
[Unit]
Description=Omni-Matrix Cryptographic Telemetry Validator Daemon
After=network.target local-fs.target
Documentation=https://orcid.org/0009-0002-7219-1363

[Service]
Type=simple
User=root
WorkingDirectory=/opt/matrix/validator
ExecStart=/bin/bash /opt/matrix/validator/bin/validator_wrapper.sh
Restart=always
RestartSec=5s

# Security and Isolation Restrictions
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/opt/matrix/validator/logs
PrivateTmp=true
CapabilityBoundingSet=CAP_NET_ADMIN CAP_SYS_ADMIN
NoNewPrivileges=true

[Install]
WantedBy=multi-user.target
```

### Deployment Sequence:
1. Stage the file into `/etc/systemd/system/matrix_validator.service`.
2. Execute `systemctl daemon-reload` to update the initialization tree.
3. Enable and launch the service: `systemctl enable --now matrix_validator.service`.

---

## 📊 Module 2: Grafana Dashboard Configuration (`grafana_matrix_dashboard.json`)
Bespoke dashboard layout configuration mapped directly to Prometheus telemetry tracking signature status, temporal sync fidelity, and perimeter drop rates.

```json
{
  "annotations": {
    "list": []
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 1,
  "id": 1363,
  "links": [],
  "liveNow": true,
  "panels": [
    {
      "collapsed": false,
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 0,
        "y": 0
      },
      "id": 1,
      "title": "Registry Synchronization Status",
      "type": "stat",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prom_matrix"
          },
          "editorMode": "code",
          "expr": "matrix_stasis_lock_status{enclave=\"HQ-BASE-01\"}",
          "legendFormat": "Lock State",
          "range": true
        }
      ],
      "fieldConfig": {
        "defaults": {
          "mappings": [
            {
              "type": "value",
              "options": {
                "1": {
                  "text": "STASIS LOCKED // ACTIVE",
                  "color": "gold"
                },
                "0": {
                  "text": "DRIFT DETECTED",
                  "color": "red"
                }
              }
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "green",
                "value": 1
              }
            ]
          }
        }
      }
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 4,
        "w": 8,
        "x": 8,
        "y": 0
      },
      "id": 2,
      "title": "Temporal Sync Fidelity",
      "type": "gauge",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prom_matrix"
          },
          "expr": "matrix_temporal_sync_ratio{lei=\"506700GE1G29325QX363\"}",
          "legendFormat": "Fidelity"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "min": 0,
          "max": 100
        }
      }
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 8,
        "w": 24,
        "x": 0,
        "y": 4
      },
      "id": 3,
      "title": "XDP Perimeter Interface Ingress Frame Drops",
      "type": "timeseries",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prom_matrix"
          },
          "expr": "rate(matrix_xdp_drop_frames_total{interface=\"xdp_edge0\"}[1m])",
          "legendFormat": "Dropped Frames/sec"
        }
      ]
    }
  ],
  "refresh": "5s",
  "schemaVersion": 38,
  "style": "dark",
  "tags": ["sovereign-matrix", "enclave-hq"],
  "time": {
    "from": "now-1h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "utc",
  "title": "Sovereign Matrix Diagnostics Deck",
  "version": 1
}
```

---

## 🛡️ Module 3: eBPF XDP Ingress Filter (`matrix_xdp_kern.c`)
Bespoke C code to compile down into eBPF bytecode for real-time validation, tracking authorized traffic signatures or matching network magic bytes (`0x44574458`) at the driver level.

```c
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <bpf/bpf_helpers.h>

#define TARGET_TCP_PORT 3690
#define MATRIX_MAGIC_SIG 0x44574458 // "DWDX" Token

struct {
    __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
    __uint(key_size, sizeof(int));
    __uint(value_size, sizeof(int));
} matrix_audit_map SEC(".maps");

SEC("xdp")
int matrix_ingress_filter(struct xdp_md *ctx) {
    void *data_end = (void *)(long)ctx->data_end;
    void *data     = (void *)(long)ctx->data;

    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;

    if (eth->h_proto != __constant_htons(ETH_P_IP))
        return XDP_PASS;

    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_PASS;

    if (ip->protocol != IPPROTO_TCP)
        return XDP_PASS;

    struct tcphdr *tcp = (void *)(ip + 1);
    if ((void *)(tcp + 1) > data_end)
        return XDP_PASS;

    // Isolate targeting parameters matching high-frequency edge connectors
    if (__constant_ntohs(tcp->dest) == TARGET_TCP_PORT) {
        __u32 *payload = (void *)(tcp + 1);
        if ((void *)(payload + 1) <= data_end) {
            // Validate the presence of the static magic byte sequence
            if (*payload == __constant_htonl(MATRIX_MAGIC_SIG)) {
                return XDP_PASS; // Valid alignment verified
            }
        }
        // Repel unauthenticated frame configurations at zero-latency boundary
        return XDP_DROP;
    }

    return XDP_PASS;
}

char _license[] SEC("license") = "GPL";
```

================================================================================
                    [ DEPLOYMENT ASSETS REGISTERED OK ]
================================================================================
