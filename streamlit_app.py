import streamlit as st
import pandas as pd
import numpy as np

# Displaying title with customized text color and background
st.title("Streamlit Custom Theme Showcase")
st.write(
    "This app demonstrates how Streamlit's custom themes work using `.streamlit/config.toml`."
)

# Sample dataframe to visualize the background and text colors
data = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10)
})

st.write("Here’s a DataFrame with custom theme settings applied:")
st.dataframe(data)

# Displaying a button and some alert examples
st.button('Custom Styled Button')
st.success('This is a success alert with the custom success color!')
st.warning('This is a warning alert with the default color.')
st.error('This is an error alert.')

# Display some markdown with custom text color
st.markdown("""
    ### Custom Text Color Example
    This is some custom text displayed using the `textColor` property from the custom theme.
""")
