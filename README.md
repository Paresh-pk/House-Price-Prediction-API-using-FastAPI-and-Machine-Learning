1- Project Overview

This project provides a machine learning-powered API to predict the median house value in California districts. The API is built using **FastAPI**, and the prediction model is a **Random Forest Regressor** trained on the California Housing dataset. The project includes a simple HTML frontend to interact with the API.

The API exposes endpoints to check service health, get model information, and make predictions based on housing features. It includes robust data validation and preprocessing steps to ensure accurate predictions.

***
## Dataset
The project uses the **California Housing Prices** dataset. This dataset was originally published in:

*Pace, R. Kelley, and Ronald Barry. "Sparse spatial autoregressions." Statistics & Probability Letters 33.3 (1997): 291-297.*

Each row in the dataset represents a block group in California from the 1990 census. The features are as follows:
* **`longitude`**: A measure of how far west a house is.
* **`latitude`**: A measure of how far north a house is.
* **`housing_median_age`**: Median age of a house within a block.
* **`total_rooms`**: Total number of rooms within a block.
* **`total_bedrooms`**: Total number of bedrooms within a block.
* **`population`**: Total number of people residing within a block.
* **`households`**: Total number of households within a block.
* **`median_income`**: Median income for households within a block (in tens of thousands of US Dollars).
* **`ocean_proximity`**: Location of the house w.r.t ocean/sea.
* **`median_house_value`**: The target variable; the median house value for households within a block.

***
## Setup Instructions

To set up and run this project on your local machine, please follow these steps.

**1. Clone the Repository**

'''bash

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

2. Install Dependencies
   
Make sure you have Python 3.8+ installed. It is recommended to use a virtual environment.

# Create a virtual environment (optional but recommended)

python -m venv venv

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required packages

pip install -r requirements.txt

(Note: If you don't have a requirements.txt file, create one with fastapi, uvicorn, scikit-learn, pandas, and numpy.)

3. Train the Model
   
Run the training script from the Jupyter Notebook (House_Price_Prediction_API_using_FastAPI_and_Machine_Learning.ipynb) or a separate train.py file to generate the random_forest_model.pkl file.

4. Run the API Server
   
Once the dependencies are installed and the model file is generated, start the FastAPI server using Uvicorn.

uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000.

# API Endpoint Documentation
The API provides the following endpoints:

## 1. Health Endpoint
This checks if the server is running.
URL Link: http://127.0.0.1:8000/health
How to Check: This is a GET request, so you can check it easily.

Make sure your server is running in the terminal.
Copy and paste the URL directly into your browser's address bar and press Enter.

What You Should See:

JSON

{"status":"ok"}
## 2. Model Info Endpoint
This gives you information about the model.

URL Link: http://127.0.0.1:8000/model-info

How to Check: This is also a GET request.
Make sure your server is running.
Copy and paste the URL directly into your browser's address bar and press Enter.

What You Should See:

JSON

{"model_name":"RandomForestRegressor (California Housing)","model_description":"A pipeline model..."}
## 3. Predict Endpoint
This is for making predictions and is the most important one.

URL Link: http://127.0.0.1:8000/predict

How to Check: This is a POST request, so you cannot just paste the URL into your browser. You must send data to it. Here are the two ways to check it:

Method A: Use the Web Page (main.html)

Make sure your server is running.

Open your main.html file in your browser.

Fill out the form with house details.

Click the "Predict Price" button.

The predicted price will appear on the page.

Method B: Use the API Docs (Best for testing)

Make sure your server is running.

Go to the documentation URL: http://127.0.0.1:8000/docs

Find the green POST /predict section and click on it.

Click the "Try it out" button.

A "Request body" text box will appear with example data.

Click the blue "Execute" button.

What You Should See: A successful response with a predicted price.

JSON

{"predicted_price": 452600.0}
Example Requests and Responses

You can interact with the API using the provided main.html file or by using a tool like curl.

Example curl request for the /predict endpoint:

curl -X 'POST' \
  '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  
  -d '{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "ocean_proximity": "NEAR BAY"
}'

Example successful response:

{
  "predicted_price": 452600.0
}
