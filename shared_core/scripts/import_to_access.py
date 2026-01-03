import pyodbc
import csv
from pathlib import Path

accdb_path = Path("access/SkyLedger.accdb").resolve()
conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={accdb_path};"
)
tables = {
    "Flights": "data/Flights.csv",
    "DemandSignals": "data/DemandSignals.csv",
    "Revenue": "data/Revenue.csv",
    "Influences": "data/Influences.csv",
    "OverbookingSettings": "data/OverbookingSettings.csv",
    "InventoryControl": "data/InventoryControl.csv",
    "GroupsPolicy": "data/GroupsPolicy.csv",
    "PDDCorrections": "data/PDDCorrections.csv",
    "AlertsLog": "data/AlertsLog.csv",
}

def main():
    with pyodbc.connect(conn_str, autocommit=True) as conn:
        cur = conn.cursor()
        for table, csv_path in tables.items():
            with open(csv_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                cols = reader.fieldnames
                placeholders = ", ".join(["?"] * len(cols))
                col_list = ", ".join(cols)
                insert_sql = f"INSERT INTO {table} ({col_list}) VALUES ({placeholders})"
                rows = [tuple(row[c] for c in cols) for row in reader]
                if rows:
                    cur.executemany(insert_sql, rows)
                    print(f"Inserted {len(rows)} rows into {table}")

if __name__ == "__main__":
    main()
