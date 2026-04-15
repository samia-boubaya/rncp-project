# 🏡 Real Estate Investment Value Predictor & Recommendation
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
- What type of property should I purchase?  
- Where should I invest?  
- What is the expected rental value?  
- Can I get real-time property recommendations?  
- How do I maximize ROI with a given budget?

## 🧠 Methodology

To answer these questions, we use:
- **5-year datasets of French real estate transactions**  
- External data sources (rental prices, transport, amenities)  
- Machine learning models  


## 🎯 Objective
To assess, predict and recommend what and where to invest in French real-estate properties for best ROI based on a given budget so even small investors can start investing more in France. 

To **assess, predict and recommend the best real estate investments in France** based on:
- Budget  
- Location  
- Property characteristics  


## ⚙️ Installation (requirements.txt)
```bash
!pip install -r requirements.txt
```

## Machine Learning

### Type of ML problem
A regression problem where:
- Target: the property's value
- Features: , , , ...

### Evaluation Metrics
table of evaluation metrics for regression problem
- 
-
-
### Models Results
table comparing models results


## Data
This dataset contains real-estate transactions across France between 2020 2nd Semester and 2025 1st Semester, including mainland and overseas areas.
## Data Sources
Table of data sources:
+ DVF (transactions) Concatinated into a large file 'ValeursFoncieres_2020-S2_2025-S1.csv'

TXT files:

        - ValeursFoncieres_2020-S2
        - ValeursFoncieres_2021
        - ValeursFoncieres_2022
        - ValeursFoncieres_2023
        - ValeursFoncieres_2024
        - ValeursFoncieres_2025-S1

+ API Geospatial Rental prices by location in France
+ Scraped Website: SeLoger.com (real-time property listings for recommendations)
+ API Transport
+ API POI


### Data fileds

| Original Field Name          | Standardized              | Description                                      | Type (Cat/Numeric) | Python Type        |
|-----------------------------|--------------------------|--------------------------------------------------|--------------------|--------------------|
| **Date mutation**           | `transaction_date`       | Date when the property was sold                  | Categorical        | string             |
| **Nature mutation**         | `transaction_type`       | Nature of transaction (sale, donation, etc.)     | Categorical        | string             |
| **Valeur fonciere**         | `property_value`         | Transaction price in euros                       | Numeric (TARGET)            | float64            |
| **No voie**                 | `street_number`          | Street number of the property                    | Categorical        | string             |
| **B/T/Q**                   | `btq_code`               | Bâtiment/Type/Quartier code                     | Categorical        | string             |
| **Voie**                    | `street_name`            | Full street name                                 | Categorical        | string             |
| **Code postal**             | `postal_code`            | Postal code (categorical, not numeric)           | Categorical        | string             |
| **Commune**                 | `com_name`               | Commune name                                     | Categorical        | string             |
| **Nombre de lots**          | `lots_count`             | Number of lots in the property                   | Numeric            | Int64 (nullable)   |
| **Type local**              | `property_type`          | Property type (Apartment, House, etc.)           | Categorical        | category           |
| **Surface reelle bati**     | `building_real_surface`  | Built area in square meters                      | Numeric            | float64            |
| **Nombre pieces principales**| `main_rooms_count`      | Number of main rooms                             | Numeric            | Int64 (nullable)   |
| **Surface terrain**         | `land_surface`           | Land area in square meters                       | Numeric            | float64            |
| **Code departement**        | `dep_code`               | Department code (DD or DDD)                      | Categorical        | string             |
| **Code commune**            | `com_code`               | Commune code (CCC or CC)                         | Categorical        | string             |
| **Code voie**               | `street_id`              | Street identifier                               | Categorical        | string             |


## Database Design (Entity Relational Diagram)
- EDA using MySQL workbench

## API Endpoints
- amenities
- location gps


## Conclusions
- Best property type to invest in is:
- Best communes to invest in are:
- Most profitable is: 

-
## Limitations
- Almost half the dataset has an unknown type of property
- A lot of real-estate property listings aren't evne publicly available

## Future Improvements
- To webscrape from different sources such as agencies
- Expand to the world properties



## Author
Mme BOUBAYA Samia
