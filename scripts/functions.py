# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import seaborn as sns

plt.style.use('ggplot')
pd.set_option('display.max_columns', 200) # to display all columns in the dataframe


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# define function display_data to explore each dataset
# This function will be used to explore each dataset in the notebooks
# It will display the shape, head, data types, missing values and unique values of each column in the dataframe
# -------------------------------------------------------------------------------
def display_data(df):
    # ----------------------------------------
    # Display shape and head of the dataframe
    # ----------------------------------------
    print(f"Dataset Shape: {df.shape[0]} rows and {df.shape[1]} columns\n")
    display(df.head(3))
    print(100*"-" + "\n")

    # ----------------------------------------------------------
    # Display data types & missing values of each column in df
    # ----------------------------------------------------------
    print("Data Types & Missing Values of Each Column:")
    display(df.info())

    # ---------------------------------------------------
    # Display Info & unique values for each column in df    
    # ---------------------------------------------------
    for col in df.columns:
        unique_vals = df[col].unique()
        print(f"Column: {col}")
        print(f"Unique values ({len(unique_vals)}): {unique_vals}\n")

    print(f"\nData types check:")
    for col in df.columns:
        dtype = df[col].dtype
        unique_vals = df[col].nunique()
        print(f"  ➡️{col:<25} {str(dtype):<10} [{unique_vals}] unique values")





def display_info(df, df_label):
    """
    Explore a DataFrame safely without crashing on large datasets.
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataframe to explore
    df_label : str
        Name of the dataframe for display purposes
    """
    # ----------------------------------------
    # Display shape and head of the dataframe
    # ----------------------------------------
    print(f"{df_label} Shape: {df.shape[0]} rows and {df.shape[1]} columns\n")
    display(df.head(5))
    print("-" * 80)

    # ----------------------------------------
    # Display data types & missing values
    # ----------------------------------------
    print(f"{df_label} Columns Info:\n")
    dtypes_df = df.dtypes.to_frame("dtype")
    missing_df = df.isna().sum().to_frame("missing_values")
    display(dtypes_df)
    display(missing_df)
    print("-" * 80)

    # ----------------------------------------
    # Show unique values only for columns with <= 20 unique values
    # ----------------------------------------
    for col in df.columns:
        nunique = df[col].nunique(dropna=True)
        if nunique <= 20:
            print(f"Column: {col} | {nunique} unique values -> {df[col].unique()}")
    print("-" * 80)