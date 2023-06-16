from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#Access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#Access the service
@app.route("/avclassify", methods=['GET', 'POST'])
def avclassify():

    #Get inputs from index.html
    FamiliarityTech = request.form.get("FamiliarityTech")
    SharePerformanceData = request.form.get("SharePerformanceData")
    ReportSafetyIncident = request.form.get("ReportSafetyIncident")
    ArizonaCrash = request.form.get("ArizonaCrash")
    Speed25Mph = request.form.get("Speed25Mph")
    ProvingGround = request.form.get("ProvingGround")
    AvImpact = request.form.get("AvImpact")
    SchoolZoneManual = request.form.get("SchoolZoneManual")

    #Convert the inputs from index.html to json data
    input_data = json.dumps({"FamiliarityTech": FamiliarityTech, "SharePerformanceData": SharePerformanceData, 
                            "ReportSafetyIncident": ReportSafetyIncident, "ArizonaCrash": ArizonaCrash, 
                            "Speed25Mph": Speed25Mph, "ProvingGround": ProvingGround, "AvImpact": AvImpact, 
                            "SchoolZoneManual": SchoolZoneManual})
    

    #url for AV model
    #url = "http://localhost:3000/api" #used for local machine testing - comment out when using Heroku
    url = "https://av-model-app-6f2c9d64a330.herokuapp.com/api" #for hosting on Heroku - comment out if local testing
  
    #Sends POST request to the API with data input from index.html
    results =  requests.post(url, input_data)

    #Sends user input and the model prediction to index.html to be displayed
    return render_template("index.html", FamiliarityTech = FamiliarityTech, SharePerformanceData = SharePerformanceData,
                           ReportSafetyIncident = ReportSafetyIncident, ArizonaCrash = ArizonaCrash, Speed25Mph = Speed25Mph,
                           ProvingGround = ProvingGround, AvImpact = AvImpact, SchoolZoneManual = SchoolZoneManual,
                           results=results.content.decode('UTF-8'))