import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open("car_price_model (1).pkl", "rb"))

st.title("Car Price Predictor 🚗")

name = st.text_input("Car Name")
company = st.text_input("Company")
year = st.number_input("Year", min_value=1990, max_value=2024)
kms = st.number_input("KMs Driven")
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG"])

if st.button("Predict Price"):
    car = pd.DataFrame(
            [[name, company, int(year), int(kms), fuel]],
                    columns=["name", "company", "year", "kms_driven", "fuel_type"]
                        )
price = pipe.predict(car)[0]
st.success(f"Estimated Price: ₹{round(price)}")
