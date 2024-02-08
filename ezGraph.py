import matplotlib.pyplot as plt
import numpy as np

class ezGraph:
    def __init__(self, xmin=0, xmax=10, ymin="auto", ymax="auto", xLabel="x", yLabel="y", aspectRatio="equal", line=True, scatter=True, drawAxes=True):
        self.x = []          
        self.y = []
        self.line = line
        self.scatter = scatter
        self.fig, self.ax = plt.subplots()    # initialize matplotlib plot
        plt.xlim(xmin, xmax)
        if ymin != "auto" and ymax != "auto":
            plt.ylim(ymin, ymax)
        self.xLabel, self.yLabel = xLabel, yLabel
        self.setLabels()
        if aspectRatio == "equal":
            self.ax.set_aspect('equal', adjustable='box')

        if drawAxes:
            self.xaxis = self.ax.plot([xmin,xmax], [0, 0])
            self.yaxis = self.ax.plot([0, 0], [ymin, ymax])

        if self.line:
            self.mainLine = self.ax.plot(self.x, self.y, color='blue')               # put data into plot (line)
        if self.scatter:
            self.mainScatter = self.ax.scatter(self.x, self.y) 

    def setLabels(self):
        self.ax.set_xlabel(self.xLabel)  # label axes
        self.ax.set_ylabel(self.yLabel)  # label axes

    def add(self, x, y):
        self.x.append(x)
        self.y.append(y) 
        # self.clear()
        self.setLabels()
        if self.line:
            l = self.mainLine.pop(0)
            l.remove()
            self.mainLine = self.ax.plot(self.x, self.y, color='blue')               # put data into plot
        if self.scatter:
            self.ax.scatter(self.x, self.y)
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        

    def plot(self, y, dx=1):
        self.x = np.ones(y.shape) 
        for i in range(len(self.x)):
            self.x[i] = i * dx
        self.y = y 
        self.ax.plot(self.x, self.y)               # put data into plot
        self.ax.scatter(self.x, self.y)

    def update_xy(self, x, y):
        self.x = x
        self.y = y
        if self.line:
            self.ax.plot(self.x, self.y)               # put data into plot
        if self.scatter:
            self.ax.scatter(self.x, self.y)

        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        self.ax.autoscale()

    def updatePlot(self, y, dt=0.25, title="Plot", dx=1):
        self.clear()
        self.plot(y, dx)
        self.title(title)
        self.wait(dt)

    def wait(self, dt):
        plt.pause(dt)

    def keepOpen(self):
        plt.show()

    def clear(self):
        plt.cla()

    def title(self, txt="Plot"):
        self.ax.set_title(txt)
        



class ezGraphMM:
    def __init__(self, xmin="auto", xmax="auto", ymin="auto", ymax="auto", xLabel="x", yLabel="y", x_measured=[], y_measured=[]):
        self.measured = {
            "x": [],
            "y": []
        }
        self.modeled = {
            "x": [],
            "y": []
        }

        self.fig, self.ax = plt.subplots()    # initialize matplotlib plot
        if xmin != "auto" and xmax != "auto":
            plt.xlim([xmin, xmax])
        if ymin != "auto" and ymax != "auto":
            plt.ylim([ymin, ymax])
        self.xLabel, self.yLabel = xLabel, yLabel
        self.setLabels()
        self.ax.plot(self.modeled["x"], self.modeled["y"])               # put data into plot (line)
        self.ax.scatter(self.modeled["x"], self.modeled["y"]) 

        self.addMeasured(x_measured, y_measured)
        #self.ax.scatter(x_measured, y_measured)
        
    def setLabels(self):
        self.ax.set_xlabel(self.xLabel)  # label axes
        self.ax.set_ylabel(self.yLabel)  # label axes

    def addMeasured(self, xarr, yarr):
        self.measured["x"] = xarr
        self.measured["y"] = yarr
        self.plotMeasured()

    def plotMeasured(self):
        self.clear()
        self.setLabels()
        self.ax.scatter(self.measured["x"], self.measured["y"])

    def addModeled(self, x, y):
        self.modeled["x"].append(x)
        self.modeled["y"].append(y) 
        self.plotModeled()

    def plotModeled(self):
        self.clear()
        self.setLabels()
        self.plotMeasured()
        self.ax.plot(self.modeled["x"], self.modeled["y"])               # put data into plot
        self.ax.scatter(self.modeled["x"], self.modeled["y"])

    def wait(self, dt):
        plt.pause(dt)

    def keepOpen(self):
        plt.show()

    def clear(self):
        plt.cla()

    def title(self, txt="Plot"):
        self.ax.set_title(txt)
        