"""Configuration settings for CESPOO"""
import os
from dotenv import load_dotenv

load_dotenv()

# Email accounts
SOURCE_EMAIL = "Krell@KeplerCommerce.com"
DESTINATION_EMAIL = "JohnKrell.StaAna1@gmail.com"

# Anthropic API
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Gmail API settings
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send']

# Scheduling
RUN_TIME = os.getenv("RUN_TIME", "09:00")  # Default 9 AM, format HH:MM

# Email categories for classification
EMAIL_CATEGORIES = [
    "Amazon Advertising",
    "Listing Optimization",
    "Recent Trends in Amazon",
    "AI Trends connected to Amazon",
    "Other AI Trends",
    "Uncategorized"
]

# Email processing settings
PROCESS_UNREAD_ONLY = True
LOOKBACK_HOURS = 24  # How many hours back to look for emails
