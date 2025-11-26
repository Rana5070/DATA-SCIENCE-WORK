#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Pakwheels Car Dataset Analysis")

# Load Your Data
@st.cache_data
def load_data():
    df = pd.read_csv("pakwheels_cleaned.csv")   # change file name if different
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Add Filters
st.sidebar.header("Filters")

min_year, max_year = int(df['Model Year'].min()), int(df['Model Year'].max())
year = st.sidebar.slider("Select Model Year", min_year, max_year, (min_year, max_year))

filtered_df = df[(df['Model Year'] >= year[0]) & (df['Model Year'] <= year[1])]

st.write("Filtered Data")
st.dataframe(filtered_df)

# Plot Example
st.subheader("Price Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df["Price"].dropna())
st.pyplot(fig)
st.subheader("Correlation Heatmap")

num_col = ['Model Year', 'Price', 'Mileage', 'Engine Capacity']
# Compute correlation (pak = your DataFrame)
corr = df[num_col].corr()
# Create the heatmap
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)


# In[ ]:




