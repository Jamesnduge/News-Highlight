class Source:
    '''
    Source class to define News source Objects
    '''

    def __init__(self, id, name, description, urlToImage):
        self.id =id
        self.name = name
        self.description = description
        self.urlToImage = urlToImage

class Articles:
    '''
    defines the articles objects
    '''

    def __init__(self, blue, id, title, author, description, urlToImage, publishedAt, url):
        self.blue = blue
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url
