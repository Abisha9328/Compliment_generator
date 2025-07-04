# compliment_generator.py
import streamlit as st
import random

compliments = [
    "You have an amazing smile! 😊",
    "You light up the room! ✨",
    "You're a true friend. 🤝",
    "Your creativity knows no bounds! 🎨",
    "You are unstoppable! 🚀",
    "You make the world better. 🌍",
]

st.title("💖 Random Compliment Generator")

if st.button("Get a Compliment"):
    st.success(random.choice(compliments))
