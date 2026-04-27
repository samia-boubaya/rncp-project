## DATA DICTIONARY

- This dataset represents historical French property transactions from the **2nd semester of 2020** to the **1st semester of 2025**.

- Each transaction can have **multiple rows**, since a single notarial sale may include several properties, parcels, or lots.

- The 6 files from **2020-S2 to 2025-S1** must be concatenated into a single CSV file.

- These data correspond to real estate transactions across France (both metropolitan and overseas territories), sourced from notarial deeds and cadastral records.

- Source: https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres

The data fields in the dataset are as follows:

0. <b>N° de disposition → `transaction_id`:</b>  
Identifier of a notarial act grouping multiple rows belonging to the same sale.  
Note: This field is not strictly reliable as a unique transaction identifier when concatenating datasets; therefore, a new `transaction_id` was generated to ensure uniqueness.

1. <b>Date mutation → `transaction_date`:</b>  
Exact date when the notarial deed was signed, representing the official transfer of ownership.

2. <b>Nature mutation → `transaction_type`:</b>  
Legal type of transaction such as standard sale, VEFA (sale before completion), land sale, auction (adjudication), expropriation, or exchange.

3. <b>Valeur fonciere → `property_value`:</b>  
Declared transaction price in euros (TTC), excluding notary and agency fees, representing the net value agreed between buyer and seller.

4. <b>No voie → `street_number`:</b>  
Numeric identifier assigned to a property along a street, used for precise location and address matching.

5. <b>B/T/Q → `btq_code`:</b>  
Additional address qualifier (e.g., Bis, Ter, Quarter) used to distinguish multiple properties sharing the same street number.

6. <b>Type de voie → `street_type`:</b>  
Category of the road (e.g., Rue, Avenue, Boulevard, Chemin), useful for address standardization.

7. <b>Code voie → `street_id`:</b>  
Official administrative code identifying the street within the commune.

8. <b>Voie → `street_name`:</b>  
Full textual name of the street as recorded in official address registries.

9. <b>Code postal → `postal_code`:</b>  
Five-digit postal code used for mail delivery and geographic grouping.

10. <b>Commune → `com_name`:</b>  
Name of the municipality (city or town) where the property is located.

11. <b>Code departement → `dep_code`:</b>  
Administrative code identifying the department, used for regional classification and analysis.

12. <b>Code commune → `com_code`:</b>  
Official INSEE code identifying the commune within a department.

13. <b>Prefixe de section → `section_prefix`:</b>  
Optional prefix used in cadastral identification to distinguish sections in complex or reorganized areas.

14. <b>Section → `section`:</b>  
Cadastral section identifier grouping parcels within a commune.

15. <b>No plan → `plot_number`:</b>  
Unique number identifying a land parcel within a cadastral section.

16. <b>No Volume → `volume_number`:</b>  
Identifier used for properties defined by volume divisions (e.g., multi-level ownership structures).

17. <b>1er lot → `lot_1`:</b>  
Identifier of the first co-ownership lot included in the transaction (e.g., apartment, cellar, parking).

18. <b>Surface Carrez du 1er lot → `lot_1_surface`:</b>  
Private usable surface area of the first lot in square meters, measured under Carrez law.

19. <b>2eme lot → `lot_2`:</b>  
Identifier of the second lot included in the transaction.

20. <b>Surface Carrez du 2eme lot → `lot_2_surface`:</b>  
Surface area of the second lot in square meters (Carrez measurement).

21. <b>3eme lot → `lot_3`:</b>  
Identifier of the third lot included in the transaction.

22. <b>Surface Carrez du 3eme lot → `lot_3_surface`:</b>  
Surface area of the third lot in square meters.

23. <b>4eme lot → `lot_4`:</b>  
Identifier of the fourth lot included in the transaction.

24. <b>Surface Carrez du 4eme lot → `lot_4_surface`:</b>  
Surface area of the fourth lot in square meters.

25. <b>5eme lot → `lot_5`:</b>  
Identifier of the fifth lot included in the transaction (only the first five lots are recorded).

26. <b>Surface Carrez du 5eme lot → `lot_5_surface`:</b>  
Surface area of the fifth lot in square meters.

27. <b>Nombre de lots → `lots_count`:</b>  
Total number of lots involved in the transaction, including those not individually detailed.

28. <b>Code type local → `property_type_code`:</b>  
Encoded categorical value representing the property type for standardized processing.

29. <b>Type local → `property_type`:</b>  
Human-readable property category such as house, apartment, commercial premises, or outbuilding.

30. <b>Surface reelle bati → `building_real_surface`:</b>  
Actual built floor area measured inside the walls (m²), excluding land.

31. <b>Nombre pieces principales → `main_rooms_count`:</b>  
Number of main living rooms (e.g., bedrooms, living room), excluding auxiliary spaces.

32. <b>Nature culture → `land_nature`:</b>  
General classification of land usage (e.g., agricultural land, forest, vineyard, pasture, building land).

33. <b>Nature culture speciale → `land_nature_special`:</b>  
More detailed classification refining the general land usage category.

34. <b>Surface terrain → `land_surface`:</b>  
Total cadastral land area in square meters.

35. <b>(Derived) → `surface_type`:</b>  
Engineered feature indicating whether the property includes built area only, land only, or both.

36. <b>(Derived) → `effective_surface`:</b>  
Computed total surface equal to built surface plus land surface, used for normalization.

37. <b>(Derived for ANALYSIS) → `value_per_m2`:</b>  
Price per square meter calculated as property value divided by effective surface.

<b>(Derived) → longitude:</b>
Geographic longitude coordinate obtained through geocoding.

<b>(Derived) → latitude:</b>
Geographic latitude coordinate obtained through geocoding.

<b>(Derived) → com_type:</b>
Classification of the commune based on density or urbanization level (e.g., urban, suburban, rural).

<b>(Derived) → insee_code:</b>
Official geographic identifier combining department and commune codes (DDCCC for mainland France, DDDCC for overseas).

<b>(Derived for ML) → transaction_year:</b>
Year extracted from the transaction date, used for temporal modeling.

<b>(Derived for ML) → transaction_month:</b>
Month extracted from the transaction date, used for seasonality analysis and modeling.


...

### DATA TABLE
| #  | Original Name           | Standard Name            | Description                                       | Data Type      | Variable Type                          |
| -- | ------------------------------ | ----------------------- | ------------------------------------------------- | -------------- | ----------------------------- |
| 0  | (derived after seeing that **No disposition** is unreliable)             | `transaction_id`        | Unique identifier of the transaction              | string         | Categorical / identifier      |
| 1  | **Date mutation**              | `transaction_date`      | Date when the property was sold                   | datetime64[ns] | Temporal                      |
| 2  | **Nature mutation**            | `transaction_type`      | Nature of transaction (sale, exchange, etc.)      | string         | Categorical                   |
| 3  | **Valeur fonciere**            | `property_value`        | Transaction price in euros                        | Float64        | Numeric (**TARGET**)          |
| 4  | **No voie**                    | `street_number`         | Street number of the property                     | string         | Categorical / identifier      |
| 5  | **B/T/Q**                      | `btq_code`              | Building / Type / Quarter code                    | string         | Categorical                   |
| 6  | **Type de voie**               | `street_type`           | Type of street (Rue, Avenue, etc.)                | string         | Categorical                   |
| 7  | **Code voie**                  | `street_id`             | Street identifier code                            | string         | Categorical / identifier      |
| 8  | **Voie**                       | `street_name`           | Full street name                                  | string         | Categorical                   |
| 9  | **Code postal**                | `postal_code`           | Postal code                                       | string         | Categorical / geographic code |
| 10 | **Commune**                    | `com_name`              | Commune name                                      | string         | Categorical                   |
| 11 | **Code departement**           | `dep_code`              | Department code                                   | string         | Categorical / geographic code |
| 12 | **Code commune**               | `com_code`              | Commune code                                      | string         | Categorical / geographic code |
| 13 | **Prefixe de section**         | `section_prefix`        | Section prefix used in cadastral identification   | string         | Categorical / cadastral code  |
| 14 | **Section**                    | `section`               | Cadastral section identifier                      | string         | Categorical / cadastral code  |
| 15 | **No plan**                    | `plot_number`           | Parcel / plot number                              | string         | Categorical / identifier      |
| 16 | **No Volume**                  | `volume_number`         | Volume number for special cadastral cases         | string         | Categorical / identifier      |
| 17 | **1er lot**                    | `lot_1`                 | Identifier of the first lot                       | string         | Categorical / identifier      |
| 18 | **Surface Carrez du 1er lot**  | `lot_1_surface`         | Carrez surface of the first lot in square meters  | Float64        | Numeric                       |
| 19 | **2eme lot**                   | `lot_2`                 | Identifier of the second lot                      | string         | Categorical / identifier      |
| 20 | **Surface Carrez du 2eme lot** | `lot_2_surface`         | Carrez surface of the second lot in square meters | Float64        | Numeric                       |
| 21 | **3eme lot**                   | `lot_3`                 | Identifier of the third lot                       | string         | Categorical / identifier      |
| 22 | **Surface Carrez du 3eme lot** | `lot_3_surface`         | Carrez surface of the third lot in square meters  | Float64        | Numeric                       |
| 23 | **4eme lot**                   | `lot_4`                 | Identifier of the fourth lot                      | string         | Categorical / identifier      |
| 24 | **Surface Carrez du 4eme lot** | `lot_4_surface`         | Carrez surface of the fourth lot in square meters | Float64        | Numeric                       |
| 25 | **5eme lot**                   | `lot_5`                 | Identifier of the fifth lot                       | string         | Categorical / identifier      |
| 26 | **Surface Carrez du 5eme lot** | `lot_5_surface`         | Carrez surface of the fifth lot in square meters  | Float64        | Numeric                       |
| 27 | **Nombre de lots**             | `lots_count`            | Number of lots in the transaction                 | Int64          | Numeric count                 |
| 28 | **Code type local**            | `property_type_code`    | Code for property type                            | string         | Categorical code              |
| 29 | **Type local**                 | `property_type`         | Property type (Apartment, House, etc.)            | string         | Categorical                   |
| 30 | **Surface reelle bati**        | `building_real_surface` | Built area in square meters                       | Float64        | Numeric                       |
| 31 | **Nombre pieces principales**  | `main_rooms_count`      | Number of main rooms                              | Int64          | Numeric count                 |
| 32 | **Nature culture**             | `land_nature`           | General type of land usage                        | string         | Categorical                   |
| 33 | **Nature culture speciale**    | `land_nature_special`   | Specific type of land usage                       | string         | Categorical                   |
| 34 | **Surface terrain**            | `land_surface`          | Land area in square meters                        | Float64        | Numeric                       |
| 35 | *(derived)*                    | `surface_type`          | Type of surface: building / land / combined       | string         | Derived categorical           |
| 36 | *(derived)*                    | `property_surface`          | sum of the surfaces (building and land)       | Float64         | Derived numeric           |
| 37 | *(derived for ANALYSIS)*                    | `value_per_m2`          | value devided by effective_surface        | Float64         | Derived numeric           |
| 38 | *(derived)*                    | `longitude`          | longitude of property       | Float64         | Derived numeric           |
| 39 | *(derived)*                    | `latitude`          | Latitude of property       | Float64         | Derived numeric           |
| 40 | *(derived)*                    | `com_type`          | Commune type       | string         | Derived categorical           |
| 41 | *(derived)*                    | `insee_code`          | insee_code is either DDCCC (mainland) or DDDCC (overseas)       | Int64         | Derived categorical           |
| 42 | *(derived for ML)*                    | `transaction_year`          | The year the transaction was made (for ML)       | int         | Derived categorical           |
| 43 | *(derived for ML)*                    | `transaction_month`          | The month the transaction was made (for ML)       | string         | Derived categorical           |


## Additional explanation

- From the `property_type` field, an *outbuilding* refers to a non-habitable unit that is separate from the main dwelling, such as a cellar, garage, or garden shed.

- The `transaction_date` corresponds to the date when the notarial deed is signed. This is a crucial variable, as property prices are not directly comparable across different time periods (e.g., the same property sold in 2020 vs 2025).

- **What is the difference between real_building_surface, land_surface, and property_surface?**  
In simple terms, *surface* refers to a flat area (in m²), while *property_surface* refers to the total surface combining both `building_real_surface` and `land_surface`. 
In this dataset, **land_surface** represents the area of the land (specifically when `surface_type = 'land'`), whereas **building_real_surface** refers to the floor space inside a totally or partially built property (`surface_type = 'building'`). 

- In the DVF dataset, the **B/T/Q** column is a shorthand for additional address details that help locate the exact property within a given street number:

  - **B → Bâtiment (Building)**
  - **T → Type** (subdivision such as unit, lot, or section)
  - **Q → Quartier** (neighborhood, block, or zone)

- This information is used together with **street number (No voie)**, **street name (Voie)**, and sometimes **street code (Code voie)** to accurately identify properties, especially in large buildings, complexes, or multi-lot sites.

- `main_rooms_count` only applies to properties with a `building_real_surface` greater than 0.

Here are some categorical features values for a better understanding:

- `transaction_type`:
    - Sale in future state of completion
    - Sale of unbuilt land
    - Expropriation
    - Auction
    - Sale
    - Exchange

- `property_type`: 
    - House
    - Apartment
    - Industrial or commercial premises
    - Outbuilding
    - Unknown

- `property_type_code`:
    - 1
    - 2
    - 3 
    - 4
    - Unknown

- `surface_type`:
    - building
    - land
    - combined
    - Unknown










