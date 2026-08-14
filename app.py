from flask import Flask, render_template, request, redirect, url_for
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
@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html", message=None)

@app.route("/register", methods=["POST"])
def register_post():
    from datetime import datetime
    import csv
    import os

    name = request.form["name"]
    phone = request.form["phone"]
    dob = request.form["dob"]
    condition = request.form["condition"]
    allergies = request.form["allergies"]
    emergency_contact = request.form["emergency_contact"]
    location = request.form["location"]
    priority = request.form["priority"]
    date_joined = datetime.now().strftime("%Y-%m-%d")

    patient = {
        "name": name,
        "phone": phone,
        "dob": dob,
        "condition": condition,
        "allergies": allergies,
        "emergency_contact": emergency_contact,
        "location": location,
        "priority": priority,
        "date_joined": date_joined
    }

    file_exists = os.path.exists("data/patients.csv")
    file = open("data/patients.csv", "a", newline="")
    writer = csv.DictWriter(file, fieldnames=patient.keys())
    if not file_exists:
        writer.writeheader()
    writer.writerow(patient)
    file.close()

    return redirect(url_for("patients"))

if __name__ == "__main__":
    app.run(debug=True)