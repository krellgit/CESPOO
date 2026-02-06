#!/usr/bin/env python3
"""Complete Gmail OAuth authentication using authorization code"""
import sys
import os
from urllib.parse import urlparse, parse_qs
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import config
import json

# Allow insecure transport for localhost
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def extract_code_from_url(url):
    """Extract the authorization code from the redirect URL"""
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    return params.get('code', [None])[0]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 complete_auth.py 'REDIRECT_URL'")
        sys.exit(1)

    redirect_url = sys.argv[1]
    code = extract_code_from_url(redirect_url)

    if not code:
        print("Error: Could not extract authorization code from URL")
        sys.exit(1)

    print(f"Authorization code extracted: {code[:20]}...")
    print("\nExchanging code for tokens...")

    # Load client secrets
    with open('credentials.json', 'r') as f:
        client_config = json.load(f)

    flow = InstalledAppFlow.from_client_config(
        client_config,
        scopes=config.SCOPES,
        redirect_uri='http://localhost'
    )

    # Exchange the code for credentials
    flow.fetch_token(code=code)
    creds = flow.credentials

    # Save the credentials
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

    print("✓ Authentication successful!")
    print("✓ Token saved to token.json")
    print("\nYou can now use the /cespoo skill!\n")

if __name__ == "__main__":
    main()
