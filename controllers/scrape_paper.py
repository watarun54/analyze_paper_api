from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify
from IPython import embed
import urllib.request

app = Blueprint('scrape', __name__)

# curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' 
#      -d '{"url":"http://example.com"}' http://127.0.0.1:5000/scrape_paper
@app.route('/scrape_paper', methods=['POST'])
def get_title():
    request_json = request.get_json()
    url = request_json['url']
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.title
    title = title_tag.string
    response_json = { "title" : title }
    return jsonify(response_json)
