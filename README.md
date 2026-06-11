# Automated Multi-Site Biometric Data Synchronization System

[cite_start]A Python-based API automation middleware solution designed to bridge decentralized data silos, eliminate manual administrative retrieval, and unify user access logs from distributed distributed Access Control Systems (Suprema BioStar 2)[cite: 24, 25, 26].

---

## 📋 Project Overview

[cite_start]In traditional multi-site enterprise networks, security and attendance data often remain trapped in isolated local networks[cite: 30, 31]. [cite_start]Generating a centralized report typically requires HR administrators to manually remote log into individual servers across different regions, export local CSV logs, and merge them in Excel[cite: 32, 33, 34, 35, 36, 37]. [cite_start]This operational pattern is time-consuming, prone to human error, and lacks real-time visibility[cite: 38].

[cite_start]This project eliminates that friction by engineering a centralized, lightweight Python middleware script[cite: 40, 41]. [cite_start]Operating as an intelligent agent, the script programmatically authenticates with multiple isolated servers via HTTPS REST APIs, context-switches across regional endpoints, aggregates user data, and centralizes records into a single structured JSON repository (`global_hr_data.json`)[cite: 27, 44, 45, 46, 47].

> [cite_start]**🚀 Key Impact:** Reduced the administrative data retrieval workload by **100%**, transforming a 30-minute manual process into a **5-second automated synchronization**[cite: 48].

---

## 🏗️ System Architecture & Data Flow

[cite_start]The project layout simulates a distributed corporate topology consisting of isolated virtual endpoints representing separate geographic regions[cite: 25, 66]:

* [cite_start]**Zone A (Head Office / Sri Lanka):** Hosted on a local virtual environment[cite: 67, 84].
* [cite_start]**Zone B (USA Branch):** Hosted on a remote server clone[cite: 68, 77].
* [cite_start]**Zone C (UK Branch):** Representing additional international branch infrastructure[cite: 83].


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
* [cite_start]**Local Biometrics:** High-risk data (fingerprint/biometric templates) stays entirely local to the regional site servers to respect local compliance restrictions[cite: 79].
* [cite_start]**Centralized Logs:** Only strictly necessary, non-identifiable time-in/time-out logs are extracted and pushed to the central synchronization environment[cite: 76, 79].

---

## 🛠️ Technical Stack

* [cite_start]**Virtualization & Infrastructure:** Oracle VirtualBox [cite: 50]
* [cite_start]**Operating System Environment:** Windows Server 2022 (64-bit) [cite: 51]
* [cite_start]**Access Control Platform:** Suprema BioStar 2 (Web-based Access Control) [cite: 52]
* [cite_start]**Scripting & Automation Engine:** Python 3 (Core libraries used: `requests`, `json`, `urllib3`) [cite: 53]
* [cite_start]**Data Layer Format:** JSON (JavaScript Object Notation) [cite: 55]
* [cite_start]**Networking Infrastructure:** Bridged Adapter configuration, static IP management, and custom local firewall rules[cite: 54].

---

## 🚀 Core Features Demonstrated

* [cite_start]**Automated REST API Authentication:** Handles programmatic HTTPS authorization payloads to communicate securely with third-party application platforms, bypassing self-signed SSL token barriers during execution[cite: 328, 352].
* [cite_start]**Dynamic Context Switching:** Iterates dynamically through an array of production server IPs to authenticate and query user states sequentially without cross-database links or complex VPN overlays[cite: 41, 376, 377, 395].
* [cite_start]**Data Consolidation & Parsing:** Normalizes distributed JSON payloads and unifies them into a globally accessible, clean analytics-ready file[cite: 47, 441].
* [cite_start]**DevOps Scalability:** Built on clean architectural practices; new regional office branches can be integrated into the synchronization stream instantly by appending new IP markers to the script matrix[cite: 473].

```
