import streamlit as st
import pandas as pd
import plotly.express as px

st.title("☀️ Solar Data Dashboard")

# Google Drive direct download URLs for each country
country_map = {
    "Benin": "https://drive.google.com/uc?export=download&id=1agfPwNJAOc5nzWVnXt49-djmDshvdiI_",
    "Sierra Leone": "https://drive.google.com/uc?export=download&id=17YZErwPwjhEUUdfV6kPZRHFoSxMZHZ2-",
    "Togo": "https://drive.google.com/uc?export=download&id=1BpWrG_eKsAAnhmKMebA8iiM5xe79yyjY"
}

selected_country = st.selectbox("Choose a country", list(country_map.keys()))

@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data(country_map[selected_country])

if df is not None:
    st.write(df.head())

    st.subheader(f"GHI Over Time in {selected_country}")
    fig = px.line(df, x="Timestamp", y="GHI", title="Global Horizontal Irradiance")
    st.plotly_chart(fig)

    st.subheader("Summary Statistics")
    st.write(df[["GHI", "DNI", "DHI"]].describe())
else:
    st.warning("Data could not be loaded.")
