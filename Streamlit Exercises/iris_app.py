import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")

model = joblib.load("iris_model.pkl")

st.title("🌸 Iris Flower Classifier")
st.write("Enter the measurements and identify the type of flower✨")

st.divider()

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("Sepal Length (cm)", step=0.1)
    petal_length = st.number_input("Petal Length (cm)", step=0.1)

with col2:
    sepal_width = st.number_input("Sepal Width (cm)", step=0.1)
    petal_width = st.number_input("Petal Width (cm)", step=0.1)

st.divider()

if st.button("Predict Species 🌿"):

    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)

    species = {
        0: "Setosa 🌱",
        1: "Versicolor 🌿",
        2: "Virginica 🌺"
    }

    st.markdown("### Prediction Result")

    st.success(f"Predicted Species: **{species[prediction[0]]}**")