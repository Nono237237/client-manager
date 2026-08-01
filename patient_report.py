import pandas as pd
from datetime import datetime
import os

os.makedirs("reports", exist_ok=True)

df = pd.read_csv("data/patients.csv")

today = datetime.now().strftime("%Y-%m-%d")
report_file = "reports/patient_report_" + today + ".txt"

file = open(report_file, "w")

file.write("=" * 45 + "\n")
file.write(" CLINIC PATIENT REPORT\n")
file.write(" Generated: " + today + "\n")
file.write("=" * 45 + "\n\n")

#Total number of patients
file.write("TOTAL NUMBER OF PATIENTS: " + str(len(df)) + "\n\n")

#Conditions breakdown
file.write("PATIENTS BY CONDITION:\n")
file.write("-" * 30 + "\n")
for condition, count in df["condition"].value_counts().items():
    file.write(condition + ": " + str(count) + "\n")

#Cities breakdown
file.write("\nPATIENTS BY CITY:\n")
file.write("-" * 30 + "\n")
for city, count in df["location"].value_counts().items():
    file.write(str(city) + ": " + str(count) + "\n")

#Most common condition
top_condition = df["condition"].value_counts().index[0]
file.write("\nMOST COMMON CONDITION: " + top_condition + "\n")

#Most patients from a city
top_city = df["location"].value_counts().index[0]
file.write("MOST PATIENTS FROM: " + top_city + "\n")

file.write("\n" + "=" * 45 + "\n")
file.write("END OF REPORT\n")
file.close()

print("Report saved to: " + report_file)
