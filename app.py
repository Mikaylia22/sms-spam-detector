import streamlit as st
import joblib
import numpy as np

# Load the pre-trained models
rf_model = joblib.load('rf_model.pkl')  # Random Forest model for SMS spam detection
cv = joblib.load('CountVector.pkl')  # CountVectorizer used to transform SMS text

# Function to predict whether an SMS is spam or not
def predict_sms(text):
    # Transform the input SMS text using the CountVectorizer
    text_features = cv.transform([text])
    
    # Make prediction with the Random Forest model
    prediction = rf_model.predict(text_features)
    
    # Return prediction result
    return prediction[0]

# Function to explain why it's considered spam or not
def explain_prediction(result):
    if result == 1:
        return "This SMS contains certain keywords and patterns commonly associated with spam messages, such as unsolicited offers or requests for personal information."
    else:
        return "This SMS appears to be a legitimate message, as it lacks patterns or content typically found in spam messages."

# Streamlit UI
st.title("SMS Spam Filter")
st.markdown("""
    This app checks whether the provided SMS is spam or not. 
    Enter an SMS text and we will classify it for you.
""")

# Input SMS text from the user
sms_input = st.text_area("Enter SMS text here:")

# Add a button to start processing
if st.button("Check SMS"):
    if sms_input:
        # Process the SMS text when the button is clicked
        st.info("The model is processing your input to detect if it is spam or not...")
        
        # Make the prediction
        result = predict_sms(sms_input)
        
        # Display result
        if result == 1:
            st.warning("Warning: This SMS is detected as spam!")
        else:
            st.success("This SMS is not spam. It's safe!")
        
        # Explain why it's considered spam or not
        explanation = explain_prediction(result)
        st.write(f"**Explanation:** {explanation}")
        
        # Provide instructions for the user
        if result == 1:
            st.write("""
                **What to do next:**
                - You can ignore or block this SMS.
                - If you suspect this message is from a legitimate source, verify the information directly with the sender.
            """)
        else:
            st.write("""
                **What to do next:**
                - Feel free to engage with the sender.
                - If the message is important, you can save it for future reference.
            """)
    else:
        st.error("Please enter an SMS text to check.")
