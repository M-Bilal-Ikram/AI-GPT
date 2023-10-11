# In this code you can ask questions by replacing my question 
# You can also change source by replacing my link
# You can run this code on Google colab, if you dont have installed enviroment or ide for it. 😀😀

import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Load the question-answering model
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Define the URL you want to scrape
url = 'https://islamabadpost.com.pk/how-pakistan-can-become-a-developed-country/'

# Send an HTTP GET request and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract relevant information (adjust this part based on the website's HTML structure)
content = " ".join([p.text for p in soup.find_all('p')])

# Ask a question related to the scraped content
question = "How can Pakistan become a developed country?"

# Get the answer using the model
answer = qa_pipeline(question=question, context=content)

print(f"Question: {question}")
print(f"Answer: {answer['answer']}")
