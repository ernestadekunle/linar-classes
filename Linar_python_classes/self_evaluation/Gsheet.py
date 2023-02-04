import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTAc6VvZVAxWe-Op1NpAvF7riIWyJJhvgz3LUm0oKUoyrTmiW5DGcYH_Cy0r7LfGdX88HrhzBuMEtIp/pubhtml'

# Send a request to the webpage and retrieve the HTML
r = requests.get(url)
html = r.text

# Use Beautiful Soup to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all the email elements on the webpage
email_elements = soup.find_all(class_='email')
print(email_elements)

'''# Create an empty list to store the emails
emails = []

# Iterate through the email elements and extract the email text
for email in email_elements:
  email_text = email.text
  emails.append(email_text)

# Print the emails
print(emails)

# Save the emails to a file
with open('emails.txt', 'w') as f:
  for email in emails:
    f.write(email + '\n')'''
