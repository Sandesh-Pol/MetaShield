import joblib
import pandas as pd

model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
scaler = joblib.load("scaler.pkl")

def encode_value(column, value):
    encoder = label_encoders[column]
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        print(f"Warning: Unknown {column} '{value}' found, using default encoding (-1).")
        return -1 
    
def predict(record):
    try:
        file_extension_encoded = encode_value('file_extension', record['file_extension'])
        filename_encoded = encode_value('filename', record['filename'])
        esign_encoded = encode_value('esign', record['esign'])

        input_df = pd.DataFrame([[record['size_kb'], record['page_count']]], columns=['size_kb', 'page_count'])
        scaled_features = scaler.transform(input_df)
        size_kb_scaled, page_count_scaled = scaled_features[0]

        input_features = pd.DataFrame([[file_extension_encoded, filename_encoded, size_kb_scaled, page_count_scaled, esign_encoded]],
                                      columns=['file_extension', 'filename', 'size_kb', 'page_count', 'esign'])
        prediction = model.predict(input_features)[0]
        predicted_label = "Sensitive" if prediction == 1 else "Not Sensitive"

        return {"Filename": record["filename"], "Predicted": predicted_label}
    
    except Exception as e:
        return {"Filename": record["filename"], "Error": str(e)} 
