![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/syed-amjad65/SkyLedger-AI?style=social)
![GitHub forks](https://img.shields.io/github/forks/syed-amjad65/SkyLedger-AI?style=social)

<p align="center">
  <img src="assets/logo.png" alt="SkyLedger AI Logo" width="200"/>
</p>

# SkyLedger‑AI  
**Aviation Operations & Revenue Optimization Framework**

---

## Overview
SkyLedger-AI is a dual-domain analytics and optimization framework designed to power airline commercial performance and digital analytics precision. It blends forecasting, inventory optimization, event tracking validation, and ledger-style transparency to drive data-driven decisions across routes, seats, and customer journeys.

The framework provides an end-to-end solution for managing complex Revenue Management (RM) decisions and auditing data quality, directly aligning with key Aviation Operations Optimization (AOO) goals.

---

## 💡 Key Demonstrations (Why Recruiters Should Care)

This project showcases expertise in moving legacy decision processes into AI-driven, automated, and transparent systems.

- **Airline Inventory Optimization:** EMSR-b seat allocation, demand forecasting, overbooking strategy simulation  
- **Revenue KPIs Visibility:** RASK, yield, load factor, spill/spoil trade-off  
- **Digital Analytics Validation:** Event capture checks, funnel analysis, anomaly detection  
- **APIs & Scalability:** FastAPI endpoints (`/forecast`, `/inventory`, `/anomaly`)  
- **Automation & Auditing:** GitHub Actions + ledger-style logs for transparency  

---

## 📁 Project Structure

```text
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
ata Dictionary (Key Tables)
Domain	Entity	Key Fields	Purpose
Operations	Flights	flight_no, route, aircraft_type, seats, managed_capacity	Master data for flight parameters and capacity
Forecasting	DemandSignals	dpd, bookings, daily_intakes, cancellations, no_show_rate	Tracks real-time demand metrics by DPD
Commercial	Revenue	forecast_revenue, yield, rask, lf_target, class_mix	Core financial and performance metrics
Inventory	InventoryControl	class_code, action_type, dpd_band, min_yield, owner	Logs granular controls applied to seat availability
Risk	OverbookingSettings	no_show_rate, safety_buffer, overbooking_level, risk_flag	Dynamic overbooking strategy
Audit	AlertsLog	alert_type, root_cause, action_taken, owner, next_review	Ledger-style transparency
Sample datasets are available in data/ and kept ≤100 rows for fast testing.

⚡ Data Quick Start
1. Local Setup
bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
2. CSV → Access Database Pipeline (ODBC Integration)
SkyLedger-AI includes a reusable pipeline to load sample datasets from CSV into a Microsoft Access .accdb database using pyodbc.

Database file: access/SkyLedger.accdb

Loader script: scripts/import_to_access.py

How to run the import
Install the Microsoft Access Database Engine 2016 driver

Update the connection string in scripts/import_to_access.py

Run the loader:

bash
python scripts/import_to_access.py
Expected result:

All CSVs load into Access tables

Logs saved in logs/access_import.log

🧪 Excel Templates Quick Test (Logic Verification)
These templates let you prove inventory and capacity logic without heavy tooling.

1. OverbookingCalculator.xlsx
Focus: Risk Management & Dynamic Decrement Strategy

Inputs	Outputs
seats, bookings, no_show_rate, safety_buffer	overbooking_level, decrement_rate, risk_flag
Example Test:

seats = 296

bookings = 290

no_show_rate = 0.06

safety_buffer = 6

Confirm:

overbooking_level ≈ 24

decrement_rate = 3

risk_flag = Overheating

2. CapacityScenarios.xlsx
Focus: Fleet Planning & Commercial Trade-offs

Inputs	Outputs
route, aircraft_type (dropdown), frequency (dropdown)	expected_LF_delta, expected_yield_delta
Example Test (Simulated):

aircraft_type = B789

frequency = 7

route = RUH-LHR

Confirm:

expected_LF_delta = +0.05

expected_yield_delta = +0.01

🌐 Tiny API Quickstart (FastAPI)
Run the local server:

bash
uvicorn app.main:app --reload
Open Swagger UI: http://127.0.0.1:8000/docs

Health Check Endpoint
Attribute	Detail
Method	GET
Path	/health
Response	{"status": "ok"}
Usage Examples
bash
# Forecast Endpoint
curl http://127.0.0.1:8000/forecast

# Inventory Control Endpoint
curl http://127.0.0.1:8000/inventory

# Anomaly Detection Endpoint
curl http://127.0.0.1:8000/anomaly
Contact & Owner Details
This project was developed by Syed Muhammad Amjad, Senior Data Scientist, Digital Analytics Insights Manager, and Inventory Optimization Leader with 25+ years of experience across aviation, healthcare, pharma, and supply chain.

Detail	Contact Information
Name	Syed Muhammad Amjad
Email	syedemirates2021@gmail.com
WhatsApp	+92 335 2177766
LinkedIn	https://www.linkedin.com/in/syed-amjad-9b513570
GitHub	https://github.com/syed-amjad65
License
This project is released under the MIT License. You may use, modify, and distribute this project with attribution. See the LICENSE.txt file for full details.