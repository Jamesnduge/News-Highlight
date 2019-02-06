import os

class Config:
    '''
    General configuration parent class
    '''
    BASE_NEWS_API_URL ='https://newsapi.org/v2/sources?category={}&apiKey=84ace3fc520e4373b0d875d7d4c542b1'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=84ace3fc520e4373b0d875d7d4c542b1'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
