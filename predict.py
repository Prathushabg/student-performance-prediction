import streamlit as st
import pandas as pd
import joblib
from database import save_prediction

# ---------------- LOAD MODEL & ENCODERS ---------------- #

model = joblib.load("model/student_model.pkl")
encoders = joblib.load("model/encoders.pkl")


# ---------------- PREDICTION PAGE ---------------- #

def prediction_page():

    st.title("🤖 AI Student Performance Predictor")

    st.markdown("""
Predict a student's expected Mathematics score using
Machine Learning.

Fill in the details below and let AI predict the result.
""")

    st.divider()

    st.subheader("📝 Student Information")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "👤 Gender",
            list(encoders["gender"].classes_)
        )

        race = st.selectbox(
            "🌍 Race / Ethnicity",
            list(encoders["race/ethnicity"].classes_)
        )

        parental = st.selectbox(
            "🎓 Parent Education",
            list(encoders["parental level of education"].classes_)
        )

    with col2:

        lunch = st.selectbox(
            "🍱 Lunch Type",
            list(encoders["lunch"].classes_)
        )

        preparation = st.selectbox(
            "📚 Test Preparation",
            list(encoders["test preparation course"].classes_)
        )

        reading = st.slider(
            "📖 Reading Score",
            0,
            100,
            50
        )

        writing = st.slider(
            "✍️ Writing Score",
            0,
            100,
            50
        )

    st.divider()

    if st.button("🚀 Predict Performance"):

        with st.spinner("🤖 AI is analyzing student performance..."):

            input_data = pd.DataFrame({

                "gender": [
                    encoders["gender"].transform([gender])[0]
                ],

                "race/ethnicity": [
                    encoders["race/ethnicity"].transform([race])[0]
                ],

                "parental level of education": [
                    encoders["parental level of education"].transform([parental])[0]
                ],

                "lunch": [
                    encoders["lunch"].transform([lunch])[0]
                ],

                "test preparation course": [
                    encoders["test preparation course"].transform([preparation])[0]
                ],

                "reading score": [reading],

                "writing score": [writing]

            })

            prediction = model.predict(input_data)[0]
            prediction = round(prediction, 2)

        st.success("✅ Prediction Completed Successfully!")

        st.markdown(
            f"""
<div style="
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 3px 12px rgba(0,0,0,0.15);
text-align:center;
">

<h2>📊 Predicted Mathematics Score</h2>

<h1 style="color:#2563EB;">{prediction}</h1>

</div>
""",
            unsafe_allow_html=True
        )

        if prediction >= 80:

            level = "🌟 Excellent"
            message = "Outstanding performance! Keep up the excellent work."

        elif prediction >= 60:

            level = "👍 Good"
            message = "Good performance. Practice consistently to improve further."

        elif prediction >= 40:

            level = "🙂 Average"
            message = "Needs more preparation and regular practice."

        else:

            level = "⚠ Needs Improvement"
            message = "Focus on the basics and practice daily."

        col1, col2 = st.columns(2)

        with col1:

            st.info(f"""
### 📈 Performance Level

**{level}**
""")

        with col2:

            st.warning(f"""
### 💡 AI Recommendation

{message}
""")

        save_prediction(
            gender,
            reading,
            writing,
            prediction
        )

        st.success("Prediction saved successfully in database ✅")