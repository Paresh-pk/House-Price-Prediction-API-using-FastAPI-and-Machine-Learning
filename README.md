# California House Price Prediction API 🏠

## 📘 Project Overview

This project provides a **machine learning-powered API** to predict the **median house value** in California districts.  
The API is built using **FastAPI**, and the prediction model is a **Random Forest Regressor** trained on the **California Housing dataset**.  
A simple **HTML frontend** is also included to interact with the API.

The API exposes endpoints to:
- Check service health
- Get model information
- Make predictions based on housing features

It includes **robust data validation and preprocessing** to ensure accurate predictions.

---

## 🧠 Dataset

The project uses the **California Housing Prices** dataset, originally published in:

> Pace, R. Kelley, and Ronald Barry. *"Sparse spatial autoregressions."* Statistics & Probability Letters 33.3 (1997): 291–297.

Each row represents a block group in California from the 1990 census.

### Dataset Features:

| Feature | Description |
|----------|--------------|
| `longitude` | How far west a house is |
| `latitude` | How far north a house is |
| `housing_median_age` | Median age of a house within a block |
| `total_rooms` | Total number of rooms within a block |
| `total_bedrooms` | Total number of bedrooms within a block |
| `population` | Total number of people residing within a block |
| `households` | Total number of households within a block |
| `median_income` | Median income for households within a block (in tens of thousands of USD) |
| `ocean_proximity` | Location of the house w.r.t ocean/sea |
| `median_house_value` | Target variable — median house value |

---

## ⚙️ Setup Instructions

Follow these steps to set up and run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Dependencies

Ensure you have **Python 3.8+** installed. It’s recommended to use a virtual environment.

```bash
# Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

> 💡 If you don’t have a `requirements.txt`, create one containing:
> `fastapi`, `uvicorn`, `scikit-learn`, `pandas`, `numpy`

### 3️⃣ Train the Model

Run the training script (`House_Price_Prediction_API_using_FastAPI_and_Machine_Learning.ipynb`)
or `train.py` to generate `random_forest_model.pkl`.

### 4️⃣ Run the API Server

Once the dependencies are installed and the model file is generated, start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🚀 API Endpoints

### 1️⃣ **Health Endpoint**

**URL:** `http://127.0.0.1:8000/health`  
**Method:** `GET`

**Response Example:**
```json
{"status": "ok"}
```

---

### 2️⃣ **Model Info Endpoint**

**URL:** `http://127.0.0.1:8000/model-info`  
**Method:** `GET`

**Response Example:**
```json
{"model_name": "RandomForestRegressor (California Housing)", "model_description": "A pipeline model..."}
```

---

### 3️⃣ **Predict Endpoint**

**URL:** `http://127.0.0.1:8000/predict`  
**Method:** `POST`

This endpoint makes predictions for the median house price.

#### 🧩 Example Request (via `curl`)
```bash
curl -X 'POST'   'http://127.0.0.1:8000/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
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
```

**Example Successful Response:**
```json
{"predicted_price": 452600.0}
```

---

## 🌐 Testing the API

### 🖥️ Method A: Using `main.html`
1. Ensure your FastAPI server is running.
2. Open `main.html` in your browser.
3. Fill in the form with house details.
4. Click **“Predict Price”** — the predicted price will appear on the page.

### 🧪 Method B: Using FastAPI Docs (Recommended)
1. Start the FastAPI server.
2. Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
3. Click on the **POST /predict** section → “Try it out” → Fill in example data → Execute.
4. View the prediction in the response.

---

## 🧾 Example JSON Input
```json
{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "ocean_proximity": "NEAR BAY"
}
```

**Example Output:**
```json
{"predicted_price": 452600.0}
```

---

## 🧑‍💻 Author
**Paresh Kumar Palai**  
Final-Year MCA Student, Tripura University  
Aspiring AI Engineer | Passionate Learner

---

## 🏁 License
This project is open source and available under the [MIT License](LICENSE).
