import streamlit as st
import pickle
import numpy as np

# 1. Setup the Web App Title
st.title("Salary Prediction App 💰")
st.write("Enter your years of experience to predict the estimated salary.")

# 2. Load the trained model
# precise filename with the space
filename = 'linear_regression_model (2).pkl'

try:
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Error: The file '{filename}' was not found.")
    st.info(f"Make sure the file in your GitHub repo is named EXACTLY: '{filename}'")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# 3. Input Field
years_experience = st.number_input(
    "Years of Experience", 
    min_value=0.0, 
    max_value=50.0, 
    value=1.0, 
    step=0.1
)

# 4. Predict Button
if st.button("Predict Salary"):
    try:
        # Reshape data for the model
        input_data = np.array([[years_experience]])
        
        # Predict
        prediction = loaded_model.predict(input_data)
        
        # Display
        salary = prediction[0]
        st.success(f"The predicted salary for {years_experience} years of experience is: ${salary:,.2f}")
    except Exception as e:
        st.error(f"Prediction Error: {e}")
