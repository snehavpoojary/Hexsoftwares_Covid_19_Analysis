import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# LOAD DATASET
# ---------------------------
# Replace with your Kaggle dataset path
df = pd.read_csv("owid-covid-data.csv")

# Keep useful columns
df = df[['location','date','total_cases','new_cases','total_deaths','new_deaths',
         'people_vaccinated','people_fully_vaccinated','population']]
df['date'] = pd.to_datetime(df['date'])

# Drop rows without cases
df = df.dropna(subset=['total_cases'])

# ---------------------------
# USER INPUT: Choose country
# ---------------------------
country = input("Enter country name (e.g., India, United States): ")
country_data = df[df['location'] == country]

if country_data.empty:
    print(f"No data found for {country}. Please check spelling.")
    exit()

# ---------------------------
# ANALYSIS
# ---------------------------
print("\nBasic Info:")
print(f"Country: {country}")
print(f"Latest Total Cases: {country_data['total_cases'].max():,.0f}")
print(f"Latest Total Deaths: {country_data['total_deaths'].max():,.0f}")
print(f"Latest People Vaccinated: {country_data['people_vaccinated'].max():,.0f}")

# ---------------------------
# VISUALIZATION 1: Cases & Deaths Trend
# ---------------------------
plt.figure(figsize=(12,6))
plt.plot(country_data['date'], country_data['total_cases'], label="Total Cases", color='blue')
plt.plot(country_data['date'], country_data['total_deaths'], label="Total Deaths", color='red')
plt.title(f"Covid-19 Cases & Deaths in {country}")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.show()

# ---------------------------
# VISUALIZATION 2: Daily New Cases
# ---------------------------
plt.figure(figsize=(12,6))
plt.plot(country_data['date'], country_data['new_cases'], color='orange')
plt.title(f"Daily New Cases in {country}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()

# ---------------------------
# VISUALIZATION 3: Vaccination Progress
# ---------------------------
plt.figure(figsize=(12,6))
plt.plot(country_data['date'], country_data['people_vaccinated'], label="People Vaccinated", color='green')
plt.plot(country_data['date'], country_data['people_fully_vaccinated'], label="Fully Vaccinated", color='purple')
plt.title(f"Vaccination Progress in {country}")
plt.xlabel("Date")
plt.ylabel("People Vaccinated")
plt.legend()
plt.show()

# ---------------------------
# VISUALIZATION 4: Correlation Analysis
# ---------------------------
corr = country_data[['total_cases','total_deaths','people_vaccinated']].corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title(f"Correlation in {country} Data")
plt.show()

# ---------------------------
# EXTRA: Cases per Population (%)
# ---------------------------
latest = country_data.iloc[-1]
cases_per_pop = (latest['total_cases'] / latest['population']) * 100
print(f"\nPercentage of population infected in {country}: {cases_per_pop:.2f}%")
