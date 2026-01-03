import pandas as pd

def load_feedback(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def classify_nps(score: int) -> str:
    if score >= 9:
        return "Promoter"
    elif score >= 7:
        return "Passive"
    return "Detractor"

def add_nps_segment(df: pd.DataFrame) -> pd.DataFrame:
    df["nps_segment"] = df["nps_score"].apply(classify_nps)
    return df

def compute_nps(df: pd.DataFrame) -> float:
    promoters = (df["nps_segment"] == "Promoter").mean()
    detractors = (df["nps_segment"] == "Detractor").mean()
    return round((promoters - detractors) * 100, 2)

def tag_theme(comment: str) -> str:
    text = str(comment).lower()
    if any(w in text for w in ["delay", "late", "wait"]):
        return "Timeliness"
    if any(w in text for w in ["app", "website", "crash", "bug"]):
        return "Digital Experience"
    if any(w in text for w in ["staff", "agent", "nurse", "doctor"]):
        return "Staff Interaction"
    if any(w in text for w in ["price", "expensive", "cheap"]):
        return "Pricing"
    if any(w in text for w in ["delivery", "package", "damage"]):
        return "Delivery Experience"
    return "Other"

def add_theme(df: pd.DataFrame) -> pd.DataFrame:
    df["theme"] = df["comment"].apply(tag_theme)
    return df

def main():
    print("\nChoose dataset to analyze:")
    print("1. Sample CX Data")
    print("2. Airline CX Data")
    print("3. Ecommerce CX Data")
    print("4. Healthcare CX Data")
    print("5. Logistics CX Data")
    print("6. Retail CX Data")
    print("7. Pharma CX Data")
    print("8. Oil & Gas CX Data")

    choice = input("\nEnter choice (1-8): ")

    if choice == "1":
        path = "cx_analytics/data/cx_feedback_sample.csv"
    elif choice == "2":
        path = "cx_analytics/data/cx_airline_feedback.csv"
    elif choice == "3":
        path = "cx_analytics/data/cx_ecommerce_feedback.csv"
    elif choice == "4":
        path = "cx_analytics/data/cx_healthcare_feedback.csv"
    elif choice == "5":
        path = "cx_analytics/data/cx_logistics_feedback.csv"
    elif choice == "6":
        path = "cx_analytics/data/cx_retail_feedback.csv"
    elif choice == "7":
        path = "cx_analytics/data/cx_pharma_feedback.csv"
    elif choice == "8":
        path = "cx_analytics/data/cx_oilandgas_feedback.csv"
    else:
        print("Invalid choice")
        return

    df = load_feedback(path)
    df = add_nps_segment(df)
    df = add_theme(df)

    print(f"\n=== Dataset Path: {path} ===")
    print("\n=== Overall NPS ===")
    print(compute_nps(df))

    print("\n=== NPS by Industry ===")
    print(df.groupby("industry")["nps_segment"].apply(
        lambda x: compute_nps(df[df["industry"] == x.name])
    ))

    print("\n=== Theme Counts ===")
    print(df["theme"].value_counts())


    choice = input("\nEnter choice (1-4): ")

    if choice == "1":
        path = "cx_analytics/data/cx_feedback_sample.csv"
    elif choice == "2":
        path = "cx_analytics/data/cx_airline_feedback.csv"
    elif choice == "3":
        path = "cx_analytics/data/cx_ecommerce_feedback.csv"
    elif choice == "4":
        path = "cx_analytics/data/cx_healthcare_feedback.csv"
    else:
        print("Invalid choice")
        return

    df = load_feedback(path)
    df = add_nps_segment(df)
    df = add_theme(df)

    print("\n=== Overall NPS ===")
    print(compute_nps(df))

    print("\n=== NPS by Industry ===")
    print(df.groupby("industry")["nps_segment"].apply(lambda x: compute_nps(df[df["industry"] == x.name])))

    print("\n=== Theme Counts ===")
    print(df["theme"].value_counts())


    print("\n=== Overall NPS ===")
    print(compute_nps(df))

    print("\n=== NPS by Industry ===")
    print(df.groupby("industry")["nps_segment"].apply(lambda x: compute_nps(df[df["industry"] == x.name])))

    print("\n=== Theme Counts ===")
    print(df["theme"].value_counts())

if __name__ == "__main__":
    main()
