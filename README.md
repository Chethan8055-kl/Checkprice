 🚗 Used Car Price Predictor

This is a simple AI-powered web application that predicts the selling price of a used car based on its features such as model, fuel type, transmission, kilometers driven, owner type, etc.

The app is built using:
- Python
- pandas & scikit-learn for data preprocessing and model training
- Streamlit for creating the web UI

 📁 Project Structure

UsedCarPricePredictor/
│
├── car_data.csv # Original dataset
├── train_model.py # Script to clean data and train the model
├── car_price_model.pkl # Saved machine learning model
├── app.py # Streamlit app
└── README.md # This file

 ⚙️ Installation

1. Clone the repository or Download the ZIP
2. Navigate to the project directory  
```bash
cd UsedCarPricePredictor
Install dependencies

bash
pip install -r requirements.txt
If you don't have a requirements.txt, you can install manually:

bash
pip install pandas scikit-learn streamlit
🚀 Running the App
bash
streamlit run app.py
Then go to http://localhost:8501 in your browser to access the app.

🧠 How it Works
train_model.py:

Cleans and processes the car dataset (car_data.csv)

Applies one-hot encoding to categorical columns

Trains a LinearRegression model

Saves it as car_price_model.pkl

app.py:

Loads the saved model

Takes user input via Streamlit widgets

Builds a one-hot encoded input DataFrame

Predicts and displays the selling price

📊 Features Used
model

kms_driven

car_age (from year)

fuel_type (Petrol/Diesel/CNG/LPG/Electric)

transmission (Manual/Automatic)

owner (First/Second/Third/Fourth+)

insurance (Yes/No)

📌 Example Input
Model: Swift VDI

KMs Driven: 55,000

Car Age: 6 years

Fuel Type: Diesel

Transmission: Manual

Owner: First Owner

Insurance: Yes

→ Predicted Selling Price: ₹3.5 lakhs (approx.)

📤 Deployment (Optional)
You can deploy this app for free using:

Streamlit Community Cloud

Render

Heroku

🧑‍💻 Author
Chethan KL
Developed with ❤️ using open-source tech.

📜 License
This project is open-source and free to use under the MIT License.

Thank you
Copy
Eit
