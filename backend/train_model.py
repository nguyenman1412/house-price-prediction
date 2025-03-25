# src/train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

def load_data(filepath):
    data = pd.read_csv(filepath)
    X = data.drop(columns=['SalePrice'])
    y = data['SalePrice']
    return X, y

def train_and_evaluate(data_filepath, model_filepath='house_price_model.joblib'):
    X, y = load_data(data_filepath)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Mean Absolute Error on test set: {mae:.2f}")
    
    joblib.dump(model, model_filepath)
    print(f"Trained model saved to {model_filepath}")

if __name__ == '__main__':
    preprocessed_file = 'preprocessed_data.csv'
    train_and_evaluate(preprocessed_file)