# main.py (Corrected with Final Feature Order)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import pickle
from typing import Optional
import os

# 1. Initialize the FastAPI App
app = FastAPI(
    title="House Price Prediction API",
    description="An API to predict house prices using a pre-trained model.",
    version="1.0.0"
)

# 2. Add CORS Middleware Configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Load the Trained Model
MODEL_PATH = "random_forest_model.pkl"
if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found at path: {MODEL_PATH}")
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load the model. Error: {e}")

# 4. Define Pydantic Models
class HouseFeatures(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: Optional[float] = None
    population: float
    households: float
    median_income: float
    ocean_proximity: str

class PredictionResponse(BaseModel):
    predicted_price: float

# 5. Implement the API Endpoints
@app.get("/health", tags=["Management"])
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict_price(features: HouseFeatures):
    try:
        # Convert input data to a DataFrame
        input_df = pd.DataFrame([features.dict()])
        
        # --- START: CRITICAL PREPROCESSING STEP ---

        # 1. Create the engineered features to match the training notebook
        input_df['bedroom_ratio'] = input_df['total_bedrooms'] / input_df['total_rooms']
        input_df['room_per_household'] = input_df['total_rooms'] / input_df['households']

        # 2. Apply one-hot encoding WITHOUT adding a prefix to match the model's training
        input_df_encoded = pd.get_dummies(input_df, columns=['ocean_proximity'], prefix='', prefix_sep='')

        # 3. Define the exact column order the model was trained on
        # FINAL CORRECTION: Using the exact order you provided.
        model_columns = [
            'longitude', 'latitude', 'housing_median_age', 'total_rooms',
            'total_bedrooms', 'population', 'households', 'median_income',
            '<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN',
            'bedroom_ratio', 'room_per_household'
        ]
        
        # 4. Reindex the DataFrame to match the model's expected columns and order
        input_df_processed = input_df_encoded.reindex(columns=model_columns, fill_value=0)

        # --- END: CRITICAL PREPROCESSING STEP ---

        # Make a prediction using the correctly formatted data
        prediction = model.predict(input_df_processed)
        
        predicted_price = float(prediction[0])
        return {"predicted_price": predicted_price}
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during prediction: {str(e)}"
        )
