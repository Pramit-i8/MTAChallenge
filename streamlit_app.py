import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('datasets/Merged_Weather__Ridership__and_Safety_Data.csv')

data = load_data()

# Convert 'Month' to datetime format
data['Month'] = pd.to_datetime(data['Month'], errors='coerce')


# Sidebar filter for selecting year
st.sidebar.header("Filter by Year")
selected_year = st.sidebar.selectbox('Select Year', data['Month'].dt.year.unique(), key='year_selectbox')

# Filter data based on selected year
filtered_data = data[data['Month'].dt.year == selected_year]

# Now continue with your plots and analysis using 'filtered_data'
st.title(f"MTA Ridership, Safety, and Weather Analysis for {selected_year}")

st.subheader(f"Impact of Precipitation on Ridership in {selected_year}")
precip_ridership_corr = filtered_data[['Precipitation', 'Ridership']].corr().iloc[0, 1]
st.write(f"Correlation between Precipitation and Ridership: {precip_ridership_corr:.2f}")
fig, ax = plt.subplots()
ax.scatter(filtered_data['Precipitation'], filtered_data['Ridership'], color='blue')
ax.set_title(f'Impact of Precipitation on Ridership (Correlation: {precip_ridership_corr:.2f})')
st.pyplot(fig)



# Time Series
st.subheader(f"Ridership and Precipitation Over Time in {selected_year}")
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(filtered_data['Month'], filtered_data['Ridership'], color='blue')
ax2.plot(filtered_data['Month'], filtered_data['Precipitation'], color='green')
st.pyplot(fig)


# New Section 2: Impact of Precipitation on Subway Customer Accidents
st.subheader("Impact of Precipitation on Subway Customer Accidents")

# Calculate correlation for Subway Customer Accidents
subway_accident_corr = filtered_data[['Precipitation', 'Subway Customer Accidents']].corr().iloc[0, 1]
st.write(f"Correlation between Precipitation and Subway Customer Accidents: {subway_accident_corr:.2f}")

# Plot for Subway Customer Accidents
fig, ax = plt.subplots()
ax.scatter(filtered_data['Precipitation'], filtered_data['Subway Customer Accidents'], color='red')
ax.set_title(f'Impact of Precipitation on Subway Customer Accidents (Correlation: {subway_accident_corr:.2f})')
ax.set_xlabel('Precipitation (inches)')
ax.set_ylabel('Subway Customer Accidents')
st.pyplot(fig)

# New Section 3: Impact of Precipitation on Bus Collisions
st.subheader("Impact of Precipitation on Bus Collisions")

# Calculate correlation for Bus Collisions
bus_collision_corr = filtered_data[['Precipitation', 'Bus Collision Per Million Miles']].corr().iloc[0, 1]
st.write(f"Correlation between Precipitation and Bus Collisions: {bus_collision_corr:.2f}")

# Plot for Bus Collisions
fig, ax = plt.subplots()
ax.scatter(filtered_data['Precipitation'], filtered_data['Bus Collision Per Million Miles'], color='orange')
ax.set_title(f'Impact of Precipitation on Bus Collisions (Correlation: {bus_collision_corr:.2f})')
ax.set_xlabel('Precipitation (inches)')
ax.set_ylabel('Bus Collisions Per Million Miles')
st.pyplot(fig)

# Allow users to download the filtered dataset
st.sidebar.download_button(
    label="Download filtered data",
    data=filtered_data.to_csv(index=False),
    file_name='filtered_data.csv',
    mime='text/csv'
)

# Recommendations
st.subheader("Insights and Recommendations")
st.write("""
- **Bus Collisions**: Increase safety measures during rainy periods.
- **Ridership**: Ridership is resilient, with minimal impact from precipitation.
- **Subway Accidents**: Consider flood mitigation in vulnerable stations.
""")