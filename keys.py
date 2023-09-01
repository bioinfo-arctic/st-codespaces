import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as st_auth
import subprocess

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    for i in config['credentials']['usernames']:
        for j in config['credentials']['usernames'][i]:
            if j == 'password':
                config['credentials']['usernames'][i]['password'] = st_auth.Hasher([config['credentials']['usernames'][i][j]]).generate()

with open('./hash_config.yaml', 'w') as dump_file:
    yaml.dump(config, dump_file)
subprocess.call(['sh ./correct.sh'], shell=True)