import requests
from bs4 import BeautifulSoup

# Make a request to the webpage
response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTAc6VvZVAxWe-Op1NpAvF7riIWyJJhvgz3LUm0oKUoyrTmiW5DGcYH_Cy0r7LfGdX88HrhzBuMEtIp/pubhtml')

# Parse the HTML of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements that contain the keywords "gmail" and "com"
elements = soup.find_all(string=lambda text: "gmail" in text and "com" in text)

# Extract the text from the elements
text = [element.strip() for element in elements]


# Print the text
print(elements)
