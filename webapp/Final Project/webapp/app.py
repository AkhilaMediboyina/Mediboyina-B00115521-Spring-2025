import os
import pandas as pd
import pickle
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename

# Import utilities
from utils.data_processing import clean_data, encode_categorical
from utils.visualization import plot_bar_chart
#from models.predictor import train_model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
app.secret_key = "your_secret_key"

# Ensure uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Global variable to store uploaded data
df = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global df
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        df = pd.read_csv(filepath)
        df = clean_data(df)  # Handle missing values
        df, _ = encode_categorical(df)  # Encode categorical data
        
        session['filename'] = filename
        return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    global df
    if df is None:
        return redirect(url_for('index'))

    chart = None
    if request.method == 'POST':
        selected_column = request.form['column']
        chart = plot_bar_chart(df, selected_column)

    return render_template('dashboard.html', columns=df.columns.tolist(), chart=chart)

@app.route('/train', methods=['GET', 'POST'])
def train():
    global df
    if df is None:
        return redirect(url_for('index'))

    if request.method == 'POST':  # Train model when form is submitted
        try:
            #model = train_model(df)
            return render_template('train.html', success=True)
        except Exception as e:
            return render_template('train.html', error=str(e))

    return render_template('train.html', success=False)



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if df is None:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            with open("models/sales_model.pkl", "rb") as f:
                model = pickle.load(f)

            # Extract feature values from form input
            features = [float(request.form[col]) for col in df.drop(columns=['ProdTaken', 'CustomerID']).columns]
            prediction = model.predict([features])[0]
            
            return render_template('predict.html', prediction=prediction)

        except Exception as e:
            return render_template('predict.html', error=str(e))
    
    # If GET request, just show the prediction form
    return render_template('predict.html', prediction=None)


if __name__ == '__main__':
    app.run(debug=True)
