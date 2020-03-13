from __future__ import print_function
import pickle
import os.path
import json

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from apiclient import errors

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
import os

from .models import User
from django.core.files import File
from django.core.files.base import ContentFile


SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def create_message(sender, to, subject, message_text):
       
    message = MIMEText(message_text, 'html')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(message['id'])
        return message
    except errors.HttpError as error:
        print(error)



@api_view(['POST',])
def google_api_send_email(request):
    
    id = request.data['id']
    message_text = request.data['body']
    message_subject = request.data['subject']
    message_recipients = request.data['recipients']

    creds = None
    
    if os.path.exists(f'accounts/pickles/pickle{id}'):
        with open(f'accounts/pickles/pickle{id}', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(f'accounts/pickles/pickle{id}', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    my_message = create_message('me', message_recipients, message_subject, message_text)
    send_message(service, 'me', my_message)
    return Response('sent')
    
    
    
    

    
    

    
    