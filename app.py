import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("schools.csv")
df['total_score'] = df['average_math'] + df['average_reading'] + df['average_writing']

st.set_page_config(layout="wide")
st.title("NYC High Schools Performance Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Schools", len(df))
col2.metric("Avg Total Score", round(df['total_score'].mean(), 1))
col3.metric("Top School", df.loc[df['total_score'].idxmax(), 'school_name'])

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Average Total Score by Borough")
borough_avg = df.groupby('borough')['total_score'].mean().sort_values(ascending=False)
fig, ax = plt.subplots()
borough_avg.plot(kind='bar', ax=ax)
st.pyplot(fig)
st.subheader("Top 10 Schools by Total Score")
st.dataframe(df.nlargest(10, 'total_score')[['school_name', 'borough', 'total_score']])

st.subheader("Percent Tested vs Average Math Score")
fig2, ax2 = plt.subplots()
ax2.scatter(df['percent_tested'], df['average_math'])
ax2.set_xlabel('Percent Tested')
ax2.set_ylabel('Average Math Score')
st.pyplot(fig2)
st.subheader("Explore by Borough")
selected_borough = st.selectbox("Choose a borough", df['borough'].unique())
filtered_df = df[df['borough'] == selected_borough].sort_values('total_score', ascending=False)
st.dataframe(filtered_df[['school_name', 'total_score']])
