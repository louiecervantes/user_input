#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

# Define the Streamlit app
def app():
    st.title("Read the User Input and Process")
    
    # Get the user input
    user_input = st.text_input("Enter a value: ")
    
    # Add a button to update the data
    if st.button("Update Data"):
        print('Input value = ', user_input)
        st.success("Data updated!")

# Run the app
if __name__ == "__main__":
    app()
