# 1D-diffusion-model

````diffModel.py```` is the temperature model, but it works the same as diffusion of anything (you can change T to h and call it a height model). 

This is basically a conservation model. In this case, it gets the difference between heat flow into a cell ($Q_{in}$) and the flow out ($Q_{out}$), with any difference resulting in a change in temperature (see the timestep loop). 

The flow values ($Q_{in}$ and $Q_{out}$) depend on difference in height between adjacent cells. For cell $i$, this is the gradient between the $i$ and the $i-1$ cell:

$$ Q_{in} = - K A \frac{T_i - T_{i-1}}{\Delta x}  $$

The code uses numpy array slicing to do all the cells at the same time. 

```python
    Qin = -K * A * (T[1:-1] - T[:-2]) / dx
```

Changing the $K$ coefficient will change how fast the model reacts over time, which means that you can use this to calibrate your model if you have data to compare it to.

### Boundary Conditions
````diffModel.py```` uses the simplest boundary conditions: fixed on both sides. Since, the boundary values don't change we don't even update the temperature values at the boundaries (```T[1:-1] += Qin + Qout```).



