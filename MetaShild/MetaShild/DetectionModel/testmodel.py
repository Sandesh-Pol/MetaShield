import joblib
import pandas as pd
import json
import os

# Load the trained model, encoders, and scaler
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
encoders_path = os.path.join(os.path.dirname(__file__), "label_encoders.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

try:
    model = joblib.load(model_path)
    label_encoders = joblib.load(encoders_path)
    scaler = joblib.load(scaler_path)
except FileNotFoundError as e:
    print(f"Error: {e}")
    model, label_encoders, scaler = None, None, None  # Prevents crashes if files are missing

# Function to handle unknown categories
def encode_value(column, value):
    encoder = label_encoders.get(column, None)
    if encoder is not None:
        if value in encoder.classes_:
            return encoder.transform([value])[0]
        else:
            print(f"Warning: Unknown {column} '{value}' found, using default encoding (-1).")
            return -1  # Assign -1 for unknown values
    return -1  # Default encoding for missing encoder

# Function to predict sensitivity for a single record
def predict(record):
    if model is None or label_encoders is None or scaler is None:
        return {"Error": "Model or encoders are not loaded."}

    try:
        # Encode categorical values
        file_extension_encoded = encode_value('file_extension', record['file_extension'])
        filename_encoded = encode_value('filename', record['filename'])
        esign_encoded = encode_value('esign', record['esign'])

        # Scale numerical features
        input_df = pd.DataFrame([[record['size_kb'], record['page_count']]], columns=['size_kb', 'page_count'])
        scaled_features = scaler.transform(input_df)
        size_kb_scaled, page_count_scaled = scaled_features[0]

        # Prepare the feature array
        input_features = pd.DataFrame([[file_extension_encoded, filename_encoded, size_kb_scaled, page_count_scaled, esign_encoded]],
                                      columns=['file_extension', 'filename', 'size_kb', 'page_count', 'esign'])

        # Predict sensitivity
        prediction = model.predict(input_features)[0]
        predicted_label = "Sensitive" if prediction == 1 else "Not Sensitive"
        return {"Filename": record["filename"], "Predicted": predicted_label}
    
    except Exception as e:
        return {"Filename": record["filename"], "Error": str(e)}  # Capture error instead of crashing

# Test Case
# print(predict({'file_extension': 'pdf', 'filename': 'PAN.pdf', 'size_kb': 4454.34, 'page_count': 10, 'esign': 'Unknown'}))
