#!/usr/bin/python3
#coding: utf-8

import sys
from PySide.QtCore import *
from PySide.QtGui import *

# Greetings
def sayHello():
    print("Hello World!")

# Create the Qt Application
app = QApplication(sys.argv)

# Create a button
button = QPushButton("Click me")

# Connect the button to the function
button.clicked.connect(sayHello)

# Show the button
button.show()

# Run the main Qt loop
app.exec_()