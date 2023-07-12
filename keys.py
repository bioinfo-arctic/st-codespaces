from pathlib import Path
import pickle

import streamlit as st
import streamlit_authenticator as st_auth

user = ["John Doe", "Jane Doe"]
usernames = ["jd94", "princess_doe"] 
passwords  =["qwert1234!@#$", "abc987/*-"]
hashed_passwords = st_auth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hs_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)