import PyPDF2
import requests
import json
import os



pdf_file = open('obligacje.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

text = ""


for i in range (num_pages):
    page = pdf_reader.pages[i]
    text += page.extract_text()
    
# Remove the first newline character 
text = text.replace("\n","",1)
# Replace the second newline character
text = text.replace("\n", "")
    

  

url = 'https://api.lovo.ai/v1/conversion'
data = json.dumps({
    "text": text,
    "speaker_id": "Maja L.",
    "emphasis": "[2, 4]",
    "speed": 1,
    "pause": 5,
    "encoding": "mp3"
})


headers = {
    'apiKey': os.getenv('apiKey'),   # Your API key goes here
    'Content-Type': 'application/json; charset=utf-8'}

res = requests.post(url, headers=headers, data=data)
# Check the status code
if res.status_code == 200:
    print('The request was successful')
elif res.status_code == 404:
    print('The requested page was not found')
else:
    print('An error occurred')
    print(res.status_code)

# you can also download the audio file
outfile = 'sample.mp3'
with open(outfile, 'wb') as f:
    f.write(res.content)
    

