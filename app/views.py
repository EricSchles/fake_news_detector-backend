from app import app, db
from flask import request
from flask_cors import cross_origin
from app.models import URLS
import json
import tools

@app.route("/",methods=["GET","POST"])
def index():
    return "server is running"

@app.route("/list_of_urls",methods=["GET","POST"])
def list_of_urls():
    results = [elem.url for elem in URLS.query.all()]
    return json.dumps(results)

@app.route("/send_data",methods=["GET","POST"])
@cross_origin(origin="https://serene-reef-39081.herokuapp.com/send_data",headers=['Content-Type','Authorization'])
def send_data():
    if request.method=="POST":
        data = json.loads(request.json)
        links = tools.find_urls(data["data"])
        for link in links:
            urls = URLS(url=link)
            db.session.add(urls)
            db.session.commit()
    return "data recieved"
