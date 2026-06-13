import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import joblib


# Page setting
with st.sidebar:
    st.title("🏦 Credit Risk")
    st.markdown("---")
    st.subheader("Navigation")

    page = st.radio(
        "",
        [
            "📊 Risk Assessment",
            "📋 Customer Risk Report",
            "📈 Model Insights"
        ]
    )
    st.markdown("---")
    st.subheader("Model Information")
    st.metric(
        "ROC-AUC",
        "0.93"
    )
    st.metric(
        "Threshold",
        "0.20"
    )

    st.markdown("---")

    st.caption(
        "AI-Powered Credit Risk Assessment"
    )

st.set_page_config(
    page_title="Credit Risk Intelligence Platform",
    page_icon="🏦",
    layout="wide"
)


# Loading the model

model = joblib.load("models/loan_default_xgb.pkl")

# Layout

st.title("🏦 Credit Risk Intelligence Platform")
st.markdown("""
            AI - Powered Loan Default Prediction using XGBoost
""")

# st.success("Model Loaded Successfully")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label = "Model",
        value="XGBoost"
    )
with col2:
    st.metric(
        label="AUC Score",
        value="0.93"
    )

with col3:
    st.metric(
        label = "Threshold",
        value="0.20"
    )


st.divider()
st.subheader("👤 Borrower Profile")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Name",
        max_chars= 50
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    income = st.number_input(
        "Annual Income",
        min_value=0.0,
        value=50000.0
    )

    emp_length = st.number_input(
        "Employment Length (years)",
        min_value=0.0,
        max_value=60.0,
        value=5.0
    )

    home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "MORTGAGE", "OWN", "OTHER"]
    )

    cred_hist_length = st.number_input(
        "Credit History Length (years)",
        min_value=0,
        value=5
    )


with col2:

    loan_amnt = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=10000.0
    )

    loan_int_rate = st.number_input(
        "Loan Interest Rate (%)",
        min_value=0.0,
        max_value=40.0,
        value=11.0
    )

    loan_intent = st.selectbox(
        "Loan Intent",
        ["EDUCATION", "MEDICAL", "VENTURE", "PERSONAL",
         "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"]
    )

    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )

    default_on_file = st.selectbox(
        "Previous Default on File",
        ["N", "Y"]
    )


predict_button = st.button(
    "🔍 Assess credit Risk",
    type="secondary",
    use_container_width=True

)

if predict_button:
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Income:", income)
    st.write("Loan Amount:", loan_amnt)

    loan_percent_income = loan_amnt / income if income > 0 else 0
    loan_to_income_amount = loan_amnt / income if income > 0 else 0

    st.write("Loan Percent Income:", round(loan_percent_income, 4))

    risk_factor = []
    if loan_percent_income > 0.4:
        risk_factor.append("High loan-to-income ratio")
    if loan_int_rate > 15:
        risk_factor.append("High interest rate")
    if default_on_file == "Y":
        risk_factor.append("Previous default on file")
    if loan_grade in ["D", "E", "F", "G"]:
        risk_factor.append("Low loan grade")
    if emp_length < 1:
        risk_factor.append("Very short employment history")

    # Base input dict with numeric/engineered features
    input_dict = {
        'person_age': [age],
        'person_income': [income],
        'person_emp_length': [emp_length],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income': [loan_percent_income],
        'cb_person_cred_hist_length': [cred_hist_length],
        'LoanToIncomeAmount': [loan_to_income_amount],
        'person_home_ownership_OTHER': [1 if home_ownership == "OTHER" else 0],
        'person_home_ownership_OWN': [1 if home_ownership == "OWN" else 0],
        'person_home_ownership_RENT': [1 if home_ownership == "RENT" else 0],
        'loan_intent_EDUCATION': [1 if loan_intent == "EDUCATION" else 0],
        'loan_intent_HOMEIMPROVEMENT': [1 if loan_intent == "HOMEIMPROVEMENT" else 0],
        'loan_intent_MEDICAL': [1 if loan_intent == "MEDICAL" else 0],
        'loan_intent_PERSONAL': [1 if loan_intent == "PERSONAL" else 0],
        'loan_intent_VENTURE': [1 if loan_intent == "VENTURE" else 0],
        'loan_grade_B': [1 if loan_grade == "B" else 0],
        'loan_grade_C': [1 if loan_grade == "C" else 0],
        'loan_grade_D': [1 if loan_grade == "D" else 0],
        'loan_grade_E': [1 if loan_grade == "E" else 0],
        'loan_grade_F': [1 if loan_grade == "F" else 0],
        'loan_grade_G': [1 if loan_grade == "G" else 0],
        'cb_person_default_on_file_Y': [1 if default_on_file == "Y" else 0],
    }

    input_df = pd.DataFrame(input_dict)

    # Ensure column order matches model training
    input_df = input_df[model.feature_names_in_]

    probability = model.predict_proba(input_df)[0][1]
    if probability >= 0.8:
        recommendation = """Reject application or perform detailed review"""
    elif probability >= 0.4:
        recommendation = "Manual Verification recommended"
    else:
        recommendation = "Suitable candidate for loan approval"

    st.session_state["probability"] = probability
    st.session_state["recommendation"] = recommendation
    st.session_state["risk_factor"] = risk_factor

    st.session_state["age"] = age
    st.session_state["income"] = income
    st.session_state["loan_amnt"] = loan_amnt
    st.session_state["loan_percent_income"] = loan_percent_income
    st.session_state["name"] = name

    fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=probability * 100,

        title={
            'text': "Default Probability"
        },

        gauge={
            'axis': {
                'range': [0, 100]
            },

            'bar': {
                'color': "darkred"
            },

            'steps': [
                {'range': [0, 20], 'color': "lightgreen"},
                {'range': [20, 40], 'color': "yellow"},
                {'range': [40, 60], 'color': "orange"},
                {'range': [60, 100], 'color': "red"}
            ]
        }
    )
)
    # Threshold set to 0.2
    best_threshold = 0.2
    prediction = (probability >= best_threshold)


    st.divider()
    st.subheader("📊 Risk Assessment Result")

    left, right = st.columns([2,1])

    with left:
        st.plotly_chart(
        fig,
        use_container_width=True
    )

    with right:
        st.metric(
            "Default Probability",
            f"{probability*100:.2f}%"
        )

        st.metric(
            "Threshold",
            "20%"
        )

    if probability < 0.2:
        st.success("🟢 Very Low Risk")

    elif probability < 0.4:
        st.info("🔵 Low Risk")

    elif probability < 0.6:
        st.warning("🟡 Medium Risk")

    elif probability < 0.8:
        st.warning("🟠 High Risk")

    else:
        st.error("🔴 Very High Risk")

    if prediction:
        st.error(
            "⚠ High Probability of Default"

        )

    else:
        st.success(
            "✅ Low Probability of Default"
        )



elif page == "📈 Model Insights":

    st.title("📈 Model Insights")
    st.markdown(
        "Understand how the model makes predictions."
    )
    st.divider()
    st.subheader("Model Performance")
    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric(
            "ROC-AUC",
            "0.93"
        )

    with col2:
        st.metric(
            "Model",
            "XGBoost"
        )

    with col3:
        st.metric(
            "Threshold",
            "0.20"
        )
    st.divider()
    st.subheader("📊 Feature Importance")

    st.image(
        "assets/feature_importance.png",
        use_container_width=True
    )

    st.divider()
    st.subheader("🔍 SHAP Explainability")
    st.image(
        "assets/shap_summary.png",
        use_container_width=True
    )

    st.markdown("""
                ### Key Insights

                - Loan-to-income ratio is the strongest predictor of default.
                - Lower loan grades (D-G) sharply increase default risk.
                - Higher interest rates correlate with higher default risk.
                - Renting (vs owning/mortgage) increases default risk.
                - Previous default on file is a strong risk signal.


                """)



elif page == "📋 Customer Risk Report":
    st.title("📋 Customer Risk Report")

    if "probability" not in st.session_state:
        st.warning(
            "Please generate a prediction first from the Risk Assessment page."
        )
    else:
        st.subheader("📌 Executive Summary")
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("👤 Borrower Snapshot")
            st.write(
                f"Name: {st.session_state['name']}"
            )

            st.write(
            f"Age: {st.session_state['age']}"
            )

            st.write(
                f"Annual Income: ₹{st.session_state['income']:,.0f}"
            )

            st.write(
                f"Loan Amount: ₹{st.session_state['loan_amnt']:,.0f}"
            )

            st.write(
                f"Loan/Income Ratio: {st.session_state['loan_percent_income']:.2f}"
            )

        with col2:
            st.subheader("Key Risk Drivers")
            if st.session_state['probability'] <= 0.2:
                st.info("No such risk involved")
            else:
                for factor in st.session_state["risk_factor"]:
                    st.warning(factor)

        with col3:
            st.subheader("💡 Recommendation")
            st.info(
                st.session_state["recommendation"]
            )

        st.divider()
        st.subheader("📝 Executive Narrative")
        summary = f"""
        The customer exhibits a default probability of
        {st.session_state['probability']*100:.2f}%.

        Based on the configured threshold of 20%,
        the applicant has been classified as
        {'High Risk' if st.session_state['probability'] > 0.2 else 'Low Risk'}.

        The assessment indicates that loan-to-income ratio,
        loan grade and interest rate were significant
        contributors to the final decision.
        """

        st.text_area(
            "Report Summary",
            summary,
            height=320
        )
