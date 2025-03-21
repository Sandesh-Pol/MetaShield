import pandas as pd
import nltk
import re
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Download necessary nltk resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Load CSV Data
df = pd.read_csv("comprehensive_file_metadata.csv")

# Ensure required columns exist
if 'filename' not in df.columns or 'sensitive' not in df.columns:
    raise ValueError("The dataset must contain 'filename' and 'sensitive' columns!")

# ✅ Visualization 1: Class Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x=df['sensitive'], palette="viridis")
plt.xticks(ticks=[0, 1], labels=['Not Sensitive', 'Sensitive'])
plt.title("Class Distribution of Sensitive vs Non-Sensitive Files")
plt.show()

# Advanced Text Preprocessing Function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # Remove special characters & punctuation
    words = text.split()  # Tokenization
    words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]  # Lemmatization & Stopword Removal
    return " ".join(words)

# Apply preprocessing to 'filename' column
df['processed_text'] = df['filename'].apply(preprocess_text)

# Feature Extraction using TF-IDF with n-grams
vectorizer = TfidfVectorizer(ngram_range=(1, 3), sublinear_tf=True)
X = vectorizer.fit_transform(df['processed_text'])
y = df['sensitive']

# Split Data into Training & Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# Train Naïve Bayes Classifier with Optimized Alpha
model = MultinomialNB(alpha=0.3)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Improved Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Visualization 2: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="coolwarm", xticklabels=['Not Sensitive', 'Sensitive'], yticklabels=['Not Sensitive', 'Sensitive'])
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

# ✅ Visualization 3: Top 20 Important Words
feature_names = vectorizer.get_feature_names_out()
feature_probs = model.feature_log_prob_[1]  # Sensitivity class (1)
top_words = sorted(zip(feature_probs, feature_names), reverse=True)[:20]

plt.figure(figsize=(8, 6))
sns.barplot(x=[x[0] for x in top_words], y=[x[1] for x in top_words], palette="magma")
plt.xlabel("Importance (Log Probability)")
plt.ylabel("Top Words")
plt.title("Top 20 Words Indicating Sensitivity")
plt.show()
