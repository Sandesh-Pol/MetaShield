import os
import joblib
import nltk
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# Download NLTK Stopwords
nltk.download('stopwords')

# Load the trained model and vectorizer
model = joblib.load(r"C:\Users\Admin\Desktop\HACKTHON PICT\MetaShield\MODEL TRAIN AND COMMAND LINE\flask app\sensitive_doc_model.pkl")
vectorizer = joblib.load(r"C:\Users\Admin\Desktop\HACKTHON PICT\MetaShield\MODEL TRAIN AND COMMAND LINE\flask app\vectorizer.pkl")

# Initialize Flask app
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

# Ensure the upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Preprocessing function
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    words = text.lower().split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Get the uploaded file
        uploaded_file = request.files["file"]
        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            uploaded_file.save(file_path)  # Save the file

            # Process filename and predict
            processed_name = preprocess(filename)
            transformed_text = vectorizer.transform([processed_name])
            prediction = model.predict(transformed_text)[0]

            # Show result
            result = "Sensitive Document" if prediction == 1 else "Not Sensitive"
            return render_template("index.html", filename=filename, result=result)

    return render_template("index.html", filename=None, result=None)

if __name__ == "__main__":
    app.run(debug=True)
