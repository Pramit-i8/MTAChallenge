import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('path_to_your_merged_data.csv')

data = load_data()

# Sidebar filter
st.sidebar.header("Filter by Year")
selected_year = st.sidebar.selectbox('Select Year', data['Month'].dt.year.unique())
filtered_data = data[data['Month'].dt.year == selected_year]

# Correlation and Scatter Plots
st.title("MTA Ridership, Safety, and Weather Analysis")

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

# Recommendations
st.subheader("Insights and Recommendations")
st.write("""
- **Bus Collisions**: Increase safety measures during rainy periods.
- **Ridership**: Ridership is resilient, with minimal impact from precipitation.
- **Subway Accidents**: Consider flood mitigation in vulnerable stations.
""")

# Explanatory Text
st.write("""
### Understanding the Correlation
- **Positive Correlation**: Precipitation increases the variable.
- **Negative Correlation**: Precipitation decreases the variable.
- **Weak Correlation**: Little to no relationship.
""")