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

# 3. **User Input Section in Grid**
st.subheader("User Input Widgets")

# Create grid structure (3 columns)
col1, col2, col3 = st.columns(3)

# Text input
with col1:
    name = st.text_input("What's your name?", "Guest")
    st.write(f"Hello, {name}!")

# Slider
with col2:
    age = st.slider("Select your age", 18, 100, 25)
    st.write(f"Your age is: {age}")

# Selectbox
with col3:
    color = st.selectbox("Pick a favorite color", ["Red", "Green", "Blue", "Yellow"])
    st.write(f"Your favorite color is: {color}")

# Checkbox
with col1:
    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.write("You have agreed!")

# Radio buttons
with col2:
    choice = st.radio("Choose your favorite animal", ["Cat", "Dog", "Bird"])
    st.write(f"Your favorite animal is: {choice}")

# File uploader
with col3:
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("File uploaded successfully!")
        st.dataframe(df.head())

# 4. **Data Visualization Section**
st.subheader("Data Visualization")

# Line chart
col1, col2 = st.columns(2)
with col1:
    st.write("### Line Chart Example")
    data = np.random.randn(100, 2)
    st.line_chart(data)

# Bar chart
with col2:
    st.write("### Bar Chart Example")
    data = {"Category A": 10, "Category B": 20, "Category C": 30}
    st.bar_chart(data)

# Matplotlib plot
col1, col2 = st.columns(2)
with col1:
    st.write("### Matplotlib Example")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
    st.pyplot(fig)

# Plotly plot
with col2:
    st.write("### Plotly Example")
    df_plotly = pd.DataFrame({
        "x": np.linspace(0, 10, 100),
        "y": np.sin(np.linspace(0, 10, 100))
    })
    fig = px.line(df_plotly, x="x", y="y", title="Plotly Line Chart")
    st.plotly_chart(fig)

# 5. **Layout Components Section**
st.subheader("Layout Components")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar where you can place widgets.")
sidebar_slider = st.sidebar.slider("Select a value in the sidebar", 0, 100, 50)
st.sidebar.write(f"You selected: {sidebar_slider}")

# Columns for displaying content side-by-side
col1, col2, col3 = st.columns(3)
with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")
with col3:
    st.write("This is column 3")

# Expander
with st.expander("See more info"):
    st.write("Here is some additional information inside an expander.")

# 6. **Progress and Spinner Section**
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

# 7. **Miscellaneous Section**
st.subheader("Miscellaneous")

# Balloons animation
st.balloons()

# 8. **Session State Example**
st.subheader("Session State Example")
if 'counter' not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.write(f"Counter: {st.session_state.counter}")

# 9. **Date Picker / Calendar**
st.subheader("Select a Date")

# Date input (Calendar)
selected_date = st.date_input("Pick a date")
st.write(f"You selected: {selected_date}")
