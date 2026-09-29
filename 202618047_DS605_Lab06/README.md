# DS605 Lab 06: Feature Extraction and Machine Learning with Image and Text Data

## Student Details
- **Name:** Ameya Trivedi
- **Student ID:** 202618047
- **Course:** DS605
- **Lab:** 06

## Objective
The objective of this lab is to convert raw image and text data into numerical feature representations and apply traditional machine learning models for classification.

## Datasets
### 1. Asphalt Crack Dataset
- Total images: 400
- Crack images: 200
- Non-crack images: 200

### 2. Email Spam Classification Dataset
- Total emails: 5,171
- Ham emails: 3,672
- Spam emails: 1,499

## Part A: Image Feature Extraction and Classification

### Methodology
1. Loaded asphalt images using OpenCV.
2. Resized images to 128 × 128 pixels.
3. Converted images into grayscale.
4. Extracted numerical features using NumPy and OpenCV:
   - Mean brightness
   - Contrast
   - Dark-pixel ratio
   - Bright-pixel ratio
   - Median brightness
   - Minimum and maximum intensity
   - Edge count
   - Edge density
5. Applied Canny edge detection to identify edges in the images.
6. Created a feature table with one row per image.
7. Trained and evaluated the following classifiers:
   - Logistic Regression
   - Random Forest
   - Support Vector Machine (SVM)

### Evaluation
The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Training time
- Prediction time

## Part B: Text Vectorization and Spam Classification

### Methodology
1. Loaded and inspected the email dataset.
2. Cleaned the email text.
3. Converted text into numerical features using:
   - CountVectorizer
   - TF-IDF Vectorizer
4. Trained Logistic Regression models using both representations.
5. Compared model performance and computational time.

### Results

| Representation | Features | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|---:|
| CountVectorizer | 3,917 | 0.9865 | 0.9643 | 0.9900 | 0.9770 |
| TF-IDF Vectorizer | 3,917 | 0.9865 | 0.9643 | 0.9900 | 0.9770 |

## Part C: Improved Feature Representation

Feature dimensionality was reduced from 3,917 to 2,000 using feature selection.

### Comparison

| Representation | Features | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|---:|
| Original CountVectorizer | 3,917 | 0.9865 | 0.9430 | 0.9900 | 0.9700 |
| Reduced CountVectorizer | 2,000 | 0.9360 | 0.9590 | 0.9870 | 0.9210 |

### Observation
Reducing the number of features decreased the feature dimensionality and training time. However, the reduced representation also resulted in lower accuracy and F1-score.

## Key Observations
- Image features were extracted using traditional image-processing techniques.
- Canny edge detection was used to identify edges in asphalt images.
- CountVectorizer and TF-IDF were compared for spam classification.
- Feature selection reduced the number of text features from 3,917 to 2,000.
- Traditional machine learning models were used without CNNs, deep-learning models, or pretrained image embeddings.

## Technologies Used
- Python
- NumPy
- Pandas
- OpenCV
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Repository Contents
- `202618047_DS605_lab06.ipynb` — Complete notebook
- `image_dataset/` — Asphalt crack images
- `text_dataset/` — Email datasets
- `README.md` — Project documentation

## Conclusion
This lab demonstrates how image and text data can be converted into numerical features for classification using traditional machine learning techniques. The experiments compare image classifiers, text vectorization methods, and a reduced-feature representation.