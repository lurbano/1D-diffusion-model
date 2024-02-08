# 1D-diffusion-model

````diffModel.py```` is the temperature model, but it works the same as diffusion of anything (you can change T to h and call it a height model). 

This is basically a conservation model. In this case, it gets the difference between heat flow into a cell (Qin) and the flow out (Qout), with any difference resulting in a change in temperature (see the timestep loop). 

The flow values (Qin and Qout) depend on difference in height between adjacent cells. For cell i:

$$ Q_in = K A \frac{T_i - T_{i-1}}{\Delta x}  $$
