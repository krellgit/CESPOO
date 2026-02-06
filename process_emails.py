"""Process emails and prepare for Claude Code summarization"""
import json
import sys
from datetime import datetime
import config
from gmail_handler import GmailHandler


def fetch_emails():
    """Fetch emails and return formatted data"""
    print(f"Fetching emails from {config.SOURCE_EMAIL}...")
    print(f"Looking back {config.LOOKBACK_HOURS} hours")
    print(f"Unread only: {config.PROCESS_UNREAD_ONLY}\n")

    gmail = GmailHandler()
    emails = gmail.get_emails(
        hours_back=config.LOOKBACK_HOURS,
        unread_only=config.PROCESS_UNREAD_ONLY
    )

    if not emails:
        print("No emails found.")
        return None

    print(f"Found {len(emails)} emails\n")
    return emails


def format_emails_for_claude(emails):
    """Format emails into a readable text for Claude Code to process"""
    formatted = []

    for i, email in enumerate(emails, 1):
        # Truncate body if too long
        body = email['body'][:1000] + "..." if len(email['body']) > 1000 else email['body']

        formatted.append(f"""
{'='*80}
EMAIL {i}
{'='*80}
Subject: {email['subject']}
From: {email['sender']}
Date: {email['date']}

Body:
{body}
""")

    return "\n".join(formatted)


def save_emails_to_file(emails, filename="emails_to_process.txt"):
    """Save emails to a file for Claude Code to read"""
    formatted = format_emails_for_claude(emails)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"EMAILS TO CATEGORIZE AND SUMMARIZE\n")
        f.write(f"Total Emails: {len(emails)}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"\nCategories to use:\n")
        for cat in config.EMAIL_CATEGORIES:
            f.write(f"  - {cat}\n")
        f.write("\n" + "="*80 + "\n")
        f.write(formatted)

    return filename


def send_summary_email(summary_html):
    """Send the summary email"""
    gmail = GmailHandler()

    subject = f"📧 CESPOO Daily Email Summary - {datetime.now().strftime('%b %d, %Y')}"

    success = gmail.send_email(
        to=config.DESTINATION_EMAIL,
        subject=subject,
        body=summary_html
    )

    return success


if __name__ == "__main__":
    # Fetch and save emails
    emails = fetch_emails()

    if emails:
        filename = save_emails_to_file(emails)
        print(f"✓ Emails saved to: {filename}")
        print(f"\nNext step: Use Claude Code to categorize and summarize these emails")
