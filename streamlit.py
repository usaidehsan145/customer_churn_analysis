import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained logistic regression model and scaler
with open('/home/usaid/ChurnAnalysis/model.pkl', 'rb') as file:
    saved_data = joblib.load(file)
    loaded_model = saved_data['model']
    loaded_scaler = saved_data['scaler']

st.title("Customer Churn Analysis")

tenure = st.slider("Tenure (years)", 0, 32, 16)

preferredLoginT = st.radio("Preferred Login Device", ['Mobile Phone', 'Computer'])
if preferredLoginT == 'Mobile Phone':
    preferredLogin = 1
else:
    preferredLogin = 0

city = st.radio("City Tier", [1, 2, 3])
warehouse = st.slider("Distance to Warehouse (km)", 0.0, 40.0, 20.0)

paymentmethod = st.radio("Select Payment Method", ["Cash on Delivery", "Debit Card", "Credit Card", "E wallet", "UPI"])
if paymentmethod == "Cash on Delivery":
    cashondel = 1
    debitcard = 0
    creditcard = 0
    ewallet = 0
    upi = 0

elif paymentmethod == "Debit Card":
    cashondel = 0
    debitcard = 1
    creditcard = 0
    ewallet = 0
    upi = 0
  
elif paymentmethod == "Credit Card":
    cashondel = 0
    debitcard = 0
    creditcard = 1
    ewallet = 0
    upi = 0

elif paymentmethod == "E wallet":
    cashondel = 0
    debitcard = 0
    creditcard = 0
    ewallet = 1
    upi = 0
    
else:
    cashondel = 0
    debitcard = 0
    creditcard = 0
    ewallet = 0
    upi = 1

genderT = st.radio("Select Gender", ['Female', 'Male'])

if genderT == 'Female':
  gender = 0
else:
  gender = 1

hourspend = st.slider("Hours Spent on App", 1, 5, 3)
deviceReg = st.slider("Number of Devices Registered", 1, 5, 2)

orderCatT = st.radio("Preferred Order Category", ["Laptop & Accessory", "Mobile", "Fashion"])
if orderCatT == "Laptop & Accessory":
    laptop = 1
    mobile = 0
    fashion = 0
elif orderCatT == "Mobile":
    laptop = 0
    mobile = 1
    fashion = 0
else:
    laptop = 0
    mobile = 0
    fashion = 1

satisfaction = st.slider("Satisfaction Score", 1, 5, 3)

maritalT = st.radio("Marital Status", ['Single', 'Divorced', 'Married'])
if maritalT == 'Single':
    marital = 0
elif maritalT == 'Divorced':
    marial = 1
else:
    marital = 2

totalAddresses = st.slider("Number of Addresses", 1, 12, 6)

complainT = st.radio("Customer Has Complaint", ["Yes", "No"])
if complainT == "Yes":
    complain = 1
else:
    complain = 0

Orderhike = st.slider("Order Amount Hike (%) from Last Year", 1, 30, 15)
coupon = st.slider("Total Number of Coupons Used", 0, 5, 2)
orderCount = st.slider("Total Number of Orders Placed since last month", 0, 5, 2)
daysSince = st.slider("Days Since Last Order", 0, 30, 15)
cashback = st.slider("Cashback Amount", 0.0, 100.0, 50.0)


data_frame = {
  'Tenure': [tenure],
  'PreferredLoginDevice': [preferredLogin],
  'CityTier': [city],
  'WarehouseToHome': [warehouse],
  'Gender': [gender],
  'HourSpendOnApp': [hourspend],
  'NumberOfDeviceRegistered': [deviceReg],
  'SatisfactionScore': [satisfaction],
  'MaritalStatus': [marital], 
  'NumberOfAddress': [totalAddresses], 
  'Complain': [complain],
  'OrderAmountHikeFromlastYear': [Orderhike], 
  'CouponUsed': [coupon], 
  'OrderCount': [orderCount],
  'DaySinceLastOrder': [daysSince], 
  'CashbackAmount': [cashback], 
  ' Mode_Cash on Delivery': [cashondel],
  ' Mode_Credit Card': [creditcard], 
  ' Mode_Debit Card': [debitcard], 
  ' Mode_E wallet': [ewallet], 
  ' Mode_UPI': [upi],
  ' Cat_Fashion': [fashion], 
  ' Cat_Laptop & Accessory': [laptop], 
  ' Cat_Mobile': [mobile]
}

df = pd.DataFrame(data_frame)

# Standardize the user input using Min-Max Scaling
user_input_standardized = loaded_scaler.transform(df)

# Make prediction using the loaded model
prediction = loaded_model.predict(user_input_standardized)[0]

# Display the prediction result
st.subheader("Prediction Result:")

if st.button("Predict", key="predict_button"):
    if prediction == 0:
        st.write("The customer is predicted to NOT churn.")
    else:
        st.write("The customer is predicted to churn.")




