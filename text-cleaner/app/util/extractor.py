from newspaper import Article

def getText(url):
    text = Article(url)
    text.download()
    text.parse()
    output = text.text
    return output
