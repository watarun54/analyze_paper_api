from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify
from IPython import embed
import urllib.request
from . import get_goo_keywords

app = Blueprint('scrape', __name__)

# curl -X POST -H 'Accept:application/json' -H 'Content-Type:application/json' 
#      -d '{"url":"http://example.com"}' http://127.0.0.1:5000/scrape_paper
@app.route('/scrape_paper', methods=['POST'])
def get_title():
    try:
        request_json = request.get_json()
        url = request_json['url']
        title = get_goo_keywords.get_keywords(url)
        if title is None:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            title_tag = soup.title
            title = title_tag.string
        response_json = { "title" : title }
    except:
        response_json = { "title" : "" }
    finally:
        return jsonify(response_json)
