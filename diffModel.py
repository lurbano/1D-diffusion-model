'''
1D transient, diffusional model between two fixed boundary conditions.
'''
import numpy as np
import time
from ezGraph import *

''' Prameters '''
# SPATIAL PARAMETERS
n = 10      # number of cells in model
dx = 1      # width of cell
A = 1       # area of cell

# TIME PARAMETERS
tsteps = 500    # number of timesteps
dt = 0.1        # timestep

K = 0.1         # diffusion coefficient
V = A * dx


''' Initial Conditions '''
# INITIAL TEMPERATURE
T = np.ones((n,)) * 5   # Temperature everywhere is 5

# BOUNDARY CONDITIONS
T[0] = 5                # left boundary fixed at 5
T[n-1] = 10             # right boundary fixed at 10 


''' Initialize Graph'''
# SET UP GRAPH
graph = ezGraph()
graph.plot(T)
graph.wait(1)
print(f"-1: T")

''' MODEL TIMESTEPS '''
for t in range(tsteps):
    # flow into cell (Qin)
    Qin = -K * A * (T[1:-1] - T[:-2]) / dx
    # flow out of cell (Qout)
    Qout = K * A * (T[2:] - T[1:-1]) / dx   
    # change in temperature
    T[1:-1] += Qin + Qout

    # update graph ocassionally
    if (t%10 == 0):
        graph.updatePlot(T, dt=0.1, title=f"{t+1}/{tsteps}")
    

# DRAW fINAL GRAPH
graph.updatePlot(T, dt=0.1, title=f"{t+1}/{tsteps}")       # final update
graph.keepOpen()    # keep graph open when done
