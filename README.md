# A project to read sensor data from Arduino and upload sketches via a python-based GUI
In this project, I try to connect the power of Python with the versatility of arduino microcontrollers. I work at the Humboldt-University of Berlin and try to build my own setup to monitor dissolved oxygen (DO) and temperature in water. In a second step I then want to control the gas flow into the water through solenoid valves or gas mixing devices.

Note: as a biologist, I'm a newbie when it comes to programming. This is my first programming project, so helpful comments are greatly appreciated and please be gentle - it's my first time.

# System components
I currently work with Python 3.6 and arduino IDE 1.8.2 on a windows-10 machine and try to keep this project compatible with recent updates.
I use the following hardware components:
- Arduino Uno rev. 3 ([link](https://store.arduino.cc/arduino-uno-rev3))
- Atlas Scientific dissolved oxygen probe ([link](https://www.atlas-scientific.com/product_pages/probes/do_probe.html))
- Atlas Scientific temperature probe ([link](https://www.atlas-scientific.com/product_pages/probes/pt1000.html))
- Atlas Scientific EZO DO circuit for dissolved oxygen probe ([link](https://www.atlas-scientific.com/product_pages/circuits/ezo_do.html))
- Atlas Scientific EZO RTD circuit for temperature probe ([link](https://www.atlas-scientific.com/product_pages/circuits/ezo_rtd.html))
- Whitebox Tentacle Shield for Arduino ([link](https://www.whiteboxes.ch/shop/tentacle/))

The EZO circuits are SMBus/I2C slave devices that communicate sensor data to the arduino and integrate some functionality like temperature, pressure and salinity compensation, calibration, conversion between different units. Read and write operations are done by accessing 42 different 8-bit registers. The tentacle shield connects the atlas scientific probes and circuits to the arduino. Through the supplied arduino-sketch ([link](https://raw.githubusercontent.com/whitebox-labs/tentacle-examples/master/arduino/tentacle-setup/tentacle_setup/tentacle_setup.ino)), it forwards serial monitor inputs to the sensor circuits and returns sensor readings over the serial bus. 
The pros of this setup:
- cheap (ca. 380€ total investment)
- EZO circuits are compatible with any temperature or DO-sensor
- Tentacle shield offers quick start without much coding

The cons:
- EZO circuits are patent-protected and do some black-box stuff (e.g. temperature-compensation) that could mess with your readings
- more expensive than completely DIY solutions

# First step: upload sketches to arduino via Python
Since arduino IDE 1.5, it is possible to upload sketches to the arduino via the command line (check out [this](https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc) manual to learn the commands). In a first step, I want to write a short Python skript that allows me to input a filepath to an .ino sketch which it will then upload to the arduino. Later, this should be integrated into the main program.

Update: finished a first simple python script that does upload sketches to the arduino via the windows cmd.exe: sketch_upload.py
