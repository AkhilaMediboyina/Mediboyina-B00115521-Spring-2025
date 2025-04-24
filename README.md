# README.md

### Overview

This project is focused on **Sales Prediction in the Tourism Industry** using an **LSTM (Long Short-Term Memory)** model. The goal is to predict future sales based on historical data and leading indicators related to the tourism industry. The model was trained using data related to tourism packages and external indicators, which you can find in the project’s **data** directory.

### How to Run/Interact/Reproduce the Work

1. **Clone the Repository**  
   To get started, first clone this repository to your local machine:
   ```bash
   git clone https://github.com/AkhilaMediboyina/Mediboyina-B00115521-Spring-2025.git

Install Required Dependencies
Navigate to the project folder and install the required Python libraries:

bash
Copy code
cd Mediboyina-B00115521-Spring-2025
pip install -r requirements.txt

Running the Code

Model: The model is saved as tourism_sales_predictor.h5 in the project directory. You can load and make predictions using this model.

Web App: If you want to interact with the model via a web app, follow the steps below.

To run the Python script and make predictions manually:

bash
Copy code
python predict_sales.py
This will load the trained model, input data, and return predictions.

Web App Setup
If you want to run the web app to interact with the model, follow these steps:

Install Flask (if you haven't already):

bash
Copy code
pip install flask
Navigate to the folder containing the main web app file (e.g., app.py) and run it:

bash
Copy code
python app.py
The app will start a server on http://127.0.0.1:5000/. Open this URL in your browser to interact with the model and make predictions through the web interface.

Making Predictions
In the web app, you can input various features such as tourism packages, pricing, and seasonal factors. After submitting the form, the model will display the predicted sales based on the input data.

Data
The dataset used for training the model is included in the data folder. This contains historical sales data, tourist package details, and leading indicators for tourism.

Tourism Sales Data: tour_package.csv

Tourism Sales Predictions: The output of the model will be displayed as predicted sales on the web app.

Handling Large Data
If the data files are too large to fit within the data directory, you can obtain the dataset from a shared link or an external storage service. Please refer to the contract for the specific location where large datasets can be accessed.

For example:

Data Access: If the data exceeds the size limits, you can access it via a shared Google Drive link or an external storage bucket. Make sure to update the README file with the correct link.

File Structure
The project is structured as follows:

php
Copy code
mediboyina-b00115521-spring-2025/
│
├── data/
│   └── tour_package.csv               # Raw tourism sales data
│
├── deliverables/
│   └── presentation/
│       └── final.pdf                  # Final presentation in PDF format
│
├── src/
│   └── predict_sales.py               # Python script to make predictions
│   └── app.py                         # Flask web app
│
├── README.md                          # Project overview and instructions
│
└── tourism_sales_predictor.h5         # Trained model





