from app import app
import urllib.request,json
from .models import Source, Articles
#Source =source.Source

api_key = app.config['NEWS_API_KEY']
base_url = app.config['BASE_NEWS_API_URL']
sources_url = app.config['SOURCE_NEWS_URL']

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

def process_results(sources_list):
    '''
    Function that process the source results list and transforms them into a list of objects
    Args:
        sources_list: A list of dictionaries that contains sources details

    Returns:
        sources_results: a list of sources objects
    '''

    sources_results = []
    for source_item in sources_list:
        source_id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        urlToImage = source_item.get('urlToImage')


        source_object = Source(id, name, description, urlToImage)
        sources_results.append(source_object)

    return sources_results
    return movie_results

def get_articles(id):
    """Function to retrieve news sources list from the News api"""

    get_articles_url ='https://newsapi.org/v1/articles?source={}&apiKey={}'.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

    return articles_results


def process_articles_results(article_list):
    """Function that process the results list and transforms them into a list of objects
    Args: articles_list: A list of dictionaries that contains news articles and links
    Returns:
    articles_results: a list of news articles objects"""

    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        date = article_item.get('publishedAt')

        if urlToImage:
            article_object = Articles(id, author, title, description, urlToImage, url, date)
            article_results.append(article_object)

    return article_results
