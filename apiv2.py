from flask import render_template, url_for, request, redirect
import requests
import os
import pandas as pd
import re


def init_app(app):
    
    def create_url(t_query):
    
        keyword = "query={} lang:pt -is:retweet".format(t_query)
        max_results = "max_results=100"  # Min=10, max=100
        tweet_fields ="tweet.fields=created_at,text"
        url = "https://api.twitter.com/2/tweets/search/recent?{}&{}&{}".format(keyword, max_results, tweet_fields)
        return url
        
    def create_headers(bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers


    def connect_to_endpoint(url, headers):
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def main(t_query):
        bearer_token = os.environ.get("BEARER_TOKEN")
        url = create_url(t_query)
        headers = create_headers(bearer_token)
        response = connect_to_endpoint(url, headers)

        df = pd.json_normalize(response['data'])

        def cleanTxt(text):
            text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
            text = re.sub('#', '', text) # Removing '#' hash tag
            text = re.sub('RT[\s]+', '', text) # Removing RT
            text = re.sub('\n\n[A-Za-z0–9]+', '', text) # Removing \n\n
            text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
            text = re.sub(':\/\/\S+', '', text) # Removing ://
            text = re.sub(':', '', text) # Removing ":"

            return text

        # Clean the tweets
        df['text'] = df['text'].apply(cleanTxt)
        result =  df["text"]
        return result.to_csv("./query.csv")

    @app.route("/", methods=['POST', 'GET']) 
    def index():
        if request.method =='POST':
            t_query = request.form['t_query']
            t_result = main(t_query)
            return redirect(url_for("result"))
        return render_template("index.html")