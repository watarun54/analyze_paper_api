from urllib.parse import urlparse, parse_qs

def get_keywords(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc != "www.google.com": return None
    qs = urlparse(url).query
    qs_d = parse_qs(qs)
    return qs_d['q'][0]
