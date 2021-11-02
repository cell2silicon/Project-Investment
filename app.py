# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
# from scrape_invest import scrape_info   
 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



# create route that renders index.html template
@app.route("/")
def home():
    
    # results = scrape_info()
    # return render_template("index.html", invest=results)
    return render_template("index.html")

# @app.route("/scrape")
# def scrape():
#     results = scrape_info()
#     return render_template("index.html", invest=results)


if __name__ == "__main__":
    app.run()