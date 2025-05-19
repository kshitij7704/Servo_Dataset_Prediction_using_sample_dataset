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
├── Decision Tree/
│   ├── Decision_Tree.ipynb
│   └── decision_tree_model.pkl
├── EDA/
│   └── EDA.ipynb
├── Ensemble/
│   ├── Ensemble.ipynb
│   └── ensemble_predictions.csv
├── Gradient Boosting/
│   ├── Gradient_Boosting.ipynb
│   └── gradient_boosting_model.pkl
├── Linear Regression/
│   ├── Linear_Regression.ipynb
│   └── linear_regression_model.pkl
├── Random Forest/
│   ├── Random_Forest.ipynb
│   └── random_forest_model.pkl
├── Svr/
│   ├── Svr.ipynb
│   └── svr_model.pkl
├── Output_SS.png
├── README.md
├── Servo_Mechanism.csv
├── app.py
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
Made by [**Kshitij Kashyap**](https://kshitij-kashyap-portfolio.netlify.app/)
