

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import json
import re, string, random
import pprint
import itertools
from tqdm import tqdm
import pickle

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens



if __name__ == "__main__":

   

    f = open('my_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    stop_words = stopwords.words("english")
    stop_words.append("Quality")
    stop_words.append("Product")
    stop_words.append("Good")
    stop_words.append("Not")




    print(classifier.show_most_informative_features(200))




    
    # comments = ["I dont like this product","Good Quality Product","The Finishing was outstanding","Not Amazing packaging"]
    
    # for i in tqdm(range(0,len(comments))):
    #     custom_tokens = remove_noise(word_tokenize(comments[i]))
    #     print(comments[i], classifier.classify(dict([custom_tokens[i], True] for i in tqdm(range(0,len(custom_tokens))))))
    

    f.close()
    
    