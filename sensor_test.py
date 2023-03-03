import board
import adafruit_scd30
import csv
import datetime
from time import sleep

scd = adafruit_scd30.SCD30(board.I2C()) #Creates a sensor object

titles = ['Day', 'Hour', 'Temperature (C)', 'Humidity (%)', 'CO2 (PPM)']

with open ('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(titles)

while True:
    ct = datetime.datetime.now()
    day = ct.day
    hour = ct.hour
    co2= round(scd.CO2,1) #reads carbon dioxide
    temp = round(scd.temperature, 1) #reads temp in C
    humidity = round(scd.relative_humidity, 1) #reads relative humidity

    print("CO2: ", co2, "PPM")
    print("Temperature: ", temp, "degrees C")
    print("Humidity: ", humidity, "%")
    
    data = (day, hour, temp, humidity, co2)
    
    with open ('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    sleep(2) #Choose your frequency here