import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
file_path = "comprehensive_file_metadata.csv"
df = pd.read_csv(file_path)

# Encode categorical variables
label_encoders = {}
for col in ['file_extension', 'filename', 'esign']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define features and target
X = df.drop(columns=['sensitive'])
y = df['sensitive']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale numerical features
scaler = StandardScaler()
X_train[['size_kb', 'page_count']] = scaler.fit_transform(X_train[['size_kb', 'page_count']])
X_test[['size_kb', 'page_count']] = scaler.transform(X_test[['size_kb', 'page_count']])

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

joblib.dump(model, "sensitivity_model.pkl")

# Save the scaler and encoders
joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")
joblib.dump(model, "model.pkl")

# Save the LabelEncoders
joblib.dump(label_encoders, "label_encoders.pkl")

# Save the StandardScaler
joblib.dump(scaler, "scaler.pkl")

print("Model and preprocessing objects saved successfully!")
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", report)
