from app import db

class URLS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(900))

    def __init__(self,url):
        self.url = url

    def __repr__(self):
        return '<url {}>'.format(self.url)
