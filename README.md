
# 🧠 Unimind Ensemble Predictor

Unimind is an interactive Streamlit application that delivers **smart ensemble predictions** by aggregating outputs from multiple machine learning models.

---

## 📌 Objective
Combine diverse regressors—**Ridge (polynomial)**, **Decision Tree**, **Random Forest**, **Gradient Boosting**, and **SVR**—to produce robust numerical predictions for any new data point through a median ensemble strategy.

---

## 🧰 Tools & Libraries
- 🐍 **Python 3.x**  
- 📊 **Pandas**, **NumPy** – data handling  
- 📈 **Scikit-learn** – model pipelines and hyperparameter searches  
- 🚀 **Streamlit** – elegant web interface  
- 💾 **Joblib** – serialization of pipelines  

---

## 📁 Repository Structure
```
Unimind-Ensemble-Predictor/
├── data/
│   └── Servo_Mechanism.csv
├── models/
│   ├── ridge_poly_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── gradient_boosting_model.pkl
│   └── svr_rbf_model.pkl
├── streamlit_app.py
├── EDA_script.py
├── 2_linear_regression_improved.py
├── 6_svr_improved.py
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/Unimind-Ensemble-Predictor.git
   cd Unimind-Ensemble-Predictor
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🔍 Project Workflow

1. **EDA:** Understand data distributions and correlations.  
2. **Preprocessing:** Encode categories, scale numerics, add polynomial features.  
3. **Model Training:** Train & tune multiple regressors via cross-validation.  
4. **Ensemble:** Serialize pipelines & combine via median for stability.  
5. **Deployment:** Streamlit UI for instant predictions.

---

## 📈 Performance Metrics

| Model                  | MSE    | R²    |
|------------------------|--------|-------|
| Ridge + Polynomial     |  X.XXX |  X.XXX|
| SVR (RBF)              |  X.XXX |  X.XXX|
| Decision Tree          |  X.XXX |  X.XXX|
| Random Forest          |  X.XXX |  X.XXX|
| Gradient Boosting      |  X.XXX |  X.XXX|
| **Median Ensemble**    |  X.XXX |  X.XXX|

*(Replace X.XXX with actual results)*

---

## 🤝 Contributing
Contributions welcome! Open issues or PRs to improve Unimind.

---

## 📝 Author
Built with ❤️ by **Kshitij Kashyap**.
