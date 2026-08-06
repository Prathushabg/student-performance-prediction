import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


def dashboard_page():

    st.title("📊 Student Performance Analytics")


    # Database connection
    conn = sqlite3.connect("students.db")

    df = pd.read_sql_query(
        "SELECT * FROM predictions",
        conn
    )

    conn.close()


    if df.empty:

        st.warning("No predictions available yet.")

        return


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


    # Score Distribution

    st.subheader("📈 Prediction Score Distribution")


    fig1 = px.histogram(
        df,
        x="prediction",
        nbins=10,
        title="Student Score Distribution"
    )


    st.plotly_chart(
        fig1,
        use_container_width=True
    )



    # Reading vs Writing


    st.subheader("📚 Reading vs Writing Performance")


    fig2 = px.scatter(
        df,
        x="reading",
        y="writing",
        size="prediction",
        color="prediction",
        title="Reading and Writing Score Relationship"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



    # Gender Analysis


    st.subheader("👥 Gender Based Analysis")


    gender_data = (
        df.groupby("gender")["prediction"]
        .mean()
        .reset_index()
    )


    fig3 = px.bar(
        gender_data,
        x="gender",
        y="prediction",
        title="Average Prediction Score by Gender"
    )


    st.plotly_chart(
        fig3,
        use_container_width=True
    )


    # History Table

    st.subheader("📜 Prediction History")


    st.dataframe(
        df,
        use_container_width=True
    )


    # Download option


    csv = df.to_csv(index=False)


    st.download_button(
        "⬇ Download Report",
        csv,
        "student_predictions.csv",
        "text/csv"
    )