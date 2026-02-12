class Body:
    def __init__(self, name, mass, x, y, vx=0, vy=0):
        self.name = name       # The Object's Name
        self.mass = mass       # Mass in Kilograms
        self.pos = [x, y]      # Position in a 2D Environment (X and Y, in Meters)
        self.vel = [vx, vy]    # Velocity as in the 2D Environment (Velocity = Meters per Second, m/s)

    def __repr__(self):
        return f"{self.name}: pos={self.pos}, vel={self.vel}"


