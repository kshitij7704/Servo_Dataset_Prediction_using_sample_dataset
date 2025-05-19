import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Page Config ---
st.set_page_config(
    page_title="MechMaster Ensemble Predictor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0eafc, #cfdef3);
    }
    /* Global text color */
    .stApp, .stApp * {
        color: #333333 !important;
    }
    /* Title style */
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #003366 !important;
    }
    /* Button style */
    .stButton>button {
        background-color: #0066cc !important;
        color: white !important;
        font-size: 1.1rem;
        padding: 0.6rem 1rem;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #005bb5 !important;
        color: white;
    }
    /* Sidebar style */
    .sidebar .css-1lcbmhc { background-color: #ffffff !important; }
    /* Footer style */
    .footer {
        text-align: center;
        color: #555555 !important;
        padding-top: 1rem;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True
)

# --- Load Models ---
model_paths = {
    'Linear Regression': 'Linear Regression/linear_regression_model.pkl',
    'Decision Tree': 'Decision Tree/decision_tree_model.pkl',
    'Random Forest': 'Random Forest/random_forest_model.pkl',
    'Gradient Boosting': 'Gradient Boosting/gradient_boosting_model.pkl',
    'SVR': 'Svr/svr_model.pkl'
}

@st.cache_resource
def load_models(paths):
    return {name: joblib.load(path) for name, path in paths.items()}

models = load_models(model_paths)

# --- Sidebar for Inputs ---
st.sidebar.markdown("### 🔧 Servo Parameters")
motor = st.sidebar.selectbox("Motor Type", ['A', 'B', 'C', 'D', 'E'])
screw = st.sidebar.selectbox("Screw Type", ['A', 'B', 'C', 'D', 'E'])
pgain = st.sidebar.slider("Pgain", 0.0, 10.0, 5.0, 0.1)
vgain = st.sidebar.slider("Vgain", 0.0, 10.0, 5.0, 0.1)

# --- Main Header ---
st.markdown("<div class='title'>🤖 MechMaster Ensemble Predictor</div>", unsafe_allow_html=True)
st.markdown("<p>Use cutting-edge ensemble ML to predict servo <b>Class</b> values instantly!</p>", unsafe_allow_html=True)

# --- Prediction ---
if st.button("🚀 Predict Performance"):
    input_df = pd.DataFrame({
        'Motor': [motor],
        'Screw': [screw],
        'Pgain': [pgain],
        'Vgain': [vgain]
    })

    # Get predictions
    preds = {name: model.predict(input_df)[0] for name, model in models.items()}
    ensemble_pred = np.median(list(preds.values()))

    # Display individual model metrics as cards
    st.markdown("### Individual Model Predictions")
    cols = st.columns(len(preds))
    for col, (name, val) in zip(cols, preds.items()):
        col.metric(label=name, value=f"{val:.2f}")

    # Divider and ensemble
    st.markdown("---")
    st.markdown("### 🎯 Ensemble Prediction (Median)")
    st.markdown(f"<h1 style='color:#007f5f; text-align:center;'>{ensemble_pred:.2f}</h1>", unsafe_allow_html=True)

    st.success("🎉 Prediction Complete! Explore more or adjust parameters.")

# --- Footer ---
st.markdown("<div class='footer'>Built with ❤️ by Kshitij Kashyap | Powered by MechMaster Ensemble Pipelines</div>", unsafe_allow_html=True)