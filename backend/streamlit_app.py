import streamlit as st
import requests
import json

st.set_page_config(page_title="Emotion-Based Music Recommender", layout="wide")

st.title("🎵 Emotion-Based Music Recommender")
st.write("Detect emotions from text and get personalized music recommendations!")

# Input section
col1, col2 = st.columns([3, 1])

with col1:
    user_text = st.text_area(
        "Enter your text:",
        placeholder="How are you feeling today? Share your thoughts or emotions...",
        height=100
    )

with col2:
    st.write("")
    st.write("")
    predict_button = st.button("🎧 Get Recommendations", use_container_width=True)

# Make API call when button is clicked
if predict_button and user_text:
    try:
        # Send request to Flask API
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"text": user_text},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            
            # Display detected emotion
            emotion = result.get("emotion", "unknown").upper()
            st.success(f"Detected Emotion: **{emotion}** 😊")
            
            # Display songs
            st.subheader("🎼 Recommended Songs:")
            songs = result.get("songs", [])
            
            if songs:
                for idx, song in enumerate(songs, 1):
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col1:
                        st.write(f"**{idx}.**")
                    with col2:
                        st.write(f"**{song['song']}** by *{song['artist']}*")
                    with col3:
                        st.write(f"*{song['mood']}*")
            else:
                st.warning("No songs found for this emotion.")
        else:
            st.error(f"API Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to the Flask API. Make sure the server is running on http://127.0.0.1:5000")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

elif predict_button and not user_text:
    st.warning("Please enter some text first!")

# Sidebar info
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This app detects the emotion in your text and recommends songs that match your mood.
    
    **How it works:**
    1. Enter your text or thoughts
    2. Click 'Get Recommendations'
    3. View your detected emotion
    4. Enjoy the recommended songs!
    """)
    
    st.header("📊 Emotions Supported")
    st.write("""
    - 😊 Happy
    - 😢 Sad
    - 😠 Angry
    - 😐 Neutral
    """)
