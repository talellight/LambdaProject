from body import Body
import math

# Gravitational constant (SI units)
G = 6.67430e-11  # m^3 kg^-1 s^-2

def compute_force(body1, body2):
    """
    Compute gravitational force on body1 from body2.
    Returns a list [fx, fy].
    """
    dx = body2.pos[0] - body1.pos[0]
    dy = body2.pos[1] - body1.pos[1]
    distance_squared = dx**2 + dy**2

    if distance_squared == 0:
        return [0, 0]  # avoid division by zero

    force_magnitude = G * body1.mass * body2.mass / distance_squared
    distance = math.sqrt(distance_squared)

    fx = force_magnitude * dx / distance
    fy = force_magnitude * dy / distance

    return [fx, fy]

def simulate(bodies, dt, steps):
    """
    Simulate movement of bodies under gravity.
    
    bodies: list of Body objects
    dt: timestep in seconds
    steps: number of steps to simulate
    """
    for step in range(steps):
        # Step 1: calculate forces
        forces = {body: [0, 0] for body in bodies}
        for i, body1 in enumerate(bodies):
            for j, body2 in enumerate(bodies):
                if i != j:
                    fx, fy = compute_force(body1, body2)
                    forces[body1][0] += fx
                    forces[body1][1] += fy

        # Step 2: update velocities and positions
        for body in bodies:
            ax = forces[body][0] / body.mass
            ay = forces[body][1] / body.mass
            body.vel[0] += ax * dt
            body.vel[1] += ay * dt
            body.pos[0] += body.vel[0] * dt
            body.pos[1] += body.vel[1] * dt

        # Step 3: print positions for this step
        print(f"Step {step}:")
        for body in bodies:
            print(f"  {body}")
        print("-" * 40)  # separator for readability

