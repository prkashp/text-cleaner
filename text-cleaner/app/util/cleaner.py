#Todo
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

def cleaned(text):
    output = ""
    text_no_pun = "".join([i.lower() for i in text if i not in text.punctuation])
    ps = PorterStemmer()
    words = text_no_pun.split()
    for word in words:
        output+=ps.stem(word)
    return output

def sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

