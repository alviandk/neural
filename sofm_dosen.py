import numpy as np
from neupy import algorithms, environment

environment.reproducible()

data = np.genfromtxt('dosen.csv', delimiter=',')
learning_rate=0.005
sofm = algorithms.SOFM(
    n_inputs=15,
    n_outputs=6,
    step=learning_rate,
    reduce_step_after=30,

    shuffle_data=True,

    learning_radius=3,
    reduce_radius_after=30,

    std=2,
    reduce_std_after=30,
    
)
sofm.train(data, epochs=90)

print('dosen, learning rate:', learning_rate)
print(sofm.predict(data))
