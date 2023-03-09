import csv
# from influxdb_client import InfluxDBClient, Point
import os

# bucket = "current_analysis"

# client = InfluxDBClient(url="http://localhost:8086", token="tAPuFbQb_VlUUWKoZNvNVqSpW3bxPhceYmxyPr9fZa5dVHXN6tLaPNBessi-CHWexnWCV034jY2TisTDmVOcqA==", org="Digital-twin")

# query_api = client.query_api()

# using csv library
# csv_result = query_api.query_csv('from(bucket: "current_analysis")|> range(start: 2022-12-06T07:00:00.000Z, stop: 2022-12-28T14:00:00.000Z)|> filter(fn: (r) => r["_measurement"] == "kafka_consumer")|> filter(fn: (r) => r["_field"] == "value_current_sensor_properties_value")')
# write to csv
file = open(r'/Users/luciosquitieri/Documents/prova.txt', "r")
file1 = open('/Users/luciosquitieri/Documents/ciao.txt', "w")

while True:

    # Get next line from file
    dat = file.readline()
    dat = dat.replace("23T", "18T")
    dat = dat.replace("24T", "19T")
    dat = dat.replace("25T", "20T")
    dat = dat.replace("27T", "21T")
    file1.writelines(dat)
    # if line is empty
    # end of file is reached
    if not dat:
        break


file.close()

# Una volta ottenuto il file CSV, viene eseguito l'altro file .py che provvederà a creare un modello predittivo
# os.system("python3 Modello.py")
