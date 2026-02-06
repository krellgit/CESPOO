# CESPOO

Claude Email Summarization and Priority On-demand Offloading

## Overview

CESPOO is an intelligent email management system that uses Claude Code to process, categorize, and summarize your emails on-demand.

## What It Does

1. **On-Demand Email Processing**: Run `/cespoo` whenever you want a summary
2. **Intelligent Categorization**: Uses Claude Code to categorize emails into:
   - Amazon Advertising
   - Listing Optimization
   - Recent Trends in Amazon
   - AI Trends connected to Amazon
   - Other AI Trends
   - Uncategorized
3. **Smart Summarization**: Creates concise summaries of each email and groups them by category
4. **Email Digest**: Sends a beautiful HTML summary email to JohnKrell.StaAna1@gmail.com

## Features

1. Gmail API integration for secure email access
2. Claude Code for intelligent email analysis (no API costs!)
3. On-demand processing - you control when it runs
4. HTML formatted summary emails
5. Processes unread emails only (configurable)
6. 24-hour lookback window (configurable)

## Quick Start

### 1. Install Dependencies

```bash
cd /mnt/c/Users/Krell/Documents/Imps/gits/CESPOO
venv/bin/pip install -r requirements.txt
```

### 2. First Time: Authenticate with Gmail

```bash
venv/bin/python3 process_emails.py
```

This will open a browser for Google OAuth. Select **Krell@KeplerCommerce.com**

### 3. Use the Skill

In Claude Code, simply type:
```
/cespoo
```

Claude Code will:
1. Fetch your emails
2. Categorize and summarize them
3. Send the summary to JohnKrell.StaAna1@gmail.com

## Requirements

1. Python 3.8+
2. Claude Code CLI
3. Google Cloud Project with Gmail API enabled
4. OAuth 2.0 credentials for Gmail (already configured)

## Project Structure

```
CESPOO/
├── .claude/skills/
│   └── cespoo.md          # Claude Code skill definition
├── gmail_handler.py       # Gmail API interactions
├── process_emails.py      # Email fetching and formatting
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies (no Anthropic API!)
└── credentials.json      # Gmail OAuth credentials
```

## Configuration

Edit `config.py` to customize:
1. Email categories
2. Processing time window
3. Unread vs all emails
4. Source and destination email addresses

## Why This Approach?

**No API Costs**: Uses your existing Claude Code session instead of paying for Anthropic API
**On-Demand**: You control when it runs
**Fully Integrated**: Works seamlessly within your Claude Code workflow

## License

TBD
