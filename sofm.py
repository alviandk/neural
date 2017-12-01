import numpy as np
from neupy import algorithms, environment

environment.reproducible()

data = np.array([
    [0.1961, 0.9806],
    [-0.1961, 0.9806],
    [-0.5812, -0.8137],
    [-0.8137, -0.5812],
])

sofm = algorithms.SOFM(
    n_inputs=2,
    n_outputs=2,
    step=0.1,
    learning_radius=0
)
sofm.train(data, epochs=100)
sofm.predict(data)
