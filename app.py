from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model and scaler
with open("fish_weight_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        data = [float(request.form[feature]) for feature in ['Length1', 'Length2', 'Length3', 'Height', 'Width']]
        species_data = [0] * 6  # Placeholder for one-hot encoded species features
        species_dict = {"Bream": 0, "Parkki": 1, "Perch": 2, "Pike": 3, "Roach": 4, "Smelt": 5}
        species_input = request.form["Species"]
        if species_input in species_dict:
            species_data[species_dict[species_input]] = 1

        # Combine numerical and categorical inputs
        final_features = np.array(data + species_data).reshape(1, -1)
        final_features_scaled = scaler.transform(final_features)

        # Predict fish weight
        prediction = model.predict(final_features_scaled)

        return render_template('index.html', prediction_text=f'Predicted Fish Weight: {prediction[0]:.2f} grams')
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
