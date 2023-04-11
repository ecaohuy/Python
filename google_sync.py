import os
import httplib2
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import pickle

# remove tokenfile

file_path = r'C:/Coding/Python/Codes/token.pickle'

try:
    os.remove(file_path)
    print(f"File '{file_path}' has been removed successfully.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"Error occurred while trying to remove file: {e}")

# Set the folder path and the name of the folder you want to create on Google Drive
local_folder_path =  r'C:\Personal'
drive_folder_name = ''

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_folder(drive_service, folder_name):
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=file_metadata, fields='id').execute()
    return folder['id']

def upload_files(drive_service, folder_id, folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_metadata = {
                'name': file,
                'parents': [folder_id]
            }
            media = MediaFileUpload(file_path, resumable=True)
            drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'File "{file}" uploaded.')

def main():
    try:
        credentials = get_credentials()
        service = build('drive', 'v3', credentials=credentials)

        folder_id = create_folder(service, drive_folder_name)
        print(f'Folder "{drive_folder_name}" created with ID "{folder_id}".')

        upload_files(service, folder_id, local_folder_path)

    except HttpError as error:
        print(f'An error occurred: {error}')
        print('Check if the credentials.json file is in the same folder as this script.')

if __name__ == '__main__':
    main()
