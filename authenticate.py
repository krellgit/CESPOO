#!/usr/bin/env python3
"""Helper script to complete Gmail OAuth authentication"""
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
import config

def main():
    if len(sys.argv) < 2:
        # Generate authorization URL
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', config.SCOPES)
        flow.redirect_uri = 'http://localhost'
        auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

        print("\n" + "="*80)
        print("STEP 1: AUTHORIZE IN BROWSER")
        print("="*80)
        print("\nOpen this URL in your browser:")
        print(f"\n{auth_url}\n")
        print("1. Select the Krell@KeplerCommerce.com account")
        print("2. Grant permissions")
        print("3. Copy the ENTIRE redirect URL from your browser")
        print("   (It will start with http://localhost and contain a code)")
        print("\n" + "="*80)
        print("STEP 2: COMPLETE AUTHENTICATION")
        print("="*80)
        print("\nRun this command with the redirect URL:")
        print(f"\nvenv/bin/python3 authenticate.py 'YOUR_REDIRECT_URL_HERE'\n")
        print("="*80 + "\n")
    else:
        # Complete authentication with provided redirect URL
        redirect_url = sys.argv[1]

        print("\nCompleting authentication...")

        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', config.SCOPES)
        flow.redirect_uri = 'http://localhost'

        # Need to generate the URL first to set up the flow properly
        auth_url, state = flow.authorization_url(prompt='consent', access_type='offline')

        # Fetch the token using the redirect URL
        flow.fetch_token(authorization_response=redirect_url)

        # Save the credentials
        creds = flow.credentials
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        print("✓ Authentication successful!")
        print("✓ Token saved to token.json")
        print("\nYou can now use the /cespoo skill!\n")

if __name__ == "__main__":
    main()
