import os 
import sys

from util import cleaner
from util import extractor
from util import loader

url = "https://en.wikipedia.org/wiki/Bongcloud_Attack"

import findspark
findspark.init()

if __name__=='__main__':
    from pyspark.sql import SparkSession
    from pyspark.sql import Row
    
    spark = SparkSession.builder\
            .master('local')\
            .appName('text-cleaner')\
            .getOrCreate()
    
    text = extractor.getText(url=url)
    os.chdir(r'/Users/prakash/Documents/Projects/text-cleaner/data')
    PATH = 'text.txt'
    with open("text.txt", "w") as text_file:
        text_file.write(text)
    dF = spark.read.text(PATH)
    cleaned_text=dF.map(lambda x: cleaner.cleaned(x))
    sentiment = cleaned_text.map(lambda x: cleaner.sentiment(x))
    loader.insert(text,cleaned_text,sentiment)

    