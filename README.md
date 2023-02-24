Install: python3 >= python3.9 on Jenkins-Server

Run: pip install -r 

Run: prowler aws --list-compliance-requirements gdpr_aws

Copy Requirements:  /tmp/checks.json

Copy slack_bot_token to /tmp/slack_bot_token.txt

Put send_slack_message.py to /tmp/send_slack_message.py

Create Pipeline: Interval (H H 1 * *) every month

Add Prowler: Integrations in AWS Security-Hub