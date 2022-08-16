from flask import Flask 
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from IPython.display import Image

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/company/<company>')

def get_img_url(company):
	response = requests.get(
		url= get_url(company),
	)

	soup = BeautifulSoup(response.content, 'html.parser')
	img = soup.select_one('.image').find("img")
	image = img['src']
	return "https:" + image

def get_url(company):
    # to search
    query = company + " maroc wikipedia"
    api = ''
    Results = search(query , num=1, stop=1)
    for url in Results:
        api = url
    return api

if __name__ == "__main__":
    app.run(debug=True)
