# 🧠 Autism Spectrum Disorder (ASD) Predictor

This project is a web-based application that predicts the likelihood of Autism Spectrum Disorder (ASD) using a machine learning model. It leverages Streamlit for the user interface and Scikit-learn for model training and prediction.

---

## 🚀 Features

- 🔍 Predicts ASD based on user inputs
- 🧪 Machine Learning model trained using Random Forest Classifier
- 🧠 Based on clinical and behavioral features
- 📊 Clean and simple Streamlit interface
- 💾 Includes model persistence using `joblib`

---

## 🖼️ Screenshots

![ASD Predictor UI](https://via.placeholder.com/600x350?text=Upload+Screenshot+Here)

---

## 🛠️ Tech Stack

| Tool            | Description                          |
|-----------------|--------------------------------------|
| Python          | Core programming language            |
| Streamlit       | Web framework for the UI             |
| Scikit-learn    | Machine Learning model training      |
| Pandas & NumPy  | Data manipulation and preprocessing  |
| Joblib          | Model serialization                  |

---

## 📂 Project Structure

<pre lang="markdown"> ```bash ASD-Predictor/ │ ├── app/ │ ├── app.py # Main Streamlit app │ ├── model.joblib # Trained ML model │ └── preprocess.py # Feature processing functions │ ├── requirements.txt # Python dependencies ├── README.md # Project overview └── dataset/ # (Optional) Training data ``` </pre>


---

## 📈 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/asd-predictor.git
cd asd-predictor

###2. Install Dependencies

pip install -r requirements.txt

###3. Run the Streamlit App

streamlit run app/app.py

##📊 Dataset
Source: Kaggle Autism Screening Dataset

Features Used: Age, Gender, Ethnicity, Jaundice, Family history, Behavioral patterns, etc.

##🔮 Model
Algorithm: Random Forest Classifier

Accuracy: (Insert accuracy or performance here)

Input Features: 20 features used for training

##🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

##🧑‍💻 Author
Falak Vhora
Bachelor's in AI & ML | Open Source Contributor
GitHub • LinkedIn