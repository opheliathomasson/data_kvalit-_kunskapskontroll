import streamlit as st

from rag.load_vector_db import load_vector_store
from rag.retriever import retrieve_context
from rag.prompt import generate_answer


st.set_page_config(
    page_title="The Wise Wizard",
    page_icon="🧙‍♂️"
)

st.title("🧙‍♂️ The Wise Wizard's Library ✨")

st.write(
    "Ask questions about the wizarding world.\n\n"
    "The old wizard searches through ancient books, magical records, "
    "and forgotten scrolls to uncover the answers you seek."
)

if st.button("🪄 Cast Obliviate"):
    st.session_state.messages = []
    st.rerun()


@st.cache_resource
def initialize_vector_store():
    return load_vector_store()


try:
    vector_store = initialize_vector_store()
except Exception as e:
    st.error(f"🧙‍♂️ The ancient archives could not be opened.\n\n"
        f"Magical error:  {e}")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_question := st.chat_input(
    "What secrets of the wizarding world do you seek?"
):
    
    with st.chat_message("user", avatar="🪄"):
        st.markdown(user_question)

    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("assistant", avatar="🧙‍♂️"):
        with st.spinner("The wizard searches through ancient scrolls..."):
            
            context, results = retrieve_context(
                vector_store,
                user_question,
                k=3
            )

            answer = generate_answer(user_question, context)

            st.markdown(answer)

            with st.expander("Show retrieved context"):
                for result in results:
                    st.write(result.metadata)
                    st.write(result.page_content[:1000])
                    st.write("---")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )