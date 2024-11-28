import pandas as pd

def load_data(file_path):
    df = pd.read_csv('/amazon.csv')
    # Clean and preprocess the data
    df['sub_category'] = df['category'].str.split('|').str[-1]
    df['main_category'] = df['category'].str.split('|').str[0]
    df['rating_count'] = df['rating_count'].str.replace(',', '').astype(float)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['discount_percentage'] = pd.to_numeric(df['discount_percentage'].str.replace('%', ''), errors='coerce')
    return df
