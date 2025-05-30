import os
import pickle
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from transformers import pipeline

# Define the Gmail send scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Hugging Face Summarizer and Text Generator
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Use a better general-purpose text-to-text model for formal reply generation
text_generator = pipeline(
    "text2text-generation", 
    model="google/flan-t5-base", 
    tokenizer="google/flan-t5-base"
)


def authenticate_gmail():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=1696, host='127.0.0.1')

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def summarize_email(email_body):
    summary = summarizer(email_body, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def generate_reply(user_input):
    # Preprocess input: lowercase sloppy input
    cleaned_input = f"Paraphrase this professionally: {user_input.strip()}"

    response = text_generator(cleaned_input)[0]['generated_text']

    # Generate a subject using the first sentence
    subject_hint = response.split('.')[0]
    subject = subject_hint if len(subject_hint) > 10 else "Re: Your recent message"

    email = f"""**Subject:** {subject}

Dear [Recipient],

{response}

Sincerely,  
[Your Name]
"""
    return email


def send_email(service, message_body, subject, recipient):
    try:
        message = MIMEText(message_body)
        message['to'] = recipient
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        send_message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
        print(f"✅ Message sent successfully! ID: {send_message['id']}")
    except Exception as e:
        print(f"❌ An error occurred while sending the email: {e}")
