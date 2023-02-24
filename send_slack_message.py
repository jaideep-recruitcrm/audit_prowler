from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def get_bot_token(token_path):
  with open('/tmp/slack_bot_token.txt', 'r') as token:
      bot_token = token.read().strip('\n')
  return bot_token


if __name__ == "__main__":
    date = datetime.now()
    token_path = '/tmp/slack_bot_token.txt'
    bot_token = get_bot_token(token_path)

    slack_client = WebClient(token=bot_token)

    try:
        response = slack_client.files_upload_v2(
            file='./scan_result.zip',
            initial_comment=f'Monthly Prowler Scan Report {(date.today()).strftime("%d_%m_%Y")}',
            title='scan_result.zip',
            channels='C04RGT1AG4R'
        )

    except SlackApiError as error:
        print(f'Error uploading file: {error}')