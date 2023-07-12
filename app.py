from pathlib import Path
import pickle

import streamlit as st
import streamlit_authenticator as st_auth


user = ["John Doe", "Jane Doe"]
usernames = ["jd94", "princess_doe"] 

file_path = Path(__file__).parent / "hs_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = st_auth.Authenticate(user,usernames, hashed_passwords, "file_uploader", "a78fnei", cookie_expiry_days=10)
name, authentication_status, username = authenticator.login("Login", "main")
match authentication_status :
    case False:
        st.error("Username and/or password invalid")
    case None:
        st.warning("Please enter your username and password")
    case True:
        #file uploader goes here
        authenticator.logout("Logout", "sidebar")