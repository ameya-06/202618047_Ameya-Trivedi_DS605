# Vectorized Programming with NumPy and Data Wrangling with Pandas

## Student Details

**Name:** Ameya Trivedi  
**Student ID:** 202618047

## Dataset

**Dataset:** Kaggle Titanic Dataset  
**File:** train.csv  
**Source:** Kaggle Titanic Competition

The dataset contains information about passengers aboard the Titanic, including passenger class, age, sex, fare, family information, port of embarkation, and survival status.

## Project Objective

The objective of this assignment is to practice:

- Vectorized programming using NumPy
- NumPy arrays and statistical operations
- Vectorized arithmetic and linear algebra
- Normal distribution and histogram visualization
- Data loading and inspection using Pandas
- Filtering and querying data
- Grouping and aggregation
- Handling missing values
- Detecting outliers using the IQR method
- Feature engineering
- Pivot tables
- Data visualization and interpretation

## Project Tasks

### Part A – Vectorized Programming with NumPy

- Created random NumPy arrays and calculated descriptive statistics.
- Used `np.arange()`, `np.zeros()`, `np.ones()` and `np.linspace()`.
- Created and manipulated 2D and 3D arrays.
- Performed reshaping and flattening.
- Performed vectorized matrix operations including addition, element-wise multiplication and matrix multiplication.
- Calculated matrix transpose, determinant and inverse.
- Generated normally distributed data and visualized it using a histogram.

### Part B – Data Wrangling with Pandas

- Loaded and inspected the Titanic dataset.
- Used `head()`, `tail()`, `shape`, `columns`, `info()` and `describe()`.
- Used `loc` and `iloc` for data selection.
- Applied Boolean indexing and filtering.
- Used `groupby()` and aggregation functions.
- Handled missing values using mean, median, mode and random-value imputation.
- Detected Fare outliers using the IQR method.
- Created `FamilySize` and `IsAlone` features.
- Created pivot tables based on Sex and Pclass.
- Created visualizations and analyzed relationships between variables.

## Key Observations

1. Female passengers had a substantially higher survival rate than male passengers.

2. First-class passengers had a higher survival rate compared with second- and third-class passengers.

3. Fare showed a positive relationship with survival, suggesting that passengers paying higher fares generally had better survival outcomes.

4. Pclass and Fare showed a strong relationship because first-class passengers generally paid higher fares than passengers in lower classes.

5. The Age vs Fare plot showed that most passengers had relatively low fares, while a smaller number of passengers paid very high fares.

6. SibSp and Parch showed a positive relationship, indicating that passengers travelling with siblings or spouses were more likely to also travel with parents or children.

7. The IQR method identified unusually high Fare values as outliers.

## Files Included

- `Titanic_Assignment.ipynb` – Complete runnable Jupyter Notebook containing the NumPy and Pandas code.
- `train.csv` – Original Kaggle Titanic dataset.
- `cleaned_titanic.csv` – Cleaned/processed Titanic dataset.
- `figures/` – Generated plots and visualizations.

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Conclusion

This assignment demonstrates the use of NumPy for vectorized numerical operations and Pandas for practical data wrangling. The Titanic dataset was used to perform data cleaning, filtering, aggregation, feature engineering, statistical analysis and visualization.
