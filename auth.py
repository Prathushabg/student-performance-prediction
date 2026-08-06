import streamlit as st


# ---------------- USER CREDENTIALS ---------------- #

USERS = {
    "admin": "1234",
    "sindhu": "sindhu123"
}


# ---------------- LOGIN PAGE ---------------- #

def login():

    st.markdown(
        """
        <style>

        .login-box{
            background:white;
            padding:40px;
            border-radius:20px;
            box-shadow:0px 8px 20px rgba(0,0,0,0.15);
            text-align:center;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown(
            """
            <div class="login-box">

            <h1>🎓 EduPredict AI</h1>

            <h4>Student Performance Prediction System</h4>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        username = st.text_input(
            "👤 Username"
        )

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        remember = st.checkbox("Remember Me")

        login_btn = st.button(
            "Login"
        )

        if login_btn:

            if username in USERS and USERS[username] == password:

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Login Successful ✅")

                st.rerun()

            else:

                st.error("Invalid Username or Password ❌")