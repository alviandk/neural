import numpy as np
from neupy import algorithms, environment

environment.reproducible()
file_name = 'dosen'
data = np.genfromtxt(file_name+'.csv', delimiter=',')
artnet = algorithms.ART1(
    step=2,
    rho=0.7,
    n_clusters=2,
    verbose=False
)
artnet.predict(data)

