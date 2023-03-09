from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((150, 400), (150, 0))
])

sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': [
        [1, {"path": [0, 0]}],
        [1, {"path": [0, 0]}],
        [1, {"path": [0, 0]}],
        [1, {"path": [0, 0]}]
    ]
})

#sim.create_signal([[0], [2]])

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=3)