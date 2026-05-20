import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# PHYSICAL PARAMETERS
# -----------------------------

m = 1.0       # mass
k = 1.0       # spring constant
b = 0.2       # damping coefficient

# -----------------------------
# TIME SETTINGS
# -----------------------------

dt = 0.01                 # time step
t_max = 20                # total simulation time

t = np.arange(0, t_max, dt)

# -----------------------------
# ARRAYS
# -----------------------------

x = np.zeros(len(t))      # position array
v = np.zeros(len(t))      # velocity array

# -----------------------------
# INITIAL CONDITIONS
# -----------------------------

x[0] = 1.0                # initial displacement
v[0] = 0.0                # initial velocity

# -----------------------------
# EULER METHOD SIMULATION
# -----------------------------

for i in range(len(t) - 1):

    # acceleration equation
    a = -(b/m) * v[i] - (k/m) * x[i]

    # update velocity
    v[i+1] = v[i] + a * dt

    # update position
    x[i+1] = x[i] + v[i+1] * dt

# -----------------------------
# PLOT 1: POSITION VS TIME
# -----------------------------

plt.figure(figsize=(10,5))
plt.plot(t, x)

plt.title("Damped Harmonic Oscillator")
plt.xlabel("Time")
plt.ylabel("Displacement")

plt.grid()

plt.savefig("displacement_vs_time.png")

# -----------------------------
# PLOT 2: VELOCITY VS TIME
# -----------------------------

plt.figure(figsize=(10,5))
plt.plot(t, v)

plt.title("Velocity vs Time")
plt.xlabel("Time")
plt.ylabel("Velocity")

plt.grid()

plt.savefig("velocity_vs_time.png")

# -----------------------------
# PLOT 3: PHASE SPACE
# -----------------------------

plt.figure(figsize=(6,6))
plt.plot(x, v)

plt.title("Phase Space Plot")
plt.xlabel("Displacement")
plt.ylabel("Velocity")

plt.grid()

plt.savefig("phase_space.png")

# -----------------------------
# SHOW ALL PLOTS
# -----------------------------

plt.show()