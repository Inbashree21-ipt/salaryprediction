import streamlit as st
import pickle
import numpy as np

# 1. Setup the Web App Title and Description
st.title("Salary Prediction App 💰")
st.write("Enter your years of experience to predict the estimated salary.")

# 2. Load the trained model
# Note: The filename must match exactly what you uploaded to GitHub
filename = 'linear_regression_model(2).pkl'

try:
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Error: The file '{filename}' was not found.")
    st.info("Please make sure you uploaded 'linear_regression_model(2).pkl' to your GitHub repository.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.info("This is usually caused by a version mismatch. Check your requirements.txt.")
    st.stop()

# 3. Create Input Field
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
        # The model expects a 2D array like [[5.5]]
        input_data = np.array([[years_experience]])
        
        # Make prediction
        prediction = loaded_model.predict(input_data)
        
        # Display result
        salary = prediction[0]
        st.success(f"The predicted salary for {years_experience} years of experience is: ${salary:,.2f}")
    except Exception as e:
        st.error(f"Prediction Error: {e}")
