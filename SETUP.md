# CESPOO Setup Guide

## Overview

CESPOO is a Claude Code skill that fetches, categorizes, and summarizes your emails on-demand. No API costs - uses your existing Claude Code session!

## Prerequisites

1. Python 3.8+ (already installed ✓)
2. Claude Code CLI (you're using it now ✓)
3. Google Cloud Project with Gmail API enabled
4. OAuth credentials (credentials.json already in place ✓)

## Setup Steps

### 1. Install Dependencies (Already Done ✓)

```bash
cd /mnt/c/Users/Krell/Documents/Imps/gits/CESPOO
venv/bin/pip install -r requirements.txt
```

### 2. First Run - Gmail Authentication

Run the email fetcher once to authenticate:

```bash
cd /mnt/c/Users/Krell/Documents/Imps/gits/CESPOO
venv/bin/python3 process_emails.py
```

This will:
1. Open a browser window for Google OAuth
2. Ask you to select **Krell@KeplerCommerce.com** (IMPORTANT!)
3. Grant permissions to read and send emails
4. Save the token to `token.json`

### 3. Test the Skill

In Claude Code, type:
```
/cespoo
```

This will:
1. Fetch unread emails from the last 24 hours
2. Ask Claude Code to categorize and summarize them
3. Send the summary to JohnKrell.StaAna1@gmail.com

## How It Works

### The Flow

1. **You invoke**: Type `/cespoo` in Claude Code
2. **Fetch emails**: Script downloads emails from Krell@KeplerCommerce.com
3. **Claude processes**: I (Claude Code) read, categorize, and summarize
4. **Send summary**: Beautiful HTML email sent to JohnKrell.StaAna1@gmail.com

### Email Categories

Emails are categorized into:
1. Amazon Advertising
2. Listing Optimization
3. Recent Trends in Amazon
4. AI Trends connected to Amazon
5. Other AI Trends
6. Uncategorized

## Configuration

Edit `/mnt/c/Users/Krell/Documents/Imps/gits/CESPOO/config.py` to customize:

```python
# Change email addresses
SOURCE_EMAIL = "Krell@KeplerCommerce.com"
DESTINATION_EMAIL = "JohnKrell.StaAna1@gmail.com"

# Change processing settings
PROCESS_UNREAD_ONLY = True  # Set to False to process all emails
LOOKBACK_HOURS = 24  # How far back to look

# Modify categories
EMAIL_CATEGORIES = [
    "Your Category 1",
    "Your Category 2",
    # ...
]
```

## Troubleshooting

### "credentials.json not found"
The file is already in place. If missing, re-download from Google Cloud Console.

### "Invalid grant" or authentication errors
Delete `token.json` and run `venv/bin/python3 process_emails.py` again.

### "No emails found"
1. Check there are unread emails in Krell@KeplerCommerce.com
2. Adjust `LOOKBACK_HOURS` in config.py
3. Set `PROCESS_UNREAD_ONLY = False` to process all emails

### Skill not found
Make sure you're in a Claude Code session and the skill file exists at:
`/mnt/c/Users/Krell/Documents/Imps/gits/CESPOO/.claude/skills/cespoo.md`

## Usage Tips

1. **Run on-demand**: Use `/cespoo` whenever you want a summary
2. **Morning routine**: Run it first thing to see overnight emails
3. **Before meetings**: Quick summary of what's important
4. **End of day**: Review what came in during the day

## Advantages Over API Approach

1. **No API Costs**: Uses your existing Claude Code session
2. **Full Control**: You decide when to run it
3. **Transparent**: You see exactly what Claude is doing
4. **Flexible**: Easy to adjust the prompt or categories on the fly

## Next Steps

Ready to test? Just type:
```
/cespoo
```
