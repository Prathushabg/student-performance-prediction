import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image

from dashboard import dashboard_page
from predict import prediction_page
from auth import login


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="EduPredict AI",
    page_icon="🎓",
    layout="wide"
)
# ---------------- LOGIN SESSION ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()


# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:#F8FAFC;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    background:#2563EB;
    color:white;
    border:none;
}

.stButton>button:hover{
    background:#1D4ED8;
}


div[data-testid="metric-container"]{
    background:white;
    padding:20px;
    border-radius:15px;
}


section[data-testid="stSidebar"]{
    background:white;
}

</style>
""", unsafe_allow_html=True)



# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "https://img.icons8.com/color/96/student-center.png",
    width=80
)

st.sidebar.title("EduPredict AI")


menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🤖 Predict",
        "📜 History",
        "👨‍💻 About",
        "🚪 Logout"
    ]
)



# ---------------- HOME ---------------- #

if menu == "🏠 Home":

    st.title("🎓 Student Performance AI")


    try:

        image = Image.open("images/logo.png")
        st.image(
            image,
            width=180
        )

    except:

        st.info("🎓 EduPredict AI")



    st.markdown(
    """
    ## Welcome to Student Performance Prediction System 🚀


    An AI-powered application that predicts student performance
    using Machine Learning.


    ### Features:

    ✅ Machine Learning Prediction

    ✅ Interactive Dashboard

    ✅ Performance Analytics

    ✅ Prediction History

    ✅ Data Driven Insights

    """
    )


    col1,col2,col3 = st.columns(3)


    with col1:

        st.info(
        """
        🤖

        ML Model

        Random Forest
        """
        )


    with col2:

        st.success(
        """
        📊

        Analytics

        Real-time Charts
        """
        )


    with col3:

        st.warning(
        """
        💾

        Database

        SQLite Storage
        """
        )


    st.divider()


    st.markdown(
    """
    ### How it works?

    1️⃣ Enter student details

    2️⃣ AI model predicts score

    3️⃣ Result is stored

    4️⃣ Dashboard shows insights


    ---


    Developed using:

    Python | Machine Learning | Streamlit | SQLite

    """
    )



# ---------------- DASHBOARD ---------------- #

elif menu == "📊 Dashboard":

    dashboard_page()



# ---------------- PREDICT ---------------- #

elif menu == "🤖 Predict":

    prediction_page()



# ---------------- HISTORY ---------------- #

elif menu == "📜 History":

    st.title("📜 Prediction History")


    conn = sqlite3.connect("students.db")


    try:

        df = pd.read_sql_query(
            "SELECT * FROM predictions",
            conn
        )


        if len(df) == 0:

            st.warning(
                "No predictions available yet."
            )


        else:


            # Metrics

            col1, col2, col3 = st.columns(3)


            with col1:

                st.metric(
                    "Total Predictions",
                    len(df)
                )


            with col2:

                st.metric(
                    "Average Score",
                    round(df["prediction"].mean(),2)
                )


            with col3:

                st.metric(
                    "Highest Score",
                    round(df["prediction"].max(),2)
                )



            st.divider()



            # Search

            st.subheader("🔍 Search Prediction")


            search = st.text_input(
                "Search by Gender"
            )


            if search:

                df = df[
                    df["gender"]
                    .str.contains(
                        search,
                        case=False
                    )
                ]



            st.subheader("📊 Prediction Records")


            st.dataframe(
                df,
                use_container_width=True
            )



            st.divider()



            # Download

            csv = df.to_csv(
                index=False
            )


            st.download_button(
                "⬇ Download Report",
                csv,
                "student_prediction_report.csv",
                "text/csv"
            )


    except Exception as e:

        st.error(
            "Database error"
        )


    conn.close()



# ---------------- ABOUT ---------------- #
elif menu == "👨‍💻 About":

    st.title("👨‍💻 About EduPredict AI")


    st.markdown(
    """
    ## 🎓 Student Performance Prediction System


    EduPredict AI is a Machine Learning based application
    that predicts student mathematics performance using
    academic and personal factors.


    The system helps analyze student performance patterns
    and provides AI-based insights for better understanding.


    """
    )


    st.divider()


    col1, col2 = st.columns(2)


    with col1:

        st.subheader("🚀 Project Features")


        st.write(
        """
        ✅ Student Performance Prediction

        ✅ Machine Learning Model

        ✅ Interactive Dashboard

        ✅ Prediction History

        ✅ Data Visualization

        ✅ SQLite Database Storage

        """
        )



    with col2:

        st.subheader("🛠 Technologies Used")


        st.write(
        """
        🐍 Python

        🤖 Machine Learning

        📊 Streamlit

        🗄 SQLite

        📈 Plotly

        🐼 Pandas

        """

        )



    st.divider()


    st.subheader("🧠 Machine Learning Model")


    st.info(
    """
    Algorithm Used:

    🌲 Random Forest Regression


    Why Random Forest?

    • Handles complex data patterns

    • Provides reliable predictions

    • Works well with mixed features

    """
    )


    st.divider()


    st.subheader("👩‍💻 Developer Information")


    st.success(
    """
    Developed by:

    Sindhu K

    Computer Science Engineering
    (Data Science)


    Project:
    Student Performance Prediction System

    """
    )


    st.caption(
        "Built with Python + Machine Learning + Streamlit 🚀"
    )


    st.title("👨‍💻 About EduPredict AI")


    st.markdown(
    """
    ## Student Performance Prediction System


    This project uses Machine Learning to predict
    student performance based on academic factors.


    ### Technologies Used:

    🐍 Python

    🤖 Machine Learning

    📊 Streamlit

    🗄 SQLite Database


    ### ML Algorithm:

    Random Forest Regression


    ### Project Goal:

    To help understand student performance
    using AI-based prediction and analytics.


    """
    )



# ---------------- LOGOUT ---------------- #

elif menu == "🚪 Logout":

    st.session_state.logged_in = False

    if "username" in st.session_state:
        del st.session_state["username"]

    st.success("Logged out successfully.")

    st.rerun()