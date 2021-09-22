from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(application)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(300), nullable=False)
    barcode = db.Column(db.String(300), nullable=False)
    qutype = db.Column(db.Integer)
    vendor = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer)
    currency = db.Column(db.String(300), nullable=False)

def __repr__(self):
    return '<Article %r>' % self.id




@application.route("/")
def index():
    return render_template("index.html")




#------Main---------

if __name__== "__main__":
    application.debug = True
    application.run()
