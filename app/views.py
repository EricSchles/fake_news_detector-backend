from app import app, db
from flask import request
from app.models import URLS
import json

@app.route("/list_of_urls",methods=["GET","POST"])
def list_of_urls():
    results = [elem.url for elem in URLS.query.all()]
    return json.dumps(results)

@app.route("/send_data",methods=["GET","POST"])
def send_data():
    if request.method=="POST":
        data = request.json
        urls = URLS(url=data["url"])
        db.session.add(urls)
        db.session.commit()
    return "data recieved"
