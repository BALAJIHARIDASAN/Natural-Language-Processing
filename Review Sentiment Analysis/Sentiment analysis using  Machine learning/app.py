from flask import Flask, render_template, request
import joblib
import os, sys
from exception import CustomException
from logger import logging
from utils import text_transformer


### loading model and scalar object
logging.info("Reading model object from model.sav file")
model=joblib.load('Models\model.sav')
logging.info("Reading Vectorizer object from vectorizer.sav file")
vectorizer=joblib.load('Models\vectorizer.sav')




app=Flask(__name__)

### creating home route
logging.info("Creating Home route")
@app.route("/")
def home():
    return render_template("home.html")


# Creating Prediction route
logging.info("Creating Prediction route")
@app.route('/prediction',methods=['POST'])
def prediction():
    try:
        logging.info("Getting input data from the flask form for prediction")
        data=[str(x) for x in request.form.values()]
        logging.info("Transforming data using text transformer function")
        transformed_text=text_transformer(data[0])
        logging.info("Converting text to vector using saved TFIDF object")
        vectorized_text=vectorizer.transform([transformed_text])
        logging.info("Generating model prediction using saved model object")
        output=model.predict(vectorized_text)
        if output==-1:
            logging.info("Sentiment is Positive.")
            output= "Sentiment is Positive."
        elif output == 0:
            logging.info("Sentiment is Neutral.")
            output="Message is ham i.e. Normal."
        else:
            logging.info('Sentiment is Negative')
            output = 'Sentiment is Negative'
        logging.info("Returning model prediction to web application")
        return render_template("home.html",prediction_value="Model Prediction: {}".format(output))
    except Exception as e:
        raise CustomException(e, sys)

### Note check log file for the server link or paste this in browser: http://127.0.0.1:5000
if __name__=='__main__':
    app.run()