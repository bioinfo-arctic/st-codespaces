import subprocess
import streamlit as st
import streamlit_authenticator as st_auth
import yaml
from yaml.loader import SafeLoader

st.set_page_config("AutoReport")
with open('./hash_config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = st_auth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.title("AutoReport")
    st.subheader("Let's start to report!")
    st.text(f"Hello,{name}")
    up_file = st.file_uploader("Upload file", accept_multiple_files= True,type=["fastq","fastq.gz","txt"], help = "Upload all your necessary files")
    if st.button("Process"):
        if up_file:
            for file in up_file:
                st.write(type(file))
                st.write(dir(file))
                process = subprocess.Popen(f"sh ./test.sh {username}/temp/{file}", stdstdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
                print(process.stdout, process.stderr)
                #with open("temp_file", "wb") as f:
                #    f.write(up_file)
                    # Execute o script Bash com o arquivo como argumento
                #    result = subprocess.run(["./test.sh", "temp_file"], capture_output=True, text=True)
                    # Exiba a saída do script
                #    st.write(result.stdout)
    authenticator.logout("Logout", "sidebar")
elif authentication_status is False:
    st.error("Username and/or password invalid")
elif authentication_status is None:
    st.warning("Please enter your username and password")