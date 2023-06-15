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
    FamiliarityTech = request.form.get("FamiliarityTech")
    SharePerformanceData = request.form.get("SharePerformanceData")
    ReportSafetyIncident = request.form.get("ReportSafetyIncident")
    ArizonaCrash = request.form.get("ArizonaCrash")
    Speed25Mph = request.form.get("Speed25Mph")
    ProvingGround = request.form.get("ProvingGround")
    AvImpact = request.form.get("AVImpact")
    SchoolZoneManual = request.form.get("SchoolZoneManual")

    #convert data to json
    input_data = json.dumps({"FamiliarityTech": FamiliarityTech, "SharePerformanceData": SharePerformanceData, 
                            "ReportSafetyIncident": ReportSafetyIncident, "ArizonaCrash": ArizonaCrash, 
                            "Speed25Mph": Speed25Mph, "ProvingGround": ProvingGround, "AVImpact": AvImpact, 
                            "SchoolZoneManual": SchoolZoneManual})
    

    #url for AV model
    #url = "http://localhost:3000/api" #for local machine testing
    url = "hhttps://av-model-app-6f2c9d64a330.herokuapp.com/api" #for hosting on Heroku
  
    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", FamiliarityTech = FamiliarityTech, SharePerformanceData = SharePerformanceData,
                           ReportSafetyIncident = ReportSafetyIncident, ArizonaCrash = ArizonaCrash, Speed25Mph = Speed25Mph,
                           ProvingGround = ProvingGround, AVImpact = AvImpact, SchoolZoneManual = SchoolZoneManual,
                           results=results.content.decode('UTF-8'))