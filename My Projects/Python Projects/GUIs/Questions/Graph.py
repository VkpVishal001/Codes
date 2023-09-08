from PyQt5 import QtWidgets, QtGui, QtCore, uic

import matplotlib
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NTB

import math
import sys


class Class(QtWidgets.QDialog):

    def __init__(self):
        super(Class, self).__init__()

        uic.loadUi("Z_Graph.ui", self)

        self.pushButton_1.clicked.connect(self.plot)

        self.figure = plt.figure()
        self.canvas = FigCanvas(self.figure)
        self.tools = NTB(self.canvas, self)

        self.show()

    def plot(self):
        velocity = float(self.lineEdit_1.text())
        angle = float(self.lineEdit_2.text())

        g = 9.8

        angle1 = math.radians(angle)
        angle2 = math.radians(2*angle)

        sine = round(math.sin(angle1), 2)
        sine2 = round(math.sin(angle2), 2)
        cosine = round(math.cos(angle1), 2)

        time = int(2*velocity*sine / g)
        height = round((g*(time**2)) / 8, 2)
        distance = round(height * 4 * (cosine/sine), 2)

        distances = []
        heights = []

        height1 = 0
        distance1 = 0

        for i in range(100):
            time1 = round(time / 100, 2)
            velocity1 = round(velocity / 100, 2)

            if i<50:
                height1 += (g*(((time1 / 2) * (50-i)) ** 2)) / 8
            elif i>49:
                height1 -= (g*(((time1 / 2) * (i-49)) ** 2)) / 8

            distance1 += velocity1 * cosine * time

            distances.append(distance1)
            heights.append(height1)

        plt.xlim(0,math.ceil(max(height,distance1)))
        plt.ylim(0,math.ceil(max(height,distance1)))

        plt.plot(distances,heights)
        plt.show()

app = QtWidgets.QApplication(sys.argv)
window = Class()
app.exec_()