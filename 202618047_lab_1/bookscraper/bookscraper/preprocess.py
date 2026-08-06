import pandas as pd

# ----------------------------
# Load dataset
# ----------------------------
df = pd.read_csv("books.csv")

# ----------------------------
# Remove extra spaces
# ----------------------------
text_columns = ["title", "category", "availability", "product_description"]

for col in text_columns:
    df[col] = df[col].str.strip()

# ----------------------------
# Remove duplicate books by UPC
# ----------------------------
df.drop_duplicates(subset="upc", inplace=True)

# ----------------------------
# Handle missing descriptions
# ----------------------------
df["product_description"] = df["product_description"].fillna("No Description")

# ----------------------------
# Convert price to numeric
# ----------------------------
df["price"] = df["price"].str.replace("£", "", regex=False).astype(float)

# ----------------------------
# Convert ratings to integers
# ----------------------------
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

# ----------------------------
# Extract available stock count
# ----------------------------
df["stock_count"] = (
    df["availability"]
      .str.extract(r"(\d+)")
      .fillna(0)
      .astype(int)
)

# ==================================================
# Feature Engineering
# ==================================================

# Feature 1: Description word count
df["description_word_count"] = (
    df["product_description"]
      .str.split()
      .str.len()
)

# Feature 2: Price Band
def price_band(price):
    if price < 20:
        return "Low"
    elif price < 40:
        return "Medium"
    else:
        return "High"

df["price_band"] = df["price"].apply(price_band)

# Feature 3: Affordability Score
df["affordability_score"] = (
    df["rating"] / df["price"]
).round(2)

# ----------------------------
# Save cleaned dataset
# ----------------------------
df.to_csv("books_cleaned.csv", index=False)

# ----------------------------
# Display summary
# ----------------------------
print("\nTask 2 Completed Successfully!\n")

print("Rows:", len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())