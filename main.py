from body import Body
from simulation import simulate

# Create bodies
sun = Body("Sun", 1.989e30, 0, 0)
earth = Body("Earth", 5.972e24, 1.496e11, 0, 0, 29780)

bodies = [sun, earth]

# Simulate 24 hours with 1-hour timestep
simulate(bodies, dt=3600, steps=24)

