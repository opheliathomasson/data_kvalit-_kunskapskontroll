import streamlit as st
from harry_potter_rag_pipeline import ask_question

# Page settings
st.set_page_config(
    page_title="Hogwarts Library",
    layout="centered"
)

# Simple safe styling
st.markdown("""
<style>

.stApp {
    background-color: #0b1020;
    color: #f5e6c8;
    font-family: Georgia, serif;
}

h1 {
    color: #d4af37;
    text-align: center;
}

/* Input field */
.stTextInput input {
    background-color: #1a1f2b;
    color: #f5e6c8;
    border: 1px solid #d4af37;
    border-radius: 8px;
}

/* Button */
.stButton button {
    background-color: #740001;
    color: white;
    border: 1px solid #d4af37;
    border-radius: 8px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #a00000;
    color: white;
}

/* Response boxes */
.response-box {
    background-color: #161b2e;
    border: 1px solid #d4af37;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("Hogwarts Library")

st.write("Consult the archives guided by an old and wise wizard.")

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

# Input
question = st.text_input("Ask the wizard")

# Buttons
if st.button("Consult the archives"):

    if question.strip():

        with st.spinner("Searching ancient scrolls..."):

            try:
                answer = ask_question(question)

            except Exception as e:
                answer = str(e)

        st.session_state.history.append(
            {"q": question, "a": answer}
        )

    else:
        st.warning("Write a question")


if st.button("Clear history"):
    st.session_state.history = []

# Chat history
for item in reversed(st.session_state.history):

    st.markdown(f"""
    <div class="response-box">

    <b>Question:</b><br>
    {item["q"]}

    <br><br>

    <b>Answer:</b><br>
    {item["a"]}

    </div>
    """, unsafe_allow_html=True)