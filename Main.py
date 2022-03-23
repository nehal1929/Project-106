import csv 
import numpy as np
import plotly.express as px

with open("Student Marks vs Days Present.csv") as csv_file:
    df  = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()

def getDataSource(data_path):
    students_marks = []
    days_present = []

    with open(data_path) as csv_file:
        csv_reader  = csv.DictReader(csv_file)
        for row in csv_reader:
            students_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x":students_marks, "y":days_present}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation of students marks and days present.", correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()