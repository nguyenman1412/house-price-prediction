# House Price Prediction App

This is a full-stack application that predicts house prices using a machine learning model.

## Project Structure
house-price-prediction/
├── backend/
│   ├── app.py                   # Flask API
│   ├── data_preprocessing.py    # Data cleaning & feature engineering
│   ├── train_model.py           # Model training & evaluation
│   ├── requirements.txt         # Dependencies
│   └── Dockerfile               # Docker container config
├── data/
│   └── house_prices.csv         # Sample dataset
├── frontend/
│   ├── index.html               # Main UI
│   ├── css/styles.css           # Custom styles
│   ├── js/app.js                # JavaScript for API calls
│   └── assets/                  # Optional images or other assets

## How to Run

1. **Backend**  
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   The Flask API will start at http://localhost:5100 by default.
2.	**Frontend**
	•	Open frontend/index.html in your browser OR
	•	Serve it locally:
    cd frontend
    python -m http.server 8000
Visit http://localhost:8000 and enter house details to see the prediction.
**Docker (Optional)**
	• You can also run the backend in Docker:
    cd backend
    docker build -t house-price-app .
    docker run -p 5100:5100 house-price-app
    
    Then access the API at http://localhost:5100.