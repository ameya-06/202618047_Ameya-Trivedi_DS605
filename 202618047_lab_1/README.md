# DS605 - Data scraping Assignment  
**Student Name:** Ameya Trivedi  
**Student ID:** 202618047  

---

## Assignment Title
**Book Scraper using Python and Scrapy**

---

##  Objective
The goal of this assignment is to build a complete data pipeline by:
1. Scraping book information using Python and Scrapy.
2. Cleaning and transforming the collected data.
3. Creating visualizations.
4. Reporting meaningful data-driven insights.

---

##  Dataset Scope
- Scraped at least **100 books** from **5 catalog pages** of [Books to Scrape](https://books.toscrape.com).
- Extracted fields:
  - Title  
  - Category  
  - Price  
  - Rating  
  - Availability  
  - Product Description  
  - UPC  
  - Number of Reviews  
  - Product URL  

---

##  Task 1 — Data Scraping
- Implemented a Scrapy spider (`books_spider.py`) that:
  - Follows pagination (limited to 5 pages).
  - Visits each book’s detail page.
  - Extracts all required fields.
- Exported raw records to **CSV** (`books.csv`).
- Reported:
  - Total records scraped.
  - Missing values.
  - Duplicate UPC values.

---

## Task 2 — Preprocessing and Cleaning
- Converted `price` column from string (`£51.77`) to numeric (`51.77`).
- Removed leading/trailing spaces in text fields.
- Handled missing values in `description`.
- Saved cleaned dataset as **books.cleaned.csv**.

---

##  Task 3 — Visualization and Analysis
Generated at least four meaningful plots:
1. **Price Distribution** → Histogram of book prices.  
2. **Rating Distribution** → Bar chart of rating counts.  
3. **Average Price by Category** → Bar chart of mean prices per category.  
4. **Price vs Rating** → Scatter plot showing relationship between rating and price.  

Additional:
- **Word Cloud** → Generated from combined book descriptions (`wordcloud.png`).  
- **Summary Statistics** → Used Pandas `.describe()` and groupby to identify:
  - Category patterns.  
  - Highly rated books.  
  - Stock availability patterns.  
  - Missing/unusual values.  

---

##  Task 4 — Insights and Interpretation
- **Category Patterns**: Certain categories showed higher average prices.  
- **Highly Rated Books**: Identified titles with rating = 5.  
- **Stock Patterns**: Most books marked “In stock”; few outliers.  
- **Missing Values**: Some descriptions were absent, noted in report.  

---


