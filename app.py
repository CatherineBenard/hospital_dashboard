import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("hospital_data.csv")

st.title("🏥 Hospital Operations Dashboard")

total_patients = df["Patient_ID"].count()
beds = df["Bed_Occupied"].sum()
avg_time = df["Treatment_Time"].mean()
success = df["Success"].mean() * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", total_patients)
col2.metric("Beds Occupied", beds)
col3.metric("Avg Treatment Time", round(avg_time, 2))
col4.metric("Success Rate %", round(success, 2))

st.divider()

st.subheader("Patients by Department")
st.plotly_chart(px.bar(df, x="Department", color="Department"))

st.subheader("Gender Distribution")
st.plotly_chart(px.pie(df, names="Gender"))

st.subheader("Treatment Success")
st.plotly_chart(px.histogram(df, x="Success", color="Department"))

st.dataframe(df)