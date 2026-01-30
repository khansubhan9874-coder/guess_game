import streamlit as st
import random

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.title("🎯 Number Guessing Game")
st.write("Guess a number between **1 and 100**")

# Input from user
guess = st.number_input(
    "Enter a number:",
    min_value=1,
    max_value=100,
    step=1
)

# Check button
if st.button("Check"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.warning("Too Low ❌")
        elif guess > st.session_state.number:
            st.warning("Too High ❌")
        else:
            st.success(f"🎉 Shaan won!")
            st.info(f"Attempts: {st.session_state.attempts}")
            st.session_state.game_over = True

# Reset button
if st.button("Reset Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.success("Game reset! Guess again 😊")
