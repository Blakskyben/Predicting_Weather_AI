import time 
import requests
import pymongo as mongo
from flask import Flask

#get the db all set up
myClient = mongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["requests"]
entries = mydb["entries"]

app = Flask(__name__)
#Making api for ai
@app.route("/getWeather/5day/<zip>")
def getWeather(zip):
    url = "https://api.openweathermap.org/data/2.5/forecast?zip="+zip+"&appid=f660f63979ecdd0d09a5e0f647bdd34b"
    r = requests.get(url)
    weather = r.json()
    return str(weather)

@app.route("/getWeather/currentWeather/<zip>")
def get(zip):
    url = "https://api.openweathermap.org/data/2.5/weather?zip="+zip+"&appid=f660f63979ecdd0d09a5e0f647bdd34b"
    r = requests.get(url)
    weather = r.json()
    return str(weather)

#Making api for "requesting to predict the weather"
@app.route("/requestPrediction/",methods=[post])
def postPredict():
    entry={humidity:}