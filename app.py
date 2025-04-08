import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('rf_model.pkl')
vectorizer = joblib.load('CountVector.pkl')

# Page config
st.set_page_config(page_title="SMS Spam Detector", page_icon="📱", layout="centered")

# Custom Header
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#4CAF50;">📱 SMS Spam Detector</h1>
        <p style="font-size:18px;">Easily check whether an SMS message is <strong style="color:red;">spam</strong> or <strong style="color:green;">safe</strong>.</p>
    </div>
    """, unsafe_allow_html=True
)

# Styling box
st.markdown(
    """
    <style>
    .stTextArea > div > textarea {
        font-size: 16px;
        height: 150px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 0.6em 1em;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Input Section
user_input = st.text_area("📩 Enter your SMS message below:")

if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        # Vectorize and predict
        message_vector = vectorizer.transform([user_input])
        prediction = model.predict(message_vector)[0]
        confidence = model.predict_proba(message_vector).max() * 100

        if prediction == 1:
            st.error(f"🚨 This message is likely **SPAM** with {confidence:.2f}% confidence.")
            st.markdown("**💡 Tip:** Avoid clicking on unknown links or replying to suspicious messages.")
        else:
            st.success(f"✅ This message appears to be **SAFE** with {confidence:.2f}% confidence.")
            st.markdown("**👍 You're good to go!**")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;font-size:14px;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
