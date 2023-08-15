from pathlib import Path
import subprocess
import pickle
import streamlit as st
import streamlit_authenticator as st_auth
import yaml
from yaml.loader import SafeLoader

st.set_page_config("AutoReport")
with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = st_auth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == False:
    st.error("Username and/or password invalid")
elif authentication_status == None:
    st.warning("Please enter your username and password")
elif authentication_status == True:
    st.title("AutoReport")
    st.subheader("Let's start to report!")
    up_file = st.file_uploader("Upload file", accept_multiple_files= True, help = "Upload all your necessary files")
    if up_file is not None:
        ##process = subprocess.call("./test.sh", up_file)
        with open("temp_file", "wb") as f:
            f.write(up_file.getvalue())
            # Execute o script Bash com o arquivo como argumento
            result = subprocess.run(["./test.sh", "temp_file"], capture_output=True, text=True)
            # Exiba a saída do script
            st.write(result.stdout)
    authenticator.logout("Logout", "sidebar")