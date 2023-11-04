#1. Build a Flask app that scrapes data from multiple websites and displays it on your site.
#You can try to scrap websites like youtube , amazon and show data on output pages and deploy it on cloud
#platform
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Scraping data from YouTube
    youtube_url = "https://www.youtube.com/"
    youtube_response = requests.get(youtube_url)
    youtube_soup = BeautifulSoup(youtube_response.content, 'html.parser')
    youtube_data = youtube_soup.title.text.strip()

    # Scraping data from Amazon
    amazon_url = "https://www.amazon.com/"
    amazon_response = requests.get(amazon_url)
    amazon_soup = BeautifulSoup(amazon_response.content, 'html.parser')
    amazon_data = amazon_soup.title.text.strip()

    return render_template('index.html', youtube_data=youtube_data, amazon_data=amazon_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
