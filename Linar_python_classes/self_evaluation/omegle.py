'''import random

# Set up the Omegle client
client = OmegleClient()

# Connect to the Omegle server
client.connect()

# Start a new conversation
client.start_conversation()

# Run the chatbot
while True:
  # Get the latest message from the conversation
  message = client.get_latest_message()

  # If the message is empty, it means the other person has disconnected
  if not message:
    break

  # Print the message
  print("Other: " + message)

  # Generate a response
  response = generate_response(message)

  # Send the response
  client.send_message(response)

# Disconnect from the Omegle server
client.disconnect()'''
import math
print(math.pi   )