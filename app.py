from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")