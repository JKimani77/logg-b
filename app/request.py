import urllib.request, json
from .models import Quote


#getting base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']

def get_quotes():
    urlquote = base_url

    with urllib.request.urlopen(urlquote) as url:
        get_quotes_info = url.read()
        get_quotes_response = json.loads(get_quotes_info)

        quote_results = {}

        if get_quotes_response['quote']:
            quote_results['id'] = get_quotes_response['id']
            quote_results['author'] = get_quotes_response['author']
            quote_results['quote'] = get_quotes_response['quote']

    return quote_results 