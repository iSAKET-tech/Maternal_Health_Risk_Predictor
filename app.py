import streamlit as st
import pickle
import pandas as pd


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Maternal Health Predictor",
    page_icon="🩺",
    layout="wide"
)


# ============================================================
# CUSTOM CSS — LOOKS ONLY
# ============================================================

st.markdown("""
<style>

    /* ---------- MAIN APP ---------- */

    .stApp {
        background-color: #10130F;
        color: #F4F4EF;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 45px;
        padding-bottom: 50px;
    }


    /* ---------- HEADER ---------- */

    .app-title {
        font-size: 42px;
        font-weight: 700;
        color: #F4F4EF;
        letter-spacing: -1px;
        margin-bottom: 5px;
    }

    .app-subtitle {
        font-size: 16px;
        color: #9EA49A;
        margin-bottom: 35px;
    }


    /* ---------- INPUT CARD ---------- */

    .input-card {
        background-color: #191D18;
        border: 1px solid #2C312A;
        border-radius: 16px;
        padding: 28px 30px 18px 30px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 20px;
        font-weight: 600;
        color: #D4A24C;
        margin-bottom: 22px;
    }


    /* ---------- INPUT LABELS ---------- */

    label {
        color: #C9CEC6 !important;
        font-size: 14px !important;
    }


    /* ---------- INPUT BOXES ---------- */

    div[data-baseweb="input"] {
        background-color: #111410 !important;
        border: 1px solid #343930 !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #D4A24C !important;
    }

    input {
        color: #F4F4EF !important;
    }


    /* ---------- BUTTON ---------- */

    .stButton {
        margin-top: 12px;
    }

    .stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 9px;
        border: none;
        background-color: #D4A24C;
        color: #11130F;
        font-size: 16px;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #E2B866;
        color: #11130F;
    }


    /* ---------- RESULT CARD ---------- */

    .result-card {
        background-color: #191D18;
        border: 1px solid #343930;
        border-radius: 16px;
        padding: 28px;
        margin-top: 30px;
        text-align: center;
    }

    .result-label {
        color: #929990;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    .result-value {
        color: #D4A24C;
        font-size: 32px;
        font-weight: 700;
        margin-top: 8px;
    }


    /* ---------- PROBABILITY ---------- */

    .probability-title {
        color: #F4F4EF;
        font-size: 20px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 10px;
    }


    /* ---------- TABLE ---------- */

    [data-testid="stDataFrame"] {
        border: 1px solid #2C312A;
        border-radius: 10px;
        overflow: hidden;
    }


    /* ---------- HIDE STREAMLIT DEFAULTS ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# MODEL — UNCHANGED
# ============================================================

pipe = pickle.load(open('pipe.pkl', 'rb'))


# ============================================================
# HEADER — UI ONLY
# ============================================================

st.markdown(
    '<div class="app-title">Maternal Health Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="app-subtitle">'
    'Machine learning-based maternal health risk prediction'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT SECTION — SAME INPUTS
# ============================================================

st.markdown(
    '<div class="input-card">'
    '<div class="section-title">Patient Information</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4, col5, col6 = st.columns(6)


with col1:
    Age = st.number_input("Age")


with col2:
    SystolicBP = st.number_input("SystolicBP")


with col3:
    DiastolicBP = st.number_input("DiastolicBP")


with col4:
    BS = st.number_input("BS")


with col5:
    BodyTemp = st.number_input("BodyTemp")


with col6:
    HeartRate = st.number_input("HeartRate")


st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# PREDICTION — LOGIC UNCHANGED
# ============================================================

if st.button('Predict Probability'):

    input_df = pd.DataFrame({
        'Age': [Age],
        'SystolicBP': [SystolicBP],
        'DiastolicBP': [DiastolicBP],
        'BS': [BS],
        'BodyTemp': [BodyTemp],
        'HeartRate': [HeartRate]
    })

    st.markdown(
        '<div class="probability-title">Input Summary</div>',
        unsafe_allow_html=True
    )

    st.table(input_df)

    result = pipe.predict(input_df)

    result2 = pipe.predict_proba(input_df)


    # ========================================================
    # RESULT — SAME VALUES, NEW LOOK
    # ========================================================

    st.markdown(
        '<div class="result-card">'
        '<div class="result-label">Risk Prediction</div>'
        f'<div class="result-value">{result[0]}</div>'
        '</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="probability-title">Risk Probability</div>',
        unsafe_allow_html=True
    )

    st.write((result2 * 100).round(2).astype(str) + "%")

    st.markdown(
        '<div class="probability-title">Classes</div>',
        unsafe_allow_html=True
    )

    st.write("['high risk' 'low risk' 'mid risk']")