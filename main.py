import streamlit as st
import pandas as pd

st.write("**Take Me Home, Country Roads**")

st.write("John Denver's words **impacted millions**. Now it's time for it to impact you - where is your home, country roads?")

st.write("With our app, you can find just that.")

#reading all CSV files
cities = pd.read_csv('cities.csv')
CoL = pd.read_csv('movehubcostofliving.csv')
QoL = pd.read_csv('movehubqualityoflife.csv')
prices = pd.read_csv('price.csv')
pricesSQFT = pd.read_csv('pricepersqft.csv')




st.write(cities)
st.write(CoL)
st.write(QoL)
st.write(prices)
st.write(pricesSQFT)