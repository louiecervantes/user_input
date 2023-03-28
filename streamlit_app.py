#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

# Define the Streamlit app
def app():
    st.header("Welcome to Basic User Input App")
    st.subheader("Louie F. Cervantes \nWVSU College of ICT")
    
    st.title("Read the User Input and Process")
    
    # Get the user input
    user_input = st.text_input("Enter a value: ")
    
    # Add a button to update the data
    if st.button("Process Input"):
        st.write("Input value = " + user_input)
        st.success("Input value = " + user_input)

# Run the app
if __name__ == "__main__":
    app()
