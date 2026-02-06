"""Main script for CESPOO - Email Summarization System"""
import schedule
import time
from datetime import datetime
import config
from gmail_handler import GmailHandler
from email_processor import EmailProcessor


def process_emails():
    """Main function to process and summarize emails"""
    print(f"\n{'='*50}")
    print(f"CESPOO - Starting email processing at {datetime.now()}")
    print(f"{'='*50}\n")

    try:
        # Initialize handlers
        gmail = GmailHandler()
        processor = EmailProcessor()

        # Fetch emails
        print(f"Fetching emails from {config.SOURCE_EMAIL}...")
        print(f"Looking back {config.LOOKBACK_HOURS} hours")
        print(f"Unread only: {config.PROCESS_UNREAD_ONLY}")

        emails = gmail.get_emails(
            hours_back=config.LOOKBACK_HOURS,
            unread_only=config.PROCESS_UNREAD_ONLY
        )

        if not emails:
            print("No emails to process.")
            return

        print(f"Found {len(emails)} emails to process")

        # Categorize and summarize
        print("Analyzing and categorizing emails with Claude...")
        summary = processor.categorize_and_summarize(emails)

        # Create HTML email
        print("Creating HTML summary...")
        html_summary = processor.create_html_summary(summary, len(emails))

        # Send summary email
        print(f"Sending summary to {config.DESTINATION_EMAIL}...")
        subject = f"📧 CESPOO Daily Email Summary - {datetime.now().strftime('%b %d, %Y')}"

        gmail.send_email(
            to=config.DESTINATION_EMAIL,
            subject=subject,
            body=html_summary
        )

        print("\n✓ Email processing complete!")
        print(f"Summary sent to {config.DESTINATION_EMAIL}")

    except Exception as e:
        print(f"\n✗ Error processing emails: {str(e)}")
        import traceback
        traceback.print_exc()


def run_scheduled():
    """Run the email processor on a schedule"""
    print(f"CESPOO started - scheduled to run daily at {config.RUN_TIME}")

    # Schedule the job
    schedule.every().day.at(config.RUN_TIME).do(process_emails)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--now":
        # Run immediately for testing
        print("Running immediately (test mode)...")
        process_emails()
    else:
        # Run on schedule
        run_scheduled()
