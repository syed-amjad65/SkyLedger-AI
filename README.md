![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/syed-amjad65/SkyLedger-AI?style=social)
![GitHub forks](https://img.shields.io/github/forks/syed-amjad65/SkyLedger-AI?style=social)

<p align="center">
  <img src="assets/logo.png" alt="SkyLedger AI Logo" width="200"/>
</p>

# SkyLedger‑AI

## Overview
SkyLedger‑AI is a dual‑domain analytics and optimization framework designed to power airline commercial performance and digital analytics precision. It blends forecasting, inventory optimization, event tracking validation, and ledger‑style transparency to drive data‑driven decisions across routes, seats, and customer journeys.

---

## 📊 Data Dictionary

- **Flights:** flight_no, date, route, aircraft_type, seats, managed_capacity  
- **DemandSignals:** dpd, bookings, daily_intakes, cancellations, no_show_rate  
- **Revenue:** forecast_revenue, yield, rask, lf_target, class_mix  
- **Influences:** event_type, route, start_date, end_date, influence_weight, notes  
- **OverbookingSettings:** seats, bookings, no_show_rate, safety_buffer, overbooking_level, decrement_rate, risk_flag  
- **InventoryControl:** class_code, action_type, reason, dpd_band, min_yield, expiry_dpd, owner  
- **GroupsPolicy:** route, season, target_ratio, holdback_seats, accepted_groups, review_date  
- **PDDCorrections:** actual_show_up, actual_no_show, denied_boarding, correction_notes  
- **AlertsLog:** alert_type, root_cause, action_taken, owner, next_review  

---

## ⚡ Data Quick Start

Sample datasets are in `data/` and kept ≤100 rows for fast testing.

1. Open Power BI or Access → Import `data/*.csv`.  
2. Use `excel/OverbookingCalculator.xlsx` to compute initial settings → save results back into `data/overbooking_settings.csv`.  
3. Explore dashboards in `powerbi/SkyLedger.pbix` for monitoring, capacity, inventory, and groups mix.  

---

## 🔄 CSV → Access database pipeline

SkyLedger‑AI includes a reusable pipeline to load airline datasets from CSV into a Microsoft Access `.accdb` database using `pyodbc`.

- **Database file:** `access/SkyLedger.accdb` (tracked via Git LFS)  
- **Loader script:** `scripts/import_to_access.py`  
- **Source files:** `data/*.csv`  
- **Schema:** Detailed in `docs/data_dictionary.md`  

### How to run the import

1. Install the **Microsoft Access Database Engine 2016** driver.  
2. Update the connection string in:

```text
scripts/import_to_access.py
Run the loader:

bash
python scripts/import_to_access.py
Expected result:

All CSVs load into Access tables

Logs saved in logs/access_import.log

🧪 Excel templates quick test
These templates let you prove inventory and capacity logic without heavy tooling.

Download: excel/OverbookingCalculator.xlsx

Download: excel/CapacityScenarios.xlsx

OverbookingCalculator.xlsx
Inputs: seats, bookings, no_show_rate, safety_buffer Outputs: overbooking_level, decrement_rate, risk_flag

How to test:

Enter values in row 2:

seats = 296

bookings = 290

no_show_rate = 0.06

safety_buffer = 6

Confirm:

overbooking_level ≈ 24

decrement_rate = 3

risk_flag = Overheating

Use cases: a) Protect against oversell b) Tune decrement levels c) Flag overheating/stalling early

CapacityScenarios.xlsx
Inputs: route, aircraft_type (dropdown), frequency (dropdown) Outputs: expected_LF_delta, expected_yield_delta

How to test:

Pick:

aircraft_type = B789

frequency = 7

route = RUH‑LHR

Confirm:

expected_LF_delta = +0.05

expected_yield_delta = +0.01

Use cases: a) Up-/down-gauge trade-offs b) Frequency tuning c) Combined LF/yield impact

Templates are kept simple on purpose for recruiter evaluation. The logic mirrors the CSVs in data/ and the visuals in powerbi/SkyLedger.pbix.
Owner details and experience
Owner: Syed Muhammad Amjad

Role: Senior Data Scientist, Digital Analytics Insights Manager, and Inventory Optimization Leader

Experience: 25+ years across aviation, healthcare, pharma, and supply chain

Focus: Transforming legacy decision processes into AI‑driven, automated, and transparent systems; packaging recruiter‑ready projects with clear documentation and reproducible workflows

What SkyLedger‑AI demonstrates
Airline inventory optimization: EMSR‑b seat allocation, demand forecasting, overbooking strategy simulation

Revenue KPIs visibility: RASK, yield, load factor dashboards and spill/spoil trade‑off visualization

Digital analytics validation: Event capture checks, funnel analysis, anomaly detection, campaign effectiveness

APIs: FastAPI endpoints for /health, /forecast, /inventory, /anomaly

Automation: GitHub Actions for daily runs and consistent outputs

Transparency: Ledger‑style logs to audit decisions and data quality

Tiny API quickstart
Health check endpoint
Method: GET

Path: /health

Response:

json
{ "status": "ok" }
Local run
bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Open: http://127.0.0.1:8000/health

🧭 Getting started
Create and activate a virtual environment (Windows)
bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

🚀 Usage Examples
Once the server is running:

bash
uvicorn app.main:app --reload
Forecast
bash
curl http://127.0.0.1:8000/forecast
Inventory
bash
curl http://127.0.0.1:8000/inventory
Anomaly Detection
bash
curl http://127.0.0.1:8000/anomaly

📁 Project structure
text
SkyLedger-AI/
├─ app/                # FastAPI app and routers (health, forecast, inventory, anomaly)
├─ access/             # Access .accdb database and related assets (LFS-tracked)
├─ scripts/            # CSV→Access ODBC loader and helper scripts
├─ data/               # Sample airline datasets (≤100 rows each for fast testing)
├─ docs/               # Data dictionary and design notes
├─ logs/               # Ledger-style audit logs and run history
├─ assets/             # SkyLedger-AI logo and visual assets
├─ tests/              # Basic tests for API and services
├─ .github/workflows/  # CI workflows for daily runs and artifacts
├─ README.md           # Main documentation
├─ requirements.txt    # Python dependencies
└─ LICENSE.txt         # MIT license
Notes
Keep paths ASCII-safe (no spaces, no Unicode).

Run locally with:

bash
uvicorn app.main:app --reload
Explore docs:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

License
Type: MIT License

Usage: You may use, modify, and distribute this project with attribution

Details: See the LICENSE file in the repository

Contact
Name: Syed Muhammad Amjad

Email: syedemirates2021@gmail.com

WhatsApp: +92 335 2177766

LinkedIn: https://www.linkedin.com/in/syed-amjad-9b513570

GitHub: https://github.com/syed-amjad65