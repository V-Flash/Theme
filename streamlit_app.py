import streamlit as st
import pandas as pd
import numpy as np

# Streamlit app title and description
st.title("My Custom-Themed Streamlit App")
st.write("This is a Streamlit app with a custom theme defined in config.toml")

# Example dataframe
df = pd.DataFrame({
    "A": np.random.rand(10),
    "B": np.random.rand(10),
})
st.write(df)
