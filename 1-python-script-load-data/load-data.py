import csv
import pymongo

clientConnection = pymongo.MongoClient("mongodb://localhost:27017/")
database = clientConnection["DataScienceDB"]
collection = database["CO2EmissionFromNaturalGas"]

with open('CO2EmissionsFromGaseousFuelConsumption.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    thislist = []

    for row in readCSV:
        thisdict = {
            "Location": row[0],
            "Year": row[1],
            "CO2KilotonnesEmitted": row[2]
        }
        thislist.append(thisdict)
        collection.insert_one(thisdict)