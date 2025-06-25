from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler (ensure they are in same folder or use full path)
model = pickle.load(open('rf_acc_68.pkl', 'rb'))
scaler = pickle.load(open('normalizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [
            float(request.form['age']),
            float(request.form['total_bilirubin']),
            float(request.form['direct_bilirubin']),
            float(request.form['alkaline_phosphotase']),
            float(request.form['alamine_aminotransferase']),
            float(request.form['aspartate_aminotransferase']),
            float(request.form['total_proteins']),
            float(request.form['albumin']),
            float(request.form['albumin_globulin_ratio'])
        ]

        # Normalize and Predict
        input_data = np.array([features])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        result = '🟥 Liver Disease Detected' if prediction == 1 else '🟩 No Liver Disease'

        return render_template('result.html', prediction_text=result)

    except Exception as e:
        return render_template('result.html', prediction_text=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
