import pandas as pd
import streamlit as st

# Load CSV file
def load_csv(input_csv):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
        input_csv (str): The path or filename of the CSV file to be loaded.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(input_csv)
    df.iloc[:,1] = pd.to_datetime(df.iloc[:,1])
    return df

TWENTYFIVE = 36524.2199/4

jubilees_dict = {}
for i in range(40):
    years = (i + 1) * 25
    key = f'{years} years'
    value = TWENTYFIVE * (i + 1)
    jubilees_dict[key] = value
