import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("all_data.csv")

st.title("Analisis Data Bike Sharing")

st.header("1. Persentase Peningkatan/Penurunan Penyewaan Sepeda")
holiday_data = data[data['holiday'] == 1]
non_holiday_data = data[data['holiday'] == 0]

average_holiday_rentals = holiday_data['cnt'].mean()
average_non_holiday_rentals = non_holiday_data['cnt'].mean()
percentage_change = ((average_holiday_rentals - average_non_holiday_rentals) / average_non_holiday_rentals) * 100

st.write(f"Rata-rata penyewaan sepeda pada hari libur: {average_holiday_rentals:.2f}")
st.write(f"Rata-rata penyewaan sepeda pada hari biasa: {average_non_holiday_rentals:.2f}")
st.write(f"Persentase perubahan: {percentage_change:.2f}%")

labels = ['Holiday', 'Weekday']
averages = [average_holiday_rentals, average_non_holiday_rentals]

plt.figure(figsize=(8, 6))
plt.bar(labels, averages, color=['orange', 'blue'])
plt.title('Average Bike Rentals on Holidays vs Weekday', fontsize=16)
plt.ylabel('Average Bike Rentals', fontsize=12)
plt.xlabel('Day Type', fontsize=12)

for i, avg in enumerate(averages):
    plt.text(i, avg + 100, f'{avg:.2f}', ha='center', fontsize=12)

st.pyplot(plt)

st.header("2. Pengaruh Cuaca terhadap Penyewaan Sepeda")
avg_cnt_by_weather = data.groupby('weathersit')['cnt'].mean()

weather_conditions = {
    1: 'Clear or Partly Cloudy',
    2: 'Misty or Cloudy',
    3: 'Light Snow or Rain',
    4: 'Heavy Rain or Storm'
}

avg_cnt_by_weather.index = avg_cnt_by_weather.index.map(weather_conditions)

plt.figure(figsize=(8, 6))
plt.bar(avg_cnt_by_weather.index, avg_cnt_by_weather.values, color=['green', 'blue', 'orange', 'red'])
plt.title('Average Bike Rentals by Weather Condition', fontsize=16)
plt.xlabel('Weather Condition', fontsize=12)
plt.ylabel('Average Bike Rentals', fontsize=12)

for i, value in enumerate(avg_cnt_by_weather.values):
    plt.text(i, value + 50, f'{value:.2f}', ha='center', fontsize=12)

st.pyplot(plt)