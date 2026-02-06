# CESPOO Setup Guide

## Prerequisites

1. Python 3.8 or higher installed
2. Anthropic API key
3. Google Cloud Project with Gmail API enabled
4. Access to both email accounts:
   - Krell@KeplerCommerce.com (source)
   - JohnKrell.StaAna1@gmail.com (destination)

## Setup Steps

### 1. Install Dependencies

```bash
cd /mnt/c/Users/Krell/Documents/Imps/gits/CESPOO
pip install -r requirements.txt
```

### 2. Set Up Gmail API Credentials

#### 2.1. Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Gmail API:
   - Go to "APIs & Services" > "Library"
   - Search for "Gmail API"
   - Click "Enable"

#### 2.2. Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. If prompted, configure the OAuth consent screen:
   - User Type: Internal (if using Google Workspace) or External
   - Add your email as a test user
   - Scopes: Add Gmail API scopes (will be requested by the app)
4. Application type: "Desktop app"
5. Download the credentials
6. Rename the downloaded file to `credentials.json`
7. Place `credentials.json` in the CESPOO project root directory

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=sk-ant-...your-key-here
   RUN_TIME=09:00
   ```

### 4. First Run - Authentication

Run the script for the first time to authenticate:

```bash
python main.py --now
```

This will:
1. Open a browser window for Google OAuth authentication
2. Ask you to select the Krell@KeplerCommerce.com account
3. Grant permissions to read and send emails
4. Save the authentication token to `token.json`

**Important:** Make sure you authenticate with the Krell@KeplerCommerce.com account, not your personal Gmail.

### 5. Test the Setup

After authentication, the script will immediately process your emails and send a summary to JohnKrell.StaAna1@gmail.com.

Check your inbox to verify the summary email arrived correctly.

## Running CESPOO

### Run Once (Testing)

```bash
python main.py --now
```

### Run on Schedule

```bash
python main.py
```

This will run the script continuously, processing emails at the configured time each day (default: 9:00 AM).

### Run as Background Service (Linux/WSL)

Create a systemd service or use `nohup`:

```bash
nohup python main.py > cespoo.log 2>&1 &
```

### Run as Scheduled Task (Windows)

Use Windows Task Scheduler to run `python main.py --now` at your desired time.

## Configuration

Edit `config.py` to customize:

1. Email categories
2. Lookback period (default: 24 hours)
3. Unread only vs all emails
4. Email addresses (if needed)

## Troubleshooting

### "credentials.json not found"

Make sure you've downloaded and placed the OAuth credentials file in the project root.

### "Invalid grant" or authentication errors

Delete `token.json` and run `python main.py --now` again to re-authenticate.

### "Anthropic API error"

Verify your API key is correct in the `.env` file.

### No emails found

1. Check the time range in `config.py` (LOOKBACK_HOURS)
2. Verify there are unread emails in your inbox if PROCESS_UNREAD_ONLY is True
3. Check that you're authenticated with the correct Gmail account

## Security Notes

1. Never commit `credentials.json`, `token.json`, or `.env` to version control
2. Keep your Anthropic API key secure
3. The OAuth token has read and send permissions - protect it accordingly
4. Review the Gmail API scopes to ensure they match your security requirements
