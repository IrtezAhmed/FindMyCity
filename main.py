import streamlit as st
import pandas as pd

st.write("**Take Me Home, Country Roads**")

st.write("John Denver's words **impacted millions**. Now it's time for it to impact you - where is your home, country roads?")

st.write("With our app, you can find just that.")

#reading all CSV files
cities = pd.read_csv('cities.csv').set_index('City')
CoL = pd.read_csv('movehubcostofliving.csv').set_index('City')
QoL = pd.read_csv('movehubqualityoflife.csv').set_index('City')
prices = pd.read_csv('price.csv').set_index('City')
pricesSQFT = pd.read_csv('pricepersqft.csv').set_index('City')

merged = QoL.join(cities).join(CoL).join(prices).join(pricesSQFT)

st.write(merged)