from urllib.parse import urlparse, parse_qs

def get_keywords(url):
    parsed_url = urlparse(url)
    if "www.google" not in parsed_url.netloc: return None
    qs = urlparse(url).query
    qs_d = parse_qs(qs)
    return qs_d['q'][0] + " | Google Search"
