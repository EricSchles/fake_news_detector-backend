from app import app, db
from flask import request
from flask_cors import cross_origin
from app.models import URLS
import json
#import tools

#http://stackoverflow.com/questions/28461001/python-flask-cors-issue
#http://stackoverflow.com/questions/30717152/python-flask-how-to-set-response-header-for-all-responses
@app.after_request
def after_request(response):
    response.headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": '*',
        "Access-Control-Allow-Methods": 'PUT, GET, POST, DELETE, OPTIONS',
        "Access-Control-Allow-Headers": 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
        }
    return response
# @app.before_request(response)
# def before_request(response):
#     response.headers = {
#         "Content-Type": "application/json",
#         "Access-Control-Allow-Origin": '*',
#         "Access-Control-Allow-Methods": 'PUT, GET, POST, DELETE, OPTIONS',
#         "Access-Control-Allow-Headers": 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
#     }
#     return response


@app.route("/",methods=["GET","POST"])
def index():
    return "server is running"

@app.route("/list_of_urls",methods=["GET","POST"])
def list_of_urls():
    results = [elem.url for elem in URLS.query.all()]
    return json.dumps(results)

@app.route("/send_data",methods=["GET","POST"])
@cross_origin(origin="*",headers=['Content-Type','Authorization'])
def send_data():
    if request.method=="POST":
        data = json.loads(request.json)
        links = tools.find_urls(data["data"])
        for link in links:
            urls = URLS(url=link)
            db.session.add(urls)
            db.session.commit()
    return "data recieved"
