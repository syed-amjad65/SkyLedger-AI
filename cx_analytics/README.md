# SkyLedger‑AI — CX Analytics Module

The **CX Analytics** module provides multi‑industry customer experience insights using NPS (Net Promoter Score), VoC (Voice of Customer) feedback, and automated theme tagging.  
It is designed to demonstrate real‑world CX analytics capability across aviation, logistics, retail, healthcare, ecommerce, pharma, and oil & gas.

---

## ✅ Key Features

- **NPS Segmentation**  
  Automatically classifies customers into Promoters, Passives, and Detractors.

- **Industry‑Aligned Theme Tagging**  
  Tags comments into themes such as Timeliness, Digital Experience, Staff Interaction, Delivery Experience, Pricing, and more.

- **Multi‑Dataset Support**  
  Choose from multiple industries using a simple menu in the script.

- **Cross‑Industry CX Benchmarking**  
  Compare NPS and theme patterns across industries.

---

## ✅ Supported Industries

This module includes ready‑to‑use datasets for:

- Airline  
- Ecommerce  
- Healthcare  
- Logistics  
- Retail  
- Pharma  
- Oil & Gas  
- (Plus a small sample dataset for testing)

Each dataset contains realistic CX feedback with:
- Touchpoints  
- Channels  
- NPS scores  
- Customer comments  
- Timestamps  

---

## ✅ Folder Structure

cx_analytics/ ├─ data/ # All CX datasets (multi‑industry) ├─ scripts/ # Python scripts for NPS + VoC analysis ├─ notebooks/ # Optional Jupyter notebooks ├─ models/ # Optional ML models (sentiment, topics) └─ README.md # Module documentation

Code

---

## ✅ How to Run the CX Analytics Script

From the project root:

```bat
python cx_analytics\scripts\nps_voc_analysis.py
You will see a menu:

Code
Choose dataset to analyze:
1. Sample CX Data
2. Airline CX Data
3. Ecommerce CX Data
4. Healthcare CX Data
5. Logistics CX Data
6. Retail CX Data
7. Pharma CX Data
8. Oil & Gas CX Data
Enter a number (1–8) to run analysis for that industry.

✅ Output Includes
Overall NPS

NPS by industry

Theme counts

Automatically tagged themes

Clean, readable console output

✅ Business Value
This module demonstrates:

How CX analytics works in real operations

How NPS and VoC can be automated

How multi‑industry datasets can be analyzed with one engine

How to build scalable analytics modules for aviation, logistics, retail, healthcare, and more