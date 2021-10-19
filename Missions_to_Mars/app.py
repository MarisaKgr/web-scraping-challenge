from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars


app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
    mars_data = mongo.db.mars_dict.find_one()

    return render_template("index.html", mars_dict=mars_data)


@app.route("/scrape")
def scrape():


    mars_dict = scrape_mars.scrape_info()
    mongo.db.mars_dict.update({}, mars_dict, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)



