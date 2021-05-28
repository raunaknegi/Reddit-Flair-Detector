# Reddit-Flair-Detector

The app is live at: https://flair-detector-raunak.herokuapp.com/

### Directory Structure
<pre>
server.py: The main python flask file used for running the web app
templates folder: containing main.html file, which is rendered by flask
static folder: containing css for the html file
Subreddit_Scraper.ipynb: Contains the python script which scrapes reddit posts from the subreddit named `Reddit India` using PRAW, a python crawler provided by Reddit
Model.ipynb: Contains the python code implementing different Machine Learning models like RandomForest, LogisticRegression, MultiLayerPerceptron, and NaiveBayes
model.pickle: Best model saved in the pickle file
requirements.txt: python packages required for deploying at heroku
