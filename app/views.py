from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "NewsHub."
    news_sources = get_sources('general')
    return render_template('index.html',title = title,news_sources = news_sources)

@app.route('/news/<source_id>')
def news(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_articles(id)
    return render_template('news.html', news = news)
