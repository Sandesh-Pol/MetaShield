
---

# 🚀 **Meta-Shield: AI-Powered Sensitive Document Classification**  

🔍 **Classify documents as Sensitive (Y) or Non-Sensitive (N) using only metadata – No content analysis required!**  

## 📌 **Project Overview**  
Organizations process thousands of files daily, some containing sensitive information that must be protected. **Meta-Shield** is an AI-powered solution that automates document classification using **file metadata** to enhance security and compliance with regulations like **GDPR, HIPAA, and DPDP**.  

✅ **Key Features:**  
- 📂 **Metadata-Based Classification** – No content reading, ensuring privacy  
- 🤖 **AI-Driven Predictions** – Uses **Random Forest** for high accuracy  
- 🎯 **Confidence Score** – Provides a reliability score for predictions  
- 🌐 **Django Web Interface** – User-friendly UI for easy access  
- 🏗️ **Scalable & Deployable** – Ready for enterprise integration  

---

## 🏗️ **Team - CODE_AKATSUKI**  
🔹 **Sandesh Pol**
🔹 **Sushant Khadake**
🔹 **Irfan Naikwade**
🔹 **Tushar Neje**


---

## 🏗️ **Tech Stack**  
🔹 **Machine Learning** – Random Forest Classifier  
🔹 **Python** – Pandas, Scikit-Learn, NumPy, Joblib  
🔹 **Django** – Web framework for UI  
🔹 **HTML & CSS** – For frontend styling  
🔹 **Docker** (Future Scope) – For containerized deployment  

---

## 🛠️ **Setup & Installation**  

### 🔹 **Prerequisites**  
Ensure you have the following installed:  
✅ Python (>=3.8)  
✅ pip (Python package manager)  
✅ Virtual environment (optional but recommended)  

### 🔹 **Installation Steps**  
1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/your-repo/meta-shield.git
cd meta-shield
```
  
2️⃣ **Create a Virtual Environment & Activate It**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
  
3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```
  
4️⃣ **Run the Model Training**  
```bash
python train_model.py
```
  
5️⃣ **Start the Web Interface**  
```bash
python manage.py runserver
```
Access the UI at **http://127.0.0.1:8000/**  

---

## 📊 **How It Works?**  
1️⃣ **Train the AI Model** – Uses metadata (file name, size, type, timestamps) to learn patterns  
2️⃣ **Upload a File or Enter Metadata** – Predict sensitivity status using ML  
3️⃣ **Get Instant Results** – The system returns:  
   - **Sensitive (Y) / Non-Sensitive (N)**  
   - **Confidence Score (%)**  

---

## 🎯 **Future Enhancements**  
🚀 **Advanced ML Models** – Exploring deep learning for improved classification  
📡 **API Deployment** – Making it accessible via REST API  
📊 **Interactive Dashboards** – Real-time reports & insights  
🔄 **Continuous Learning** – Feedback-based model improvement  

---

## 🤝 **Contributing**  
We welcome contributions! 🎉 Feel free to fork this repo, make improvements, and submit a PR.  

---

## 📜 **License**  
📄 This project is licensed under the **MIT License** – free to use and modify!  

---

💡 **Have suggestions or feedback? Reach out!** 🚀