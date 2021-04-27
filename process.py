from flask import render_template, request
import os
import nltk
import re
import pandas as pd
import numpy as np
import csv
from sentipt.sentipt import SentimentIntensityAnalyzer
import plotly.express as px
import plotly

def init_app(app):
    

    @app.route("/process")
    def result():
        training_set = []
        with open('./query.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                training_set.append((row['text']))
        os.remove('./query.csv')
        s = SentimentIntensityAnalyzer()

        def classificate(training_set):    
            df = pd.DataFrame(columns=["neg", "neu", "pos", "compound"])
            for i in range(len(training_set)):
                e = s.polarity_scores(training_set[i])
                df = df.append(e, ignore_index=True)
            return df

        data = classificate(training_set)
        labels = ["Negativos", "positivos", "Neutros"]
        negativo = data["neg"].astype(np.float16).sum()
        neutro = data["neu"].astype(np.float16).sum()
        positivo = data["pos"].astype(np.float16).sum()
        values = [negativo, positivo, neutro]
        fig = px.pie(data, values=values, names=labels, hole=.3)
        fig.write_html('tcrawler/templates/plot.html', auto_open=False)


        return render_template("result.html")