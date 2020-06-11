from __future__ import unicode_literals
import json
import requests
import pandas as pd
import pickle
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
from flask import Flask, request, Response, render_template, session, redirect, url_for

app = Flask(__name__)

# entryLink = ''
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

def classify_comments(comments): 
    
    f = open('my_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    stop_words = stopwords.words("english")
    stop_words.append("Quality")
    stop_words.append("Product")
    stop_words.append("Good")
    stop_words.append("Not")
    stop_words.append("Love")
    stop_words.append("love")
    
    print(classifier.show_most_informative_features(200))

    results =  []
    for i in tqdm(range(0,len(comments))):
        custom_tokens = remove_noise(word_tokenize(comments[i]))
        # print(comments[i], classifier.classify(dict([custom_tokens[i], True] for i in tqdm(range(0,len(custom_tokens))))))
        results.append([comments[i], classifier.classify(dict([custom_tokens[i], True] for i in tqdm(range(0,len(custom_tokens)))))])
    return results

def scrape(url_):
    # entry_url = 'https://www.amazon.com/Goodthreads-Perfect-V-Neck-T-Shirt-Short-Sleeve/dp/B06XWLRX8W/ref=sr_1_1_sspa?dchild=1&keywords=t-shirt&qid=1585037086&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR005TkVRQTJRSkhSJmVuY3J5cHRlZElkPUEwNDM1Mjc3M1E2OUFGMzhYOTVVJmVuY3J5cHRlZEFkSWQ9QTA2MTg0MDEyQlNCRE5BVEdFS0tOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    params = {
        'spider_name': 'AmazonSpider',
        # 'start_requests': True,
        'url': url_
     
    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    return data
    # df=pd.DataFrame(data=data['items'], columns=['Title','Price','Stock','Star'])
    # return render_template('simple.html',  tables=[df.to_html(classes='data',  index=False)], titles=df.columns.values)
# @app.route('/')
# def scrape():
#     entry_url = 'https://www.amazon.com/Goodthreads-Perfect-V-Neck-T-Shirt-Short-Sleeve/dp/B06XWLRX8W/ref=sr_1_1_sspa?dchild=1&keywords=t-shirt&qid=1585037086&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR005TkVRQTJRSkhSJmVuY3J5cHRlZElkPUEwNDM1Mjc3M1E2OUFGMzhYOTVVJmVuY3J5cHRlZEFkSWQ9QTA2MTg0MDEyQlNCRE5BVEdFS0tOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
#     params = {
#         'spider_name': 'AmazonSpider',
#         # 'start_requests': True,
#         'url': entry_url
     
#     }
#     response = requests.get('http://localhost:9080/crawl.json', params)
#     data = json.loads(response.text)
#     print(data)
#     df=pd.DataFrame(data=data['items'], columns=['Title','Price','Stock','Star'])
#     return render_template('simple.html',  tables=[df.to_html(classes='data',  index=False)], titles=df.columns.values)

@app.route('/')
def get_url():
    return render_template('geturl.html')

@app.route('/result',methods=['POST'])
def result():
    if request.method == 'POST':
        link = request.form['link']
        data = scrape(link)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # # pprint.pprint(data)

        # print(data)
        product = data['items'][0]
        
        # print(product)
        item_name = product['item_name']
        print("Item Name: " + item_name)

        item_price = product['price']
        print("Item Price: " + item_price)

        comments = product['comments']
        
        print("Comments: \n\n" , comments)
        

        item_img_path = product['img']

        final_results = classify_comments(comments)

        number_of_negative_comments = 0
        number_of_positive_comments = 0

        print("Final Results: \n\n")
        for i in range(0,len(final_results)):
            if final_results[i][1] == "negative":
                number_of_negative_comments+=1
            else:
                number_of_positive_comments+=1

        print("\n\nTotal Negative Comments: " , number_of_negative_comments)
        print("\nTotal Positive Comments: " , number_of_positive_comments)     


        finalProduct   = {
            'title':item_name,
            'price':item_price,
            'comments':final_results,
            'img_path':item_img_path,
            'negative_count':number_of_negative_comments,
            'positive_count':number_of_positive_comments
        
        }

        # finalProduct   = {
        #     'title':"A Bufallo Rider Two On Two L)LL",
        #     'price':"$199",
        #     'comments':["One","Two","Three","Lorem Ipsuemmmm"],
        #     'img_path':"https://image.shutterstock.com/image-vector/ui-image-placeholder-wireframes-apps-260nw-1037719204.jpg",
        #     'negative_count':1000,
        #     'positive_count':30
        
        # }

        return render_template('result.html',product=finalProduct, comments = finalProduct['comments'])



        # return render_template('result.html',product_name = item_name,product_image = item_img_path, product_price = item_price, results = final_results)
       
if __name__ == '__main__':
    app.run(debug=True, port=8081)