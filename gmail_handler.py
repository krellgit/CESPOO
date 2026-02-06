"""Gmail API handler for reading and sending emails"""
import base64
import os.path
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import config


class GmailHandler:
    def __init__(self):
        self.service = None
        self.authenticate()

    def authenticate(self):
        """Authenticate with Gmail API using OAuth 2.0"""
        creds = None

        # token.json stores the user's access and refresh tokens
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', config.SCOPES)

        # If there are no (valid) credentials available, let the user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists('credentials.json'):
                    raise FileNotFoundError(
                        "credentials.json not found. Please download OAuth 2.0 credentials "
                        "from Google Cloud Console."
                    )
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', config.SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build('gmail', 'v1', credentials=creds)

    def get_emails(self, hours_back=24, unread_only=True):
        """
        Retrieve emails from the past N hours

        Args:
            hours_back: How many hours back to search
            unread_only: If True, only get unread emails

        Returns:
            List of email dictionaries with subject, sender, body, date
        """
        try:
            # Calculate the timestamp for N hours ago
            time_ago = datetime.now() - timedelta(hours=hours_back)
            after_timestamp = int(time_ago.timestamp())

            # Build the query
            query = f'after:{after_timestamp}'
            if unread_only:
                query += ' is:unread'

            # Get message IDs
            results = self.service.users().messages().list(
                userId='me',
                q=query,
                maxResults=500
            ).execute()

            messages = results.get('messages', [])

            if not messages:
                print("No messages found.")
                return []

            # Fetch full message details
            emails = []
            for message in messages:
                msg = self.service.users().messages().get(
                    userId='me',
                    id=message['id'],
                    format='full'
                ).execute()

                email_data = self._parse_email(msg)
                emails.append(email_data)

            return emails

        except HttpError as error:
            print(f'An error occurred: {error}')
            return []

    def _parse_email(self, message):
        """Parse Gmail API message into readable format"""
        headers = message['payload']['headers']

        # Extract headers
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
        date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown')

        # Extract body
        body = self._get_email_body(message['payload'])

        return {
            'id': message['id'],
            'subject': subject,
            'sender': sender,
            'date': date,
            'body': body
        }

    def _get_email_body(self, payload):
        """Extract email body from payload"""
        if 'parts' in payload:
            parts = payload['parts']
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    data = part['body'].get('data', '')
                    if data:
                        return base64.urlsafe_b64decode(data).decode('utf-8')
                elif 'parts' in part:
                    # Recursive for nested parts
                    return self._get_email_body(part)
        else:
            data = payload['body'].get('data', '')
            if data:
                return base64.urlsafe_b64decode(data).decode('utf-8')

        return ''

    def send_email(self, to, subject, body):
        """
        Send an email

        Args:
            to: Recipient email address
            subject: Email subject
            body: Email body (can be HTML)
        """
        try:
            message = MIMEText(body, 'html')
            message['to'] = to
            message['subject'] = subject

            raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
            send_message = {'raw': raw}

            self.service.users().messages().send(
                userId='me',
                body=send_message
            ).execute()

            print(f"Email sent to {to}")
            return True

        except HttpError as error:
            print(f'An error occurred: {error}')
            return False
