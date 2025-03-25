# src/data_preprocessing.py
import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    
    # For numerical columns: fill missing values with median
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # For categorical columns: fill missing values with mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

def feature_engineering(df):
    # Assume 'Id' is an identifier and 'SalePrice' is our target
    features = df.drop(columns=['Id', 'SalePrice'], errors='ignore')
    target = df['SalePrice']
    
    # One-hot encode categorical features
    features_encoded = pd.get_dummies(features, drop_first=True)
    
    return features_encoded, target

def preprocess_and_save(raw_filepath, output_filepath='preprocessed_data.csv'):
    df = load_and_clean_data(raw_filepath)
    X, y = feature_engineering(df)
    
    # Combine features and target for later use (optional)
    processed_data = X.copy()
    processed_data['SalePrice'] = y
    processed_data.to_csv(output_filepath, index=False)
    print(f"Preprocessed data saved to {output_filepath}")

if __name__ == '__main__':
    raw_data_file = 'data/house_prices.csv'  # Adjust the path as needed
    preprocess_and_save(raw_data_file)