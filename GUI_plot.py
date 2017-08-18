# Skript to create a GUI and to implement a live plot of sensor data

import matplotlib
matplotlib.use("TkAgg")     # Specify the correct backend to work with Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

