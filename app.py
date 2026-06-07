import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Dashboard")

url = "https://raw.githubusercontent.com/AP-State-Skill-Development-Corporation/Datasets/master/Data%20Analysis/Advertising.csv"

df = pd.read_csv(url)

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("TV Advertisement Spending")
fig1 = px.histogram(df, x="TV", title="TV Advertisement Spending")
st.plotly_chart(fig1)

st.subheader("TV vs Sales")
fig2 = px.scatter(df, x="TV", y="sales", title="TV vs Sales")
st.plotly_chart(fig2)

st.subheader("Summary Statistics")
st.write(df.describe())