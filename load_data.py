import pandas as pd


def load_data():

    df_csv = pd.read_csv("raw_data/student_coffee_crisis.csv")
    print("=== CSV Data ===")
    print(df_csv.head())

    df_json = pd.read_json("raw_data/student_coffee_crisis.json")
    print("\n=== JSON Data ===")
    print(df_json.head())

    df_excel = pd.read_excel("raw_data/student_coffee_crisis.xlsx")
    print("\n=== Excel Data ===")
    print(df_excel.head())

    df_parquet = pd.read_parquet(
    "raw_data/student_coffee_crisis.parquet",
    engine="pyarrow"
    )
    print("\n=== Parquet Data ===")
    print(df_parquet.head())
    print("\nLoading Info Parquet file...")
    print(df_parquet.info())

if __name__ == "__main__":
    load_data()    