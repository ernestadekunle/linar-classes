import praw

# Replace these with your own Reddit account credentials
username = 'foxysittincute'
password = 'D@r98019937'
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Create a Reddit instance and authenticate
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent='my_user_agent', username=username)

# Set the message you want the bot to reply with
response_message = "Thanks for reaching out! Here's some information you might find helpful."

# Create a function to check for new DMs and reply
def check_and_reply():
  # Get a list of unread DMs
  unread_dms = reddit.inbox.unread(limit=None)
  # Iterate through the unread DMs
  for message in unread_dms:
    # If the message is a DM, reply to it
    if isinstance(message, praw.models.Message):
      message.reply(response_message)
      message.mark_read()
      print(f'Replied to DM {message.id}')

# Run the function every 5 minutes
while True:
  check_and_reply()
  time.sleep(300)
