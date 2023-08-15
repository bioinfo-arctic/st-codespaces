import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as st_auth

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    hashed_passwords = st_auth.Hasher([config['credentials']['usernames']['jd94']['password'],config['credentials']['usernames']['princess_doe']['password']]).generate()
    config['credentials']['usernames']['jd94']['hashed_password'] = hashed_passwords[0]
    config['credentials']['usernames']['princess_doe']['hashed_password'] = hashed_passwords[1]
with open('./hash_config.yaml', 'w') as dump_file:
    yaml.dump(config, dump_file)