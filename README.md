# Used Mobile Phone Price Predictor

This repository contains a machine learning model and a Streamlit web application for predicting the prices of used mobile phones. The model is trained on historical data from ebay and can estimate the market value of a used phone based on various features.

## Features

The model takes into account various attributes of a mobile phone, including:

- Amazon Price
- Brand
- RAM
- Storage Capacity
- Year of Release
- Network Status
- Screen Size
- Operating System
- And more...

## Model Training

The model training process is documented in the Jupyter notebook `train_model.ipynb`. The notebook includes data preprocessing, feature engineering, model selection, training, and evaluation. The final model with 0.8 of R^2 is saved and used in the Streamlit application for real-time predictions.

## Web Application

The web application is built using Streamlit, allowing users to input phone characteristics and receive price predictions instantly. It's designed to be user-friendly and accessible for both technical and non-technical users.

Webapp link:
<https://device-price-vgdhwcv5prxaawbbydhwh3.streamlit.app/>

### Running the Application

To run the application locally:

1. Ensure you have Python installed on your system.
2. Clone this repository.
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   
## Data Visualization

Below is a glimpse of the data used for training the model:

Figure 1: Data Distribution by Year
<img width="579" alt="year" src="https://github.com/li2244646433/device-price/assets/154277499/5f669b3a-0348-481d-8cfd-745a08ee5371">

Figure 2: Data Distribution by Brand
<img width="643" alt="brand" src="https://github.com/li2244646433/device-price/assets/154277499/49700fa3-c3b7-4c3b-a2b9-aa982262798b">


