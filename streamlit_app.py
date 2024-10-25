import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset (ridership, safety, and weather data)
@st.cache
def load_data():
    # Add your merged dataset loading process here
    return pd.read_csv('Merged_Weather__Ridership__and_Safety_Data.csv')

data = load_data()

# Set up Streamlit 
st.title("MTA Ridership, Safety, and Weather Analysis")

# Visualization: Scatter Plot (Precipitation vs Ridership)
st.subheader("Impact of Precipitation on Ridership")
precip_ridership_corr = data[['Precipitation', 'Ridership']].corr().iloc[0, 1]
st.write(f"Correlation between Precipitation and Ridership: {precip_ridership_corr:.2f}")

# Plot the scatter plot
fig, ax = plt.subplots()
ax.scatter(data['Precipitation'], data['Ridership'], color='blue')
ax.set_title(f'Impact of Precipitation on Ridership (Correlation: {precip_ridership_corr:.2f})')
ax.set_xlabel('Total Monthly Precipitation (inches)')
ax.set_ylabel('Ridership')
st.pyplot(fig)

# Visualization: Scatter Plot (Precipitation vs Bus Collisions)
st.subheader("Impact of Precipitation on Bus Collisions")
bus_collision_corr = data[['Precipitation', 'Bus Collision Per Million Miles']].corr().iloc[0, 1]
st.write(f"Correlation between Precipitation and Bus Collisions: {bus_collision_corr:.2f}")

# Plot the scatter plot
fig, ax = plt.subplots()
ax.scatter(data['Precipitation'], data['Bus Collision Per Million Miles'], color='orange')
ax.set_title(f'Impact of Precipitation on Bus Collisions (Correlation: {bus_collision_corr:.2f})')
ax.set_xlabel('Total Monthly Precipitation (inches)')
ax.set_ylabel('Bus Collisions Per Million Miles')
st.pyplot(fig)

# Visualization: Scatter Plot (Precipitation vs Subway Customer Accidents)
st.subheader("Impact of Precipitation on Subway Customer Accidents")
subway_accident_corr = data[['Precipitation', 'Subway Customer Accidents']].corr().iloc[0, 1]
st.write(f"Correlation between Precipitation and Subway Customer Accidents: {subway_accident_corr:.2f}")

# Plot the scatter plot
fig, ax = plt.subplots()
ax.scatter(data['Precipitation'], data['Subway Customer Accidents'], color='red')
ax.set_title(f'Impact of Precipitation on Subway Customer Accidents (Correlation: {subway_accident_corr:.2f})')
ax.set_xlabel('Total Monthly Precipitation (inches)')
ax.set_ylabel('Subway Customer Accidents')
st.pyplot(fig)