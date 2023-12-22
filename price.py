#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib
import streamlit as st
import pandas as pd
import numpy as np
#from streamlit_modal import Modal
import streamlit.components.v1 as components


# In[9]:


model = joblib.load('stack_model.joblib')


# In[10]:


def process_input_data(input_data):
    # Load the column names of the preprocessed DataFrame
    encoded_columns = joblib.load('X_columns.joblib')

    # Convert the input data (which could be a dictionary) into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Initialize a DataFrame with zeros for all columns saved in 'encoded_columns'
    # This ensures that the new DataFrame has the same structure as the training data
    processed_df = pd.DataFrame(columns=encoded_columns)
    processed_df.loc[0] = 0

    # Fill in the values for the columns present in the input data
    for col in input_df.columns:
        # If the column is numeric, just copy the value
        if col in processed_df.columns:
            processed_df[col] = input_df[col].values

        # If the column is categorical, set the corresponding one-hot encoded column to 1
        elif any(col in s for s in processed_df.columns):
            # Find the matching column name and set it to 1
            matching_column = [s for s in processed_df.columns if col in s][0]
            processed_df[matching_column] = 1

    return processed_df


# In[11]:


st.title('Used Mobile Phone Price Calculator')

# Creating input widgets for each feature
amazon_price = st.number_input('Price for Brand-new one', value = 699.00,min_value=0.0, format='%f')
Screen_Size = st.number_input('Screen Size (inches)', value = 6.0,min_value=0.0, format='%f')
RAM = st.number_input('RAM (GB)',value = 6, min_value=0, format='%d')
Storage_Capacity = st.number_input('Storage Capacity (GB)', value=64,min_value=0, format='%d')
YEAR = st.number_input('Year when the device model was released', min_value=2009, max_value=2023, step=1)
Condition = st.selectbox('Condition', options=['brand-new', 'open box_excellent', 'refurbished', 'used',
       'parts or not working', 'original box', 'unknown'])
Network = st.selectbox('Network', options=['unlocked', 'restricted', 'unknown'])
Lock_Status = st.selectbox('Lock Status', options=['unlocked', 'locked', 'unknown'])
Contract = st.selectbox('Contract', options=['Without Contract', 'unknown', 'Prepaid', 'With Contract',
       'Pay as go'])
Brand = st.selectbox('Brand', options=['samsung', 'apple', 'others', 'nokia', 'sony'])
Operating_system = st.selectbox('Operating System', options=['android', 'ios'])

# When the user clicks the predict button, process the input and make a prediction
if st.button('Press to Predict'):
    # Create a dictionary from the inputs
    input_data = {
        'amazon_price': amazon_price,
        'Screen Size':Screen_Size,
        'RAM': RAM,
        'Storage Capacity': Storage_Capacity,
        'YEAR': YEAR,
        # Append '_<category>' to the categorical inputs to match the One-Hot Encoded format
        f'Condition_{Condition}': 1,
        f'Network_{Network}': 1,
        f'Lock Status_{Lock_Status}': 1,
        f'Contract_{Contract}': 1,
        f'Brand_{Brand}': 1,
        f'Operating_System_{Operating_system}': 1
    }

    # Process the input data to match the trained model's format
    processed_data = process_input_data(input_data)

    # Make a prediction
    prediction = model.predict(processed_data)

    # Display the prediction
    #st.write(f"Predicted Amazon Price: ${prediction[0]:.2f}")
    st.markdown(f"<div class='big-font'>Estimated Price: ${prediction[0]:.2f}</div>", unsafe_allow_html=True)

# CSS to increase font size
st.markdown("""
<style>
.big-font {
    font-size:42px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
    


# In[ ]:





# In[ ]:




