from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/avclassify", methods=['GET', 'POST'])
def avclassify():

    #extract form inputs
    SafeAv = request.form.get("SafeAv")
    AVImpact = request.form.get("AVImpact")
    ProvingGround = request.form.get("ProvingGround")
    FamiliarityTech = request.form.get("FamiliarityTech")
    SchoolZoneManual = request.form.get("SchoolZoneManual")
    SharedPedestrian = request.form.get("SharedPedestrian")
    ZipCode = request.form.get("ZipCode")
    FamiliarityNews = request.form.get("FamiliarityNews")

   #convert data to json
    input_data = json.dumps({"SafeAv": SafeAv, "AVImpact": AVImpact, "ProvingGround": ProvingGround,
                             "FamiliarityTech": FamiliarityTech, "SchoolZoneManual": SchoolZoneManual, 
                             "SharedPedestrian": SharedPedestrian, "ZipCode": ZipCode, 
                             "FamiliarityNews": FamiliarityNews})

    #url for bank marketing model
    url = "http://localhost:5000/api" #for local machine testing
    #url = "hhttps://av-model-app-6f2c9d64a330.herokuapp.com/api" #for hosting on Heroku
  
    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", SafeAv = SafeAv, AVImpact = AVImpact, ProvingGround = ProvingGround, 
                           FamiliarityTech = FamiliarityTech, SchoolZoneManual = SchoolZoneManual, 
                           SharedPedestrian = SharedPedestrian, ZipCode = ZipCode, FamiliarityNews = FamiliarityNews,  
                           results=results.content.decode('UTF-8'))
  
