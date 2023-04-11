import os
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

local_folder_path = r'C:/Ericsson'
drive_folder_name = 'Ericsson'

SCOPES = ['https://www.googleapis.com/auth/drive']

def get_credentials():
    creds = None
    token_path = 'token.pickle'
    
    if os.path.exists(token_path) and os.path.getsize(token_path) > 0:
        try:
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)
        except (EOFError, pickle.UnpicklingError):
            print('Invalid token file. Please delete or fix the token.pickle file.')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_folder(drive_service, folder_name, parent_id=None):
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        file_metadata['parents'] = [parent_id]

    folder = drive_service.files().create(body=file_metadata, fields='id').execute()
    return folder['id']

def upload_files(drive_service, parent_id, folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            file_metadata = {
                'name': item,
                'parents': [parent_id]
            }
            media = MediaFileUpload(item_path, resumable=True)
            drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'File "{item}" uploaded.')

        elif os.path.isdir(item_path):
            folder_id = create_folder(drive_service, item, parent_id)
            print(f'Folder "{item}" created with ID "{folder_id}".')
            upload_files(drive_service, folder_id, item_path)

def main():
    try:
        credentials = get_credentials()
        service = build('drive', 'v3', credentials=credentials)

        root_folder_id = create_folder(service, drive_folder_name)
        print(f'Root folder "{drive_folder_name}" created with ID "{root_folder_id}".')

        upload_files(service, root_folder_id, local_folder_path)

    except HttpError as error:
        print(f'An error occurred: {error}')
        print('Check if the credentials.json file is in the same folder as this script.')

if __name__ == '__main__':
    main()
