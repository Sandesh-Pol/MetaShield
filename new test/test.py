import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

data = pd.read_csv("new test/output.csv")  # Ensure the correct path

data['File Name Clean'] = data['File Name'].astype(str).apply(lambda x: ' '.join(re.findall(r'\b\w+\b', x.lower())))

data['File Size KB'] = data['File Size (Bytes)'] / 1024  

sensitive_keywords = ["aadhaar", "marksheet", "certificate", "id", "diploma"]
data['Sensitive'] = data['File Name Clean'].apply(lambda x: 1 if any(word in x for word in sensitive_keywords) else 0)

vectorizer = TfidfVectorizer()
X_text = vectorizer.fit_transform(data['File Name Clean'])
X_text_df = pd.DataFrame(X_text.toarray(), columns=vectorizer.get_feature_names_out())

X_features = data[['File Size KB', 'Page Count']].fillna(0).reset_index(drop=True)
X_text_df = X_text_df.reset_index(drop=True)

X = pd.concat([X_features, X_text_df], axis=1)

X.columns = X.columns.astype(str)

y = data['Sensitive']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
