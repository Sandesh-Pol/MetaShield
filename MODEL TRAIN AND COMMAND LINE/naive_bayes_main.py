import pandas as pd
import nltk
import joblib
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Download stopwords
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("comprehensive_file_metadata.csv")

# Text Preprocessing
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    words = text.lower().split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

df["processed_name"] = df["filename"].apply(preprocess)

# Feature Extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["processed_name"])
y = df["sensitive"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Multinomial Naive Bayes Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save the model and vectorizer
joblib.dump(model, "sensitive_doc_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

