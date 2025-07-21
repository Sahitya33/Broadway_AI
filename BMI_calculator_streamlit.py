import streamlit as st
st.title("BMI Calculator")
weight = st.number_input("Enter your bodyweight in kg:")
height = st.number_input("Enter your height in feet:")

BMI_button =st.button('BMI')


if BMI_button:

    BMI= weight / (((height/3.28))**2)
    BMI=round(BMI,2)

    if BMI<16:
        st.error(f"Your BMI is {BMI}.You're extremely underweight")
    elif BMI>=16 and BMI<18.5:
        st.warning(f"Your BMI is {BMI}.You're underweight")
    elif BMI>=18.5 and BMI<25:
        st.success(f"Your BMI is {BMI}.You're healthy")
    elif BMI>=25 and BMI<30:
        st.info(f"Your BMI is {BMI}.You're overweight")
    elif BMI>=30:
        st.error(f"Your BMI is {BMI}.You're extrmely overweight")
