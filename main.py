import streamlit as st
import pandas as pd

citiesCSV = pd.read_csv('cities.csv')
st.write(citiesCSV['City'])
