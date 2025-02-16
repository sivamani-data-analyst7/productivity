import streamlit as st
import pandas as pd

# Read your data (make sure it's in the same folder as your script or provide the path)
my_data = pd.read_csv("C:\\Users\\sikoppiset\\Downloads\\Book 5(Sheet1).csv", encoding='ISO-8859-1')
my_data['Date'] = pd.to_datetime(my_data['Date'], format='%d/%m/%Y')  # Convert 'Date' to datetime

# Streamlit app layout
st.title('Agent Performance Tracker')

# Input fields for Agent name and date range
agent_name = st.selectbox('Select Agent Name', my_data['Agent name'].unique())
start_date = st.date_input('Start Date', min_value=my_data['Date'].min())
end_date = st.date_input('End Date', min_value=start_date)

# Filter the data based on inputs
filtered_data = my_data[(my_data['Agent name'] == agent_name) & 
                        (my_data['Date'] >= pd.to_datetime(start_date))]

if end_date:
    filtered_data = filtered_data[filtered_data['Date'] <= pd.to_datetime(end_date)]

# Calculate 'Performance' column (whether the agent achieved the target)
filtered_data['Target Achieved'] = filtered_data['Processed Lots'] >= filtered_data['Target Lots']

# Displaying the result
if filtered_data.empty:
    st.write("No data available for the selected agent and date range.")
else:
    st.write(filtered_data[['Date', 'Queue', 'Processed Lots', 'Reasons', 'Target Achieved']])
    
    # Check if target was achieved for the entire period
    if filtered_data['Target Achieved'].all():
        st.success('Target Achieved!')
    else:
        st.warning('Target Not Achieved')
