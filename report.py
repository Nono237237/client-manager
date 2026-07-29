import pandas as pd
from datetime import datetime
import os

os.makedirs("reports", exist_ok=True)

df = pd.read_csv("data/clients.csv")

today = datetime.now().strftime("%Y-%m-%d")
report_file = "reports/client_report_" + today + ".txt"

file = open(report_file, "w")

file.write("=" * 40 + "\n")
file.write("CLIENT MANAGER - BUSINESS REPORT\n")
file.write("Generated: " + today + "\n")
file.write("=" * 40 + "\n\n")

file.write("TOTAL CLIENTS: " + str(len(df)) + "\n\n")

file.write("CLIENTS BY BUSINESS TYPE:\n")
file.write("-" * 30 + "\n")
business_counts =df["business"].value_counts()
for business, count in business_counts.items():
    file.write(str(business)     + ": " + str(count) + "\n")

file.write("\nCLIENTS BY LOCATION:\n")
file.write("-" * 30 + "\n")
location_counts = df["location"].value_counts()
for location, count in location_counts.items():
    file.write(str(location)  + ": " + str(count) + "\n")

file.write("\nFULL CLIENT LIST:\n")
file.write("-" + "-" * 30 + "\n")
for _, row in df.iterrows():
    name = str(row["name"])
    business = str(row["business"])
    location = str(row["location"]) if str(row["location"]) != "nan" else "N/A"
    file.write(name + " | " + business + " | " + location + "\n")

file.write("\n" + "=" * 40 + "\n")
file.write("END OF REPORT\n")
file.close()

print("Report saved to: " + report_file)

