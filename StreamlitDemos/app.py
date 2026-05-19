import streamlit as st
import pandas as pd
from datetime import time

# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="Streamlit Demos", layout="centered")

st.title("My First Streamlit App")

# =========================
# 2.1 BASIC INPUT COMPONENTS
# =========================
st.header("2.1 Basic Input Components")

st.subheader("Text Input Example")
name = st.text_input("What's your name?", "Type here...")
if name and name != "Type here...":
    st.write(f"Hello {name}!")

st.subheader("Password Input")
password = st.text_input("Enter password", type="password")
if password:
    st.write("Password received (hidden)")

st.subheader("Number Input Example")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old")

st.subheader("Button Example")
if st.button("Click me!"):
    st.success("Button was clicked!")
else:
    st.info("Button hasn't been clicked yet")

# =========================
# 2.2 SELECTION COMPONENTS
# =========================
st.header("2.2 Selection Components")

st.subheader("Slider Examples")
number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You picked: {number}")

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45))
)
st.write("Your appointment:", appointment)

st.subheader("Checkbox Example")
show = st.checkbox("Show/Hide Text")
if show:
    st.write("You can see this text!")

st.subheader("Selection Examples")

favorite_color = st.radio(
    "What's your favorite color?",
    ["Red", "Green", "Blue"]
)
st.write(f"Your favorite color is {favorite_color}")

activity = st.selectbox(
    "What are you doing?",
    ["Eating", "Sleeping", "Coding"]
)
st.write(f"You are {activity}")

# =========================
# 3. DISPLAY DATA
# =========================
st.header("3. Displaying Data")

st.subheader("Text Display Examples")

st.write("Normal text with st.write()")
st.write("You can write multiple arguments")

st.markdown("### This is a heading")
st.markdown("**Bold text** and *italic text*")
st.markdown("- Bullet point 1\n- Bullet point 2")

st.subheader("Data Structure Examples")

my_list = ["apple", "banana", "orange"]
st.write("List:", my_list)

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
st.write("Dictionary:", my_dict)

df = pd.DataFrame({
    "Name": ["John", "Anna", "Peter"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

st.write("Simple table:")
st.table(df)

st.write("Interactive dataframe:")
st.dataframe(df)

st.subheader("File Uploader Example")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    st.write("File uploaded successfully!")

# =========================
# 4. SESSION STATE
# =========================
st.header("Counter Example with Session State")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write("Count =", st.session_state.count)

# =========================
# 5. FORM
# =========================
st.header("Contact Form Example")

with st.form("contact_form"):
    name2 = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Thank you {name2}, we received your message!")