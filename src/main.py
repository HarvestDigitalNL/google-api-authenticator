import json
import sys
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

print('Creating google Consent Screen, might take a while...')

def get_script_folder():
    # path of main .py or .exe when converted with pyinstaller
    if getattr(sys, 'frozen', False):
        script_path = os.path.dirname(sys.executable)
    else:
        script_path = os.path.dirname(
            os.path.abspath(sys.modules['__main__'].__file__)
        )
    return script_path

# Adapt client_id/client_secret to environment
flow = InstalledAppFlow.from_client_config(
    {'installed': {
        'client_id': '',
        'client_secret': '',
        'redirect_uris': ["http://localhost:8080","http://localhost:8080/"],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token'
    }},
    scopes=['https://www.googleapis.com/auth/adwords']
)

print('Writing to ref-token.json located at: ', get_script_folder())

token_path = os.path.join(get_script_folder(), 'ref-token.json')

creds = flow.run_local_server(port=8080)
with open(token_path, 'w') as token:
    token.write(creds.to_json())
    print(json.dumps(creds.to_json(), indent=2))
