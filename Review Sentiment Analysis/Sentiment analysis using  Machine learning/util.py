from exception import Sentiment_Exception
from logger import logging
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


stemmer= PorterStemmer()

def text_transformer(in_text):
    #lowering the text
    in_text=in_text.lower()
    #seperating each word
    in_text=nltk.word_tokenize(in_text)
    #removing special characters from in_text
    temp_list=[]
    for word in in_text:
        if word.isalnum():
            temp_list.append(word)
    in_text= temp_list.copy()
    temp_list.clear()
    
    #removing stopwords and punctuation marks from in_text
    for word in in_text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            temp_list.append(word)
    in_text=temp_list.copy()
    temp_list.clear()
    
    #Stemming the words to get base form of words
    for word in in_text:
        temp_list.append(stemmer.stem(word))
    #joining all words in list and returning complete sentence/ document
    return " ".join(temp_list)