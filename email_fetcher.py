from base64 import urlsafe_b64decode
from bs4 import BeautifulSoup
from transformers import pipeline

# Hugging Face pipelines
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
reply_generator = pipeline("text-generation", model="gpt2")

def get_unread_emails(service, max_results=5):
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread', maxResults=max_results).execute()
    messages = results.get('messages', [])

    emails = []

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        payload = msg['payload']
        headers = payload.get('headers', [])

        email_data = {
            'from': '',
            'subject': '',
            'body': '',
            'summary': '',
            'generated_reply': ''
        }

        for header in headers:
            if header['name'] == 'From':
                email_data['from'] = header['value']
            if header['name'] == 'Subject':
                email_data['subject'] = header['value']

        # Decode email body
        body = ""
        parts = payload.get('parts')
        if parts:
            for part in parts:
                data = part['body'].get('data')
                if data:
                    decoded_data = urlsafe_b64decode(data).decode('utf-8', errors='ignore')
                    soup = BeautifulSoup(decoded_data, 'html.parser')
                    body += soup.get_text()
        else:
            body_data = payload['body'].get('data')
            if body_data:
                decoded_data = urlsafe_b64decode(body_data).decode('utf-8', errors='ignore')
                soup = BeautifulSoup(decoded_data, 'html.parser')
                body = soup.get_text()

        email_data['body'] = body.strip()

        # Generate summary
        if body:
            try:
                summary = summarizer(body[:1000], max_length=100, min_length=30, do_sample=False)[0]['summary_text']
                email_data['summary'] = summary
            except Exception as e:
                email_data['summary'] = f"Summarization failed: {e}"

        # Placeholder: Ask user for raw reply input
        raw_reply = "thank you"  # Replace with user input via frontend later

        # Generate formal reply
        if raw_reply:
            try:
                reply = reply_generator(f"Reply to this email: {raw_reply}", max_length=100, num_return_sequences=1)[0]['generated_text']
                email_data['generated_reply'] = reply
            except Exception as e:
                email_data['generated_reply'] = f"Reply generation failed: {e}"

        emails.append(email_data)

    return emails
