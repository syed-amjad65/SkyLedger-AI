![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/syed-amjad65/SkyLedger-AI?style=social)
![GitHub forks](https://img.shields.io/github/forks/syed-amjad65/SkyLedger-AI?style=social)
<p align="center">
  <img src="assets/logo.png" alt="SkyLedger AI Logo" width="200"/>
</p>

# SkyLedger AI


## Overview
SkyLedger‑AI is a dual‑domain analytics and optimization framework designed to power airline commercial performance and digital analytics precision. It blends forecasting, inventory optimization, event tracking validation, and ledger‑style transparency to drive data‑driven decisions across routes, seats, and customer journeys.

## Owner details and experience
- **Owner:** Syed Muhammad Amjad
- **Role:** Senior Data Scientist, Digital Analytics Insights Manager, and Inventory Optimization Leader
- **Experience:** 25+ years across aviation, healthcare, pharma, and supply chain
- **Focus:** Transforming legacy decision processes into AI‑driven, automated, and transparent systems; packaging recruiter‑ready projects with clear documentation and reproducible workflows

## What SkyLedger‑AI demonstrates
- **Airline inventory optimization:** EMSR‑b seat allocation, demand forecasting, overbooking strategy simulation
- **Revenue KPIs visibility:** RASK, yield, load factor dashboards and spill/spoil trade‑off visualization
- **Digital analytics validation:** Event capture checks, funnel analysis, anomaly detection, campaign effectiveness
- **APIs:** FastAPI endpoints for `/health`, `/forecast`, `/inventory`, `/anomaly` (extensible)
- **Automation:** GitHub Actions for daily runs and consistent outputs
- **Transparency:** Ledger‑style logs to audit decisions and data quality

## Tiny API quickstart
- **Health check endpoint:**
  - **Method:** GET
  - **Path:** `/health`
  - **Response:**
    ```json
    { "status": "ok" }
    ```
- **Local run:**
  - **Install:** `pip install -r requirements.txt`
  - **Start:** `uvicorn app.main:app --reload`
  - **Open:** `http://127.0.0.1:8000/health`

## 🧭 Getting started

### Create and activate a virtual environment (Windows)
```bash
python -m venv .venv
.\.venv\Scripts\activate

## 🚀 Usage Examples

Once the server is running with:

```bash
uvicorn app.main:app --reload

### Forecast
```bash
curl http://127.0.0.1:8000/forecast
{
  "route": "DXB-LHR",
  "forecasted_demand": [120, 135, 150, 160],
  "method": "EMSR-b"
}
curl http://127.0.0.1:8000/inventory
{
  "route": "DXB-LHR",
  "total_seats": 180,
  "allocated": {"economy": 120, "business": 50, "first": 10},
  "overbooking_strategy": "5% buffer"
}
curl http://127.0.0.1:8000/anomaly
{
  "campaign": "WinterSale2025",
  "events_checked": 1000,
  "anomalies_detected": 3,
  "flags": ["missing_conversion", "duplicate_event", "timestamp_gap"]
}
## 📁 Project Structure

SkyLedger-AI/
├─ app/
│  ├─ __init__.py
│  └─ main.py          # FastAPI app with /health and /hello endpoints
├─ .venv/              # Local virtual environment (optional, not committed)
├─ README.md           # Usage examples and docs
├─ requirements.txt    # Python dependencies
├─ .gitignore          # Excludes .venv, __pycache__, etc.
└─ LICENSE.txt         # License information

### Notes
- Keep paths ASCII-safe (no spaces, no Unicode) for clean imports and tooling.
- Run locally with:
```bash
uvicorn app.main:app --reload
- Explore docs at:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## License
- **Type:** MIT License
- **Usage:** You may use, modify, and distribute this project with attribution
- **Details:** See the LICENSE file in the repository

## Contact
- **Name:** Syed Muhammad Amjad
- **Email:** syedemirates2021@gmail.com
- **WhatsApp:** +92 335 2177766
- **LinkedIn:** www.linkedin.com/in/syed-amjad-9b513570
- **GitHub:** github.com/syed-amjad65
