from flask import Flask, render_template
from datetime import datetime
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    df = pd.read_csv("data/patients.csv")
    return render_template(
        "home.html",
        nurse_name="Jane",
        date=datetime.now().strftime("%A, %d %B %Y"),
        total_patients=len(df),
        waiting=18,
        admissions=7,
        emergency=2
    )

@app.route("/patients")
def patients():
    return "<h1>Patient list</h1>"

@app.route("/appointments")
def appointments():
    return "<h1>Appointments</h1>"


if __name__ == "__main__":
    app.run(debug=True)