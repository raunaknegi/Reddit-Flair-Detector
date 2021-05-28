import pickle
import flask
from flask import Flask, flash, request,jsonify, json
import praw
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import utils

#preprocessing the text
def clean_text(X):
    ps=PorterStemmer()
    post=re.sub('[^a-zA-Z]',' ',X)
    post=utils.to_unicode(post)
    post=post.lower()
    post=post.split()
    post=[ps.stem(word) for word in post if not word in set(stopwords.words('english'))]
    post=' '.join(post)
    return post

app = Flask(__name__)

reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='', \
                     username='', \
                     password='')
#returning predicted and original flair
def prediction(url):
    user_submission=reddit.submission(url=url)
    post_data={}
    post_data['title']=clean_text(user_submission.title)
    post_data['body']=clean_text(user_submission.selftext)
    user_submission.comments.replace_more(limit=None)
    comment = ''
    count = 0
    for top_level_comment in user_submission.comments:
        comment = comment + ' ' + top_level_comment.body
        count+=1
        if(count > 10):
            break
    
    post_data["comment"] = clean_text(comment)
    post_data['combined']=str(post_data['title']) + str(post_data['body']) + str(post_data['comment'])
    model=pickle.load(open('model.pkl','rb'))
    prediction_=model.predict([post_data['combined']])
    return ((str(prediction_)[2:-2]),user_submission.link_flair_text)

@app.route('/')
def main():
    return flask.render_template('main.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    url=flask.request.form['url']
    predicted_flair,real_flair=prediction(url)
    return flask.render_template('main.html',predicted=predicted_flair,actual=real_flair)

if __name__=='__main__':
    app.debug=True
    app.run()