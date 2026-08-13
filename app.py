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
    df = pd.read_csv("data/patients.csv")
    patients_list = df.to_dict(orient="records")
    return render_template(
        "patients.html",
        patients=patients_list,
        total=len(df)
    )

if __name__ == "__main__":
    app.run(debug=True)