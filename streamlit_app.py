import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import time

# Set page config
st.set_page_config(page_title="Streamlit Showcase", layout="wide")

# 1. **Title and Headers**
st.title("Streamlit Showcase App")
st.header("Most Commonly Used Streamlit Components")

# 2. **Text and Markdown Display**
st.markdown("This app demonstrates some of the most commonly used components in Streamlit.")

# 3. **Input Widgets**
st.subheader("User Input Widgets")

# Text input
name = st.text_input("What's your name?", "Guest")
st.write(f"Hello, {name}!")

# Slider
age = st.slider("Select your age", 18, 100, 25)
st.write(f"Your age is: {age}")

# Selectbox
color = st.selectbox("Pick a favorite color", ["Red", "Green", "Blue", "Yellow"])
st.write(f"Your favorite color is: {color}")

# Checkbox
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("You have agreed!")

# Radio buttons
choice = st.radio("Choose your favorite animal", ["Cat", "Dog", "Bird"])
st.write(f"Your favorite animal is: {choice}")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("File uploaded successfully!")
    st.dataframe(df.head())

# 4. **Data Visualization**
st.subheader("Data Visualization")

# Line chart
st.write("### Line Chart Example")
data = np.random.randn(100, 2)
st.line_chart(data)

# Bar chart
st.write("### Bar Chart Example")
data = {"Category A": 10, "Category B": 20, "Category C": 30}
st.bar_chart(data)

# Matplotlib plot
st.write("### Matplotlib Example")
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
st.pyplot(fig)

# Plotly plot
st.write("### Plotly Example")
df_plotly = pd.DataFrame({
    "x": np.linspace(0, 10, 100),
    "y": np.sin(np.linspace(0, 10, 100))
})
fig = px.line(df_plotly, x="x", y="y", title="Plotly Line Chart")
st.plotly_chart(fig)

# 5. **Layout Components**
st.subheader("Layout Components")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar where you can place widgets.")
sidebar_slider = st.sidebar.slider("Select a value in the sidebar", 0, 100, 50)
st.sidebar.write(f"You selected: {sidebar_slider}")

# Columns
col1, col2, col3 = st.columns(3)
col1.write("This is column 1")
col2.write("This is column 2")
col3.write("This is column 3")

# Expander
with st.expander("See more info"):
    st.write("Here is some additional information inside an expander.")

# 6. **Progress and Spinner**
st.subheader("Progress and Spinner")

# Progress bar
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i + 1)

# Spinner
with st.spinner("Loading..."):
    time.sleep(2)
st.success("Done!")

# 7. **Miscellaneous**
st.subheader("Miscellaneous")

# Balloons animation
st.balloons()

# 8. **Session State Example**
st.subheader("Session State Example")
if 'counter' not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.write(f"Counter: {st.session_state.counter}")

