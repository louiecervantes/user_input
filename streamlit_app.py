#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]

def ask_question(question):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

# Define the Streamlit app
def app():
    st.header("Welcome to Basic User Input App")
    st.subheader("Louie F. Cervantes M.Eng. \n(c) 2023 WVSU College of ICT")
    
    st.title("Read the User Input and Process")
    
    # Get the user input
    user_input = st.text_input("Enter a value: ")
    
    # Add a button to update the data
    if st.button("Process Input"):
        question = user_input
        answer = ask_question(question)
        st.write(answer)

# Run the app
if __name__ == "__main__":
    app()
