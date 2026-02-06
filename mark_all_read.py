#!/usr/bin/env python3
"""Mark all unread emails as read"""
from gmail_handler import GmailHandler
from googleapiclient.errors import HttpError


def mark_all_as_read():
    """Mark all unread emails as read"""
    print("Connecting to Gmail...")
    gmail = GmailHandler()

    try:
        # Get all unread messages
        print("Fetching unread emails...")
        results = gmail.service.users().messages().list(
            userId='me',
            q='is:unread',
            maxResults=500
        ).execute()

        messages = results.get('messages', [])

        if not messages:
            print("No unread emails found.")
            return

        print(f"Found {len(messages)} unread emails")
        print("Marking all as read...")

        # Mark all as read using batch modify
        message_ids = [msg['id'] for msg in messages]

        # Gmail API allows batch operations
        gmail.service.users().messages().batchModify(
            userId='me',
            body={
                'ids': message_ids,
                'removeLabelIds': ['UNREAD']
            }
        ).execute()

        print(f"✓ Successfully marked {len(messages)} emails as read!")

    except HttpError as error:
        print(f'An error occurred: {error}')


if __name__ == "__main__":
    mark_all_as_read()
