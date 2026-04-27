# 🏡 French Real-Estate Property Value Predictor
**Find the best properties in France for your investment!**

## 📌 Project Overview
Many real estate investors struggle to decide **what to buy** and **where to invest** to maximize their return on investment (ROI).

This project introduces a **data-driven application** that helps investors:
- Predict property values  
- Identify high-potential locations and properties based on a budget
- Get real-time property recommendations  

## ❗ Problem
Real Estate Investors in France would like to know what and where to buy for best ROI.

## ❓ Key Questions
- Which property to purchase? What characteristics?
- Where to invest?  
- When is it best to purchase?
- What is the market rental value for this property (estimated)?  
- Want to maximize ROI with a specific budget?
- Which properties to avoid?
- Want real-time property listings recommendations?  

## 🧠 Methodology
To answer these questions, we used:
- **Flat files:** 6 year datasets of French real estate transactions  
- **APIs** External data sources for Rental prices
- **Web Scraping** SeLoger.com to extract real-time property listing 
- **Machine learning models** to predict the property value
- **Python** and **SQL** to analyse the data
- **Flask** to build the frontend of the app deployment


## 🎯 Objective
To assess, predict and recommend what and where to invest in French real-estate properties for best ROI based on a given budget so even small investors can start investing more in France. 

To **assess, predict and recommend the best real estate investments in France**, we input:
```text
- Budget  (moving gauge)
- Location  (Geo map)
- Property characteristics (text input)
```

## ⚙️ Installation (requirements.txt)
```bash
!pip install -r requirements.txt
```

## Data
This dataset contains real-estate transactions across France between 2020 2nd Semester and 2025 1st Semester, including mainland and overseas areas.

[Dataset Link – Demandes de valeurs foncières](https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres/) (downloaded in April 2026)

## Data Sources
- FLAT FILES: DVF 2020-S2 to 2025-S1
- APIs: Geospatial for rental prices by location in France
- WEB SCRAPING: SeLoger.com (real-time property listings for recommendations)
- MySQL database:(Entity Relational Diagram using MySQL workbench)


## SQL Querries & insights
SQL querries and insights

## ERD
Entity Relational Diagram with at least 4 entities and 3 relationships


## Exploratory Data Analysis (EDA)
This repository structure contains the EDA where each notebook is a key step.

**0. DATA COLLECTION & EXPLORATION**

**1. DATA CLEANING**
```text
1.1. CREATE new unique TRANSACTION ID 
1.2. CONCAT files and convert into 1 CSV
1.3. STANDARDIZE column names
1.4. Deal with INVALID VALUES
1.5. CONVERT dtypes
1.6. Deal with NULLS
1.7. Deal with DUPLICATES: removed true duplicate rows and only kept first occurence with non duplicate rows from the dataset.
1.8. Deal with OUTLIERS
1.9. SAVE CLEAN FILE
```
**2. WEB SCRAPING (SeLoger.com)**

**3. DATA ANALYSIS**


## Machine Learning (ML)
**ML KEY STEPS:**
```text
1. DATA PREPROCESSING
2. MODELS & EVALUATION
3. DEPLOYMENT
```

### ML PROBLEM TYPE
It's a REGRESSION PROBLEM.

### **TARGET & FEATURES**
#### **THE TARGET** (**Valeur foncière** == `property_value`) : 
```text
- It's the transaction amount in EUROS. 
- This amount does not include notary fees and agency fees because it ultimately corresponds to the value of the property in a transaction whether it was a sale or exchange. 
- This amount is inclusive of VAT.
```
#### **FEATURES** (`Property characteristics`)
These are the selected features:

**CATEGORICAL Features:**
```text
- `transaction_year`: 
        - 2020, 2021, 2022, 2023, 2024, 2025
        
- `transaction_month`: 
        - JAN, FEB, MAR, APR, MAY, JUN, JUL AUG, SEP, OCT, NOV, DEC
        
- `transaction_type`:

        - Sale in future state of completion
        - Sale of unbuilt land
        - Sale
        - Expropriation
        - Auction
        - Exchange

- `property_type`: 
        - House
        - Apartment
        - Industrial or commercial premises
        - Outbuilding
        - Unknown

- `surface_type`: 
        - building
        - land
        - combined
        - Unknown

- 
 ```
 **NUMERIC Features:**
```text
- property_surface
- `longitude`
- `latitude`
```
### Data Preparation for Machine Learning
Since we handled invalid values, missing values, duplicates, and outliers in the EDA step data cleaning
We only need to focus on preprocessing for the sake of Machine Learning and created a new CSV file `ML_ValeursFoncieres.csv`
        - Number of rooms is null i.e there is no room so we fill nan with 0
        - The target `property_value` has null values so in order to work with scikitlearn we filter them
        - Label missing categorical data

### Data Preprocessing
```text
1. Drop Columns 
        - with mostly null values
        - with ID and future information
2. Split data to Train/Test sets
3. Feature Engineering & Feature Scaling
4. Derive New Features
```

### Models Results Evaluation
After training different models, record their results in a Google Sheet for later to rank

The models:
        - **Baseline**
        - **Linear Regression**
        - **XGBoost**
        - **CatBoost**
        - **LightGBM**

#### ML Model Evaluation Metrics (KPI)
`Note: Evaluate the model on the test data.`

For this regression problem, we use the following metrics:
- **R² Score,** To note that the R² value must be greater than 0 and in the best case 1 
- **Mean Absolute Error (MAE),**
- **Root Mean Squared Error (RMSE).**

![Regression Evaluation Metrics](images/Regression_problem_EVALUATION_METRICS.png)

Let's compare the models results:

![ML Models Results Comparison](images/Models%20Results%20Comparison.png)



### Deployment
```text
After comparing models results, we select the best model and use it for deploying our app.
```


![Demo Predict Price](images/demo-predict-price.png)

## Limitations
```text
- Almost half the dataset has an "Unknown" property type
- 
- 
```

## Conclusions
```text
- Best property types to invest in is:
- Best locations to invest in are:
```
## Future Improvements
```text
- Dataset preprocessing must be improved further to produce better result.
- Using only the top best important features with algorithm can improve model performance
- To webscrape from different sources such as agencies
- API Transport for distance calculation
- API Amenities for granular assessment of Property Neighbourhood value 
```

## Author
```text
Mme BOUBAYA Samia
```

## Version Control & Date 
```text
Version 01: April 2026
```