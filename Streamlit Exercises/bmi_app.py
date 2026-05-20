import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

st.title("🧮 BMI Calculator")
st.write("Calculate your body mass index (BMI) quickly and easily.✨")

st.divider()

col1, col2 = st.columns(2)

with col1:
    height = st.number_input("Height (meters)", min_value=0.0, step=0.01)

with col2:
    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

st.divider()

if st.button("Calculate BMI 🚀"):

    if height == 0:
        st.error("Please enter a valid height")
    else:
        bmi = weight / (height ** 2)

        st.markdown("### Result")

        st.success(f"Your BMI is **{bmi:.2f}**")

        if bmi < 18.5:
            st.info("🟡 Underweight")
        elif bmi < 25:
            st.success("🟢 Normal weight")
        elif bmi < 30:
            st.warning("🟠 Overweight")
        else:
            st.error("🔴 Obese")