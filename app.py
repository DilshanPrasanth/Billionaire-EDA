import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('Billionaires Statistics Dataset.csv')

# Sidebar
st.sidebar.title("Filters")
selected_category = st.sidebar.selectbox("Select Category", df['category'].unique())
selected_country = st.sidebar.selectbox("Select Country", df['country'].unique())

# Filter the data based on user selection
filtered_data = df[(df['category'] == selected_category) & (df['country'] == selected_country)]

# Main content
st.title("Billionaires Data Visualization")

# Display filtered data
st.write(f"Showing data for {selected_category} in {selected_country}")
st.dataframe(filtered_data)

# Bar chart for Final Worth
st.header("Bar Chart - Final Worth")
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['personName'], filtered_data['finalWorth'], color='skyblue')
plt.xlabel('Person Name')
plt.ylabel('Final Worth (in Billions)')
plt.title('Final Worth of Individuals')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
st.pyplot(plt)

# Scatter plot for Age vs Final Worth
st.header("Scatter Plot - Age vs Final Worth")
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['age'], filtered_data['finalWorth'], color='green', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Final Worth (in Billions)')
plt.title('Age vs Final Worth')
st.pyplot(plt)
