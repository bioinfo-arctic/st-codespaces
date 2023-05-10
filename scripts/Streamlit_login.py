import streamlit as st
import os
from file_visualizer import *

# Define a function to check if a user exists in a hypothetical user database
def authenticate(username, password):
    # In this example, we'll just hard-code a single username and password
    return username == "myusername" and password == "mypassword"

# Define the Streamlit app
def main():
    # Set the title and description
    st.sidebar.title("User Login")
    st.sidebar.write("Enter your username and password to log in.")

    # Create text input boxes for username and password
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Create a button to submit the form
    submitted = st.sidebar.button("Submit")

    # If the form is submitted, check if the user exists and display a message
    if submitted:
        if authenticate(username, password):
            st.markdown('## Start running your Bioinformatics Pipeline')
            st.write(f'Welcome {username}')
            visualizer()
        else:
            st.error("Invalid username or password.")

if __name__ == "__main__":
    main()
