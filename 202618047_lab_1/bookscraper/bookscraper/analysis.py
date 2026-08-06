import pandas as pd

# Read the scraped CSV file
df = pd.read_csv("books.csv")

# Total records
print("Total Records:", len(df))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate UPC values
print("\nDuplicate UPCs:")
print(df["upc"].duplicated().sum())

