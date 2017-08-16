# Simple script to upload sketches to arduino via windows command line

import subprocess
import win32com.client

# Enter the basic settings here
arduino_path    = "C:\\Program Files (x86)\\Arduino"    # Path to the arduino IDE
action          = " --upload "                          # Command for IDE (--upload or --verify)
filepath        = '"C:\\Users\\Stefan\ Mucha\\arduino_python\\tentacle_setup\\tentacle_setup.ino"'  # Path to Arduino sketch

# Subscript for finding the COM port where the arduino is connected. Only works with one arduino connected!
wmi = win32com.client.GetObject("winmgmts:") #Find com port where Arduino is connected
for port in wmi.InstancesOf("Win32_SerialPort"):
    if "Arduino" in port.Name:
        comPort = ' --port ' + port.DeviceID

command = "cmd /k arduino"+action+filepath+comPort    # Concatenate the single arguments into one command that is passed to the windows cmd.exe

subprocess.Popen(command, cwd=arduino_path)             # sets the arduino path as working directory in cmd.exe and executes the command