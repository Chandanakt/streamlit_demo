import streamlit as st
import pandas as pd
import numpy as np

# --- Title & Intro ---
st.title("🚀 My First Streamlit App")
st.write("This is a simple demo of Streamlit features.")

# --- Text Input ---
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋")

# --- Slider ---
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"You are {age} years old.")

# --- Checkbox ---
if st.checkbox("Show random data"):
    data = pd.DataFrame(
        np.random.randn(10, 2),
        columns=["Column A", "Column B"]
    )
    st.write("Here’s a random dataframe:")
    st.dataframe(data)

    st.line_chart(data)

# --- Button ---
if st.button("Celebrate"):
    st.balloons()
