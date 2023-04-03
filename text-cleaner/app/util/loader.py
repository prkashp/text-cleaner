from elasticsearch import Elasticsearch
import datetime, uuid

def insert(text,cleaned_text, sentiments):

    es = Elasticsearch()

    doc = {
        'text': text,
        'cleaned': cleaned_text,
        'sentiment': sentiments,
        'timestamp': datetime.now()
    }

    res = es.index(index='article', id=uuid, body=doc)
    return(res['result'])