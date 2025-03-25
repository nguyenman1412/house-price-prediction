// js/app.js
document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    // Gather input values from the form fields
    const payload = {
      LotArea: parseFloat(document.getElementById('lotArea').value),
      OverallQual: parseFloat(document.getElementById('overallQual').value),
      OverallCond: parseFloat(document.getElementById('overallCond').value),
      YearBuilt: parseFloat(document.getElementById('yearBuilt').value),
      TotalBsmtSF: parseFloat(document.getElementById('totalBsmtSF').value),
      GrLivArea: parseFloat(document.getElementById('grLivArea').value),
      FullBath: parseFloat(document.getElementById('fullBath').value),
      BedroomAbvGr: parseFloat(document.getElementById('bedroomAbvGr').value),
      TotRmsAbvGrd: parseFloat(document.getElementById('totRmsAbvGrd').value)
    };
  
    // Update UI: Clear previous result and show a loading message
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Predicting...';
  
    try {
      // Send the POST request to the backend API
      const response = await fetch('http://localhost:5100/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await response.json();
      resultDiv.textContent = `Predicted Sale Price: $${data.predicted_sale_price.toFixed(2)}`;
    } catch (error) {
      console.error('Error:', error);
      resultDiv.textContent = 'An error occurred while predicting.';
    }
  });