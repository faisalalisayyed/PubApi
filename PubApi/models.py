from PubApi import db

class Submit_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_email = db.Column(db.String(100), nullable=False)
    api_name = db.Column(db.String(100), nullable=False)
    api_desc = db.Column(db.String(1000), nullable=False)
    api_auth = db.Column(db.String(100), nullable=False)
    api_https = db.Column(db.Boolean, nullable=False)
    api_cors = db.Column(db.Boolean, nullable=False)
    api_link = db.Column(db.String(100), nullable=False)
    api_category = db.Column(db.String(100), nullable=False)
