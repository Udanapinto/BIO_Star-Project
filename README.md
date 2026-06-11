# Automated Multi-Site Biometric Data Synchronization System

A Python-based API automation middleware solution designed to bridge decentralized data silos, eliminate manual administrative retrieval, and unify user access logs from distributed distributed Access Control Systems (Suprema BioStar 2)[cite: 24, 25, 26].

---

## 📋 Project Overview

In traditional multi-site enterprise networks, security and attendance data often remain trapped in isolated local networks. Generating a centralized report typically requires HR administrators to manually remote log into individual servers across different regions, export local CSV logs, and merge them in Excel. This operational pattern is time-consuming, prone to human error, and lacks real-time visibility.

This project eliminates that friction by engineering a centralized, lightweight Python middleware script. Operating as an intelligent agent, the script programmatically authenticates with multiple isolated servers via HTTPS REST APIs, context-switches across regional endpoints, aggregates user data, and centralizes records into a single structured JSON repository (`global_hr_data.json`).

> **🚀 Key Impact:** Reduced the administrative data retrieval workload by **100%**, transforming a 30-minute manual process into a **5-second automated synchronization**.

---

## 🏗️ System Architecture & Data Flow

The project layout simulates a distributed corporate topology consisting of isolated virtual endpoints representing separate geographic regions:

* **Zone A (Head Office / Sri Lanka):** Hosted on a local virtual environment.
* **Zone B (USA Branch):** Hosted on a remote server clone.
* **Zone C (UK Branch):** Representing additional international branch infrastructure.


```

[ USA Branch ]                [ UK Branch ]
(Zone B: Local Server)        (Zone C: Local Server)
│                              │
└──────────────┐┌──────────────┘
(API Sync via Python Middleware)
▼
[ Central HR Database ]
(Centralized JSON Repository)
▲
│
[ Head Office: Sri Lanka ]
(Zone A: Local Server)

```

### 🔒 Privacy & Data Compliance Architecture
* **Local Biometrics:** High-risk data (fingerprint/biometric templates) stays entirely local to the regional site servers to respect local compliance restrictions.
* **Centralized Logs:** Only strictly necessary, non-identifiable time-in/time-out logs are extracted and pushed to the central synchronization environment.

---

## 🛠️ Technical Stack

* **Virtualization & Infrastructure:** Oracle VirtualBox 
* **Operating System Environment:** Windows Server 2022 (64-bit) 
* **Access Control Platform:** Suprema BioStar 2 (Web-based Access Control) 
* **Scripting & Automation Engine:** Python 3 (Core libraries used: `requests`, `json`, `urllib3`) 
* **Data Layer Format:** JSON (JavaScript Object Notation) 
* **Networking Infrastructure:** Bridged Adapter configuration, static IP management, and custom local firewall rules

---

## 🚀 Core Features Demonstrated

* **Automated REST API Authentication:** Handles programmatic HTTPS authorization payloads to communicate securely with third-party application platforms, bypassing self-signed SSL token barriers during execution.
* **Dynamic Context Switching:** Iterates dynamically through an array of production server IPs to authenticate and query user states sequentially without cross-database links or complex VPN overlays.
* **Data Consolidation & Parsing:** Normalizes distributed JSON payloads and unifies them into a globally accessible, clean analytics-ready file.
* **DevOps Scalability:** Built on clean architectural practices; new regional office branches can be integrated into the synchronization stream instantly by appending new IP markers to the script matrix.

```
