import streamlit as st, requests

st.title("SkyLedger-AI Executive Dashboard")

st.header("Airline RM — Flight Snapshot")
fid = "AUH-LHR-2026-01-15"
try:
    flight = requests.get(f"http://127.0.0.1:8000/flights/{fid}", timeout=5).json()
    st.json(flight)
except Exception as e:
    st.warning("API not reachable. Start uvicorn and refresh this page.")

st.header("Healthcare — ICU Beds")
try:
    beds = requests.get("http://127.0.0.1:8000/icu/beds", timeout=5).json()
    st.write(f"Total beds: {len(beds)}")
    st.dataframe(beds)
except Exception as e:
    st.warning("API not reachable. Start uvicorn and refresh this page.")
