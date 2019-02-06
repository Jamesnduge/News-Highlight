from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources('general')
    title = "NewsHub."
    return render_template('index.html',title = title,news_sources = news_sources)

@main.route('/articles/<id>')
def articles(id):
    '''
    Shows
    '''

    news = get_articles(id)

    title = "Top Headlines"
    return render_template('articles.html', title = title, news = news)
