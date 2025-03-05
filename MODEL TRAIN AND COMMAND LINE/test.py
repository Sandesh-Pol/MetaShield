import joblib
import numpy as np
import pandas as pd

# Load the trained model, encoders, and scaler
model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
scaler = joblib.load("scaler.pkl")

# Sample records for testing
records = [
    {'file_extension': 'pdf', 'filename': 'Aadhaar_Original.pdf', 'size_kb': 2577.47, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'docx', 'filename': 'Article_Draft.docx', 'size_kb': 1485.79, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'xlsx', 'filename': 'BankStatement_Certified.xlsx', 'size_kb': 450.17, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'xlsx', 'filename': 'BankStatement_Original.xlsx', 'size_kb': 3717.73, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'pdf', 'filename': 'LectureNotes_Review.pdf', 'size_kb': 250.17, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'pdf', 'filename': 'Magazine_Final.pdf', 'size_kb': 2324.83, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'xlsx', 'filename': 'Newsletter_Final.xlsx', 'size_kb': 1399.62, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'jpeg', 'filename': 'Notes_Final.jpeg', 'size_kb': 85.16, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'pdf', 'filename': 'PAN.pdf', 'size_kb': 4454.34, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'docx', 'filename': 'PAN_Scan.docx', 'size_kb': 321.15, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'png', 'filename': 'RecipeCollection_Updated.png', 'size_kb': 60.17, 'page_count': 10, 'esign': 'Unknown'},
{'file_extension': 'png', 'filename': 'VoterID_Scan.png', 'size_kb': 1057.09, 'page_count': 10, 'esign': 'Unknown'}
]


# Function to handle unknown categories
def encode_value(column, value):
    encoder = label_encoders[column]
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        print(f"Warning: Unknown {column} '{value}' found, using default encoding (-1).")
        return -1  # Assign -1 for unknown values

# Function to test multiple records
def test_multiple_records(records):
    results = []
    for record in records:
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

            # Store results
            results.append({
                "Filename": record["filename"],
                "Predicted": predicted_label
            })
        
        except Exception as e:
            results.append({
                "Filename": record["filename"],
                "Error": str(e)  # Capture the error instead of crashing
            })
    
    return results

# Run the test
test_results = test_multiple_records(records)

# Print results
for res in test_results:
    if "Error" in res:
        print(f"Filename: {res['Filename']} | Error: {res['Error']}")
    else:
        print(f"Filename: {res['Filename']} | Predicted: {res['Predicted']}")
