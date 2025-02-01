import streamlit as st
from src.inference import generate_code

# Streamlit UI
st.title("CodeLlama Code Generator")
st.write("Automatically generate code using Meta's CodeLlama model.")

# Input prompt
prompt = st.text_area("Enter your code generation prompt:", height=150)

# Generate code on button click
if st.button("Generate Code"):
    if prompt:
        with st.spinner("Generating code..."):
            generated_code = generate_code(prompt)
            st.code(generated_code, language="python")
    else:
        st.warning("Please enter a prompt.")