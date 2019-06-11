import time 
import requests
from flask import Flask
app = Flask(__name__)
#Making api for ai
@app.route("/getWeather/5day/<zip>")
def getWeather(zip):
    url = "https://api.openweathermap.org/data/2.5/forecast?zip="+zip+"&appid=f660f63979ecdd0d09a5e0f647bdd34b"
    r = requests.get(url)
    weather = r.json()
    return str(weather)