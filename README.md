# Customer Churn Analysis

## Overview

This project focuses on predicting customer churn using a machine learning model. The analysis is based on a logistic regression model trained on historical customer data. The model predicts whether a customer is likely to churn or not based on various features such as tenure, preferred login device, payment method, satisfaction score, and more.

## Project Structure

The project is organized into the following components:

1. **Model Training**: The machine learning model is trained using logistic regression. The training process involves feature engineering, data preprocessing, and scaling.

2. **Streamlit App**: The Streamlit app serves as the user interface for interacting with the trained model. Users can input various customer features through sliders and dropdowns, and the app displays the predicted churn status.

3. **Data Processing**: Data processing involves transforming categorical features into numeric format, handling user inputs, and scaling the data using Min-Max scaling.

## Files and Directories

- `customerchurnanalysis.py`: Jupyter Notebook containing the model training process.
- `streamlit.py`: Streamlit app for user interaction and predictions.
- `model.pkl`: Pickled file containing the trained logistic regression model and scaler.
- 'E commerce Dataset.xlsx': Dataset file used for Logistic Regression Model Training
## Dependencies

- `streamlit`: For creating interactive web apps.
- `pandas`: For data manipulation and handling.
- `scikit-learn`: For machine learning modeling and preprocessing.

## Usage

1. **Model Training**: If you want to retrain the model, you can use the `model_training.ipynb` notebook.

2. **Streamlit App**: To run the Streamlit app, execute the following command in your terminal:

   ```bash
   streamlit run streamlit.py
