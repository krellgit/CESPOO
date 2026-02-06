# CESPOO

Claude Email Summarization and Priority On-demand Offloading

## Overview

CESPOO is an intelligent email management system that leverages Claude AI to automatically process, categorize, and summarize your emails.

## What It Does

1. **Automated Email Reading**: Runs at a scheduled time each day to read emails from Krell@KeplerCommerce.com
2. **Intelligent Categorization**: Uses Claude AI to categorize emails into:
   - Amazon Advertising
   - Listing Optimization
   - Recent Trends in Amazon
   - AI Trends connected to Amazon
   - Other AI Trends
   - Uncategorized
3. **Smart Summarization**: Creates concise summaries of each email and groups them by category
4. **Daily Digest**: Sends a beautiful HTML summary email to JohnKrell.StaAna1@gmail.com

## Features

1. Gmail API integration for secure email access
2. Claude 4.5 Sonnet for intelligent email analysis
3. Configurable scheduling (default: 9 AM daily)
4. HTML formatted summary emails
5. Processes unread emails only (configurable)
6. 24-hour lookback window (configurable)

## Quick Start

See [SETUP.md](SETUP.md) for detailed setup instructions.

```bash
# Install dependencies
pip install -r requirements.txt

# Configure your API keys
cp .env.example .env
# Edit .env with your Anthropic API key

# Run once to test
python main.py --now

# Run on schedule
python main.py
```

## Requirements

1. Python 3.8+
2. Anthropic API key
3. Google Cloud Project with Gmail API enabled
4. OAuth 2.0 credentials for Gmail

## Project Structure

```
CESPOO/
├── main.py              # Main entry point and scheduler
├── gmail_handler.py     # Gmail API interactions
├── email_processor.py   # Claude AI email processing
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
└── SETUP.md          # Detailed setup guide
```

## Configuration

Edit `config.py` to customize:
- Email categories
- Processing time window
- Unread vs all emails
- Schedule timing (via .env)

## License

TBD
