import streamlit as st

# Page configuration
st.set_page_config(page_title="Calculator by SUBHAN", page_icon="🧮")

# Title
st.title("🧮 Calculator")
st.subheader("Created by **SUBHAN**")

# Input numbers
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Cannot divide by zero")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"✅ Result: {result}")

# Footer
st.markdown("---")
st.markdown("👤 **SUBHAN Calculator App**")
