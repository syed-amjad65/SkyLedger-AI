import csv, os
folder = "data"
for name in os.listdir(folder):
    if name.endswith(".csv"):
        with open(os.path.join(folder, name), newline="", encoding="utf-8") as f:
            rows = sum(1 for _ in csv.reader(f)) - 1  # minus header
        print(f"{name}: {rows} rows")
        assert rows <= 100, f"{name} exceeds 100 rows"
