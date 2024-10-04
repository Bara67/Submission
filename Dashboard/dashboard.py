import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('hour.csv')

st.title("Bike Sharing Dashboard")

avg_rentals_by_weather = data.groupby('weathersit')['cnt'].mean().reset_index()

st.subheader('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weathersit', y='cnt', data=avg_rentals_by_weather, ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Jumlah Penyewaan')
ax.set_xticks(np.arange(len(avg_rentals_by_weather['weathersit'])))
ax.set_xticklabels(['Clear', 'Mist + Cloudy', 'Light Snow/Rain', 'Heavy Rain/Snow'], rotation=45)
ax.grid(axis='y')
st.pyplot(fig)

rentals_by_hour = data.groupby('hr')['cnt'].sum().reset_index()

st.subheader('Total Penyewaan Sepeda Berdasarkan Jam')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=rentals_by_hour, marker='o', color='blue', ax=ax)
ax.set_title('Total Penyewaan Sepeda Berdasarkan Jam dalam Sehari')
ax.set_xlabel('Jam dalam Sehari')
ax.set_ylabel('Total Jumlah Penyewaan')
ax.set_xticks(np.arange(0, 24, step=1)) 
ax.grid()
st.pyplot(fig)
