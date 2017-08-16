import serial
import win32com.client
import datetime
import csv

# Define basic variables
connected = False       # Boolean to represent whether Arduino is connected or not
DO      = [0]           # Variable to hold DO values
Temp    = [0]           # Variable to hold temperature values
headers = ["Time", "DO", "Temperature"] # Headers of the columns in .csv output
csv_filename = datetime.datetime.now().strftime("%Y-%m-%d")  # Name .csv file with today's date

# Write headers as first row in .csv file
with open('csv_output/%s.csv' %(csv_filename), 'w') as f:
    w = csv.writer(f, delimiter = ",", lineterminator = "\n")
    w.writerow(headers)

# Find com port where arduino is connected
wmi = win32com.client.GetObject("winmgmts:")
for port in wmi.InstancesOf("Win32_SerialPort"):
    if "Arduino" in port.Name:
        comPort = port.DeviceID
        print(comPort, "is Arduino")

ser = serial.Serial(comPort, 9600)          # Read the com-port where the Arduino is connected

# Loop until the arduino tells us it's ready
while not connected:
    serin = ser.read()
    connected = True

# Loop that runs while the arduino sends data
while True:
    data = ser.readline()                   # Read serial input until it gets a carriage return
    data = data.decode().strip("\r\n")      # Strip serial read from carriage return
    sep = data.split("\t")                  # Make list from serial read, split by tab
    DO.append(sep[0])                       # Add DO value
    Temp.append(sep[1])                     # Add Temp value
    del(DO[0])                              # Delete old DO value from holding variable
    del(Temp[0])                            # Delete old temperature value from holding variable
    row = [datetime.datetime.now().strftime("%X"), DO[0], Temp[0]]
    with open('csv_output/%s.csv' %(csv_filename), 'a') as f:
        w = csv.writer(f, delimiter = ",", lineterminator = "\n")
        w.writerow(row)
    print(row)
