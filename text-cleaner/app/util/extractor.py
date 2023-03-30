from newspaper import Article

def getText(url):
    text = Article(url)
    text.download()
    text.parse()
    output = [text.authors,text.publish_date,text.text,text.summary,text.keywords]
    return output
