# 🤖 MechMaster Servo Ensemble Predictor

This repository showcases **MechMaster**, a Streamlit application that predicts the **Class** value of servo mechanisms using an **ensemble of machine learning models**.

---

## 📌 Objective
Leverage multiple regressors—**Ridge with polynomial features**, **Decision Tree**, **Random Forest**, **Gradient Boosting**, and **SVR**—to accurately estimate servo performance classes and combine predictions through a median ensemble.

---

## 🧰 Tools & Libraries
- 🐍 **Python 3.x**  
- 📊 **Pandas**, **NumPy** – data handling  
- 📈 **Scikit-learn** – model training, pipelining, hyperparameter tuning  
- 📉 **Matplotlib**, **Seaborn** *(optional)* – exploratory data visualization  
- 🚀 **Streamlit** – interactive web UI  
- 💾 **Joblib** – model serialization  

---

## 📁 Repository Structure
```
MechMaster-Servo-Ensemble/
├── data/
│ └── Servo_Mechanism.csv
├── models/
│ ├── ridge_poly_model.pkl
│ ├── decision_tree_model.pkl
│ ├── random_forest_model.pkl
│ ├── gradient_boosting_model.pkl
│ └── svr_rbf_model.pkl
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
   git clone https://github.com/your-username/MechMaster-Servo-Ensemble.git
   cd MechMaster-Servo-Ensemble
2. Create and activate a virtual environment
  ```
  python -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\\Scripts\\activate   # Windows
  ```
3. Install dependencies
  ```
  pip install -r requirements.txt
  ```
4. Run the Streamlit app
  ```
  streamlit run streamlit_app.py
  ```

## 🔍 Project Workflow
1. Exploratory Data Analysis (EDA)
2. Data preview, missing values, distributions, correlations
3. Feature Engineering & Preprocessing
4. One-hot encode Motor, Screw; scale numerical; add polynomial features
5. Model Training
6. Train and tune Ridge (polynomial) and SVR (RBF) via GridSearchCV
7. Fit Decision Tree, Random Forest, Gradient Boosting
8. Ensembling
9. Serialize each pipeline with Joblib
10. Combine via median ensemble for robust predictions
11. **Deployment**: Streamlit UI to input parameters and display individual and ensemble outputs

## 📈 Performance Metrics
1. Model	MSE	R²
2. Ridge + Polynomial	X.XXX	X.XXX
3. SVR (RBF)	X.XXX	X.XXX
4. Decision Tree	X.XXX	X.XXX
5. Random Forest	X.XXX	X.XXX
6. Gradient Boosting	X.XXX	X.XXX
7. Median Ensemble	X.XXX	X.XXX


## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## 📝 Author
Built and maintained by Kshitij Kashyap.
