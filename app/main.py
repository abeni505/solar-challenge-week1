import streamlit as st
import pandas as pd
import plotly.express as px

st.title("☀️ Solar Data Dashboard")

country_map = {
    "Benin": "benin_clean.csv",
    "Sierra Leone": "sierra_leone_clean.csv",
    "Togo": "togo_clean.csv"
}

selected_country = st.selectbox("Choose a country", list(country_map.keys()))

# This lets users upload their own benin_clean.csv, sierra_leone_clean.csv
uploaded_file = st.file_uploader(f"Upload the cleaned CSV for {selected_country}", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
else:
    st.warning("Please upload a cleaned CSV file to continue.")

st.subheader(f"GHI Over Time in {selected_country}")
fig = px.line(df, x="Timestamp", y="GHI", title="Global Horizontal Irradiance")
st.plotly_chart(fig)

st.subheader("Summary Statistics")
st.write(df[["GHI", "DNI", "DHI"]].describe())
