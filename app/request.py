from app import app
import urllib.request,json
from .models import Sources

api_key = None
base_url = None
source_url = None

def configure_request(app):
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_NEWS_API_URL']
    sources_url = app.config['SOURCE_NEWS_URL']


def get_sources(source):
    '''
     This method fetches the various news sources from the API
    '''

    get_sources_url = base_url.format(source,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results
    return movie_results
