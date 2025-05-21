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
df = pd.read_csv(f"data/{country_map[selected_country]}")

st.subheader(f"GHI Over Time in {selected_country}")
fig = px.line(df, x="Timestamp", y="GHI", title="Global Horizontal Irradiance")
st.plotly_chart(fig)

st.subheader("Summary Statistics")
st.write(df[["GHI", "DNI", "DHI"]].describe())
