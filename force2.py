momentum = lambda mass,velocity:mass*velocity
mass = float(input())
velocity = float(input())
s = momentum(mass,velocity)
print("{:.2f}".format(s))