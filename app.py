import streamlit as st

st.title("KnowledgeHub AI")

question = st.text_input("Ask a Question")

if st.button("Search"):
    st.write("Your answer here")