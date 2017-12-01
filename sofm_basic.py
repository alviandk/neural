import numpy as np
import matplotlib.pyplot as plt

from neupy import algorithms, environment


environment.reproducible()
plt.style.use('ggplot')


input_data = np.array([
[1.24,1.13,0.92,1.63,0.85],
[0.55,1.13,0.5,1.63,0.85],
[0.51,0.56,1.93,0.71,0.85],
[0.22,1.13,0.68,0.71,0.85],
[1.08,1.13,1.02,0.71,0.36],
[1.04,0.56,0.80,0.71,0.36],
[0.67,0.56,0.06,0.52,1.57],
[1.61,1.13,0.89,0.71,0.36],
[1.08,0.56,1.02,0.71,0.85],
[0.54,1.13,0.36,0.52,1.57],
])
print(input_data)

weight=np.array([
[0.78,0.28],
[0.46,0.63],
[0.37,0.32],
[0.91,0.13],
[0.78,0.11],
])

sofmnet = algorithms.SOFM(
    n_inputs=5,
    n_outputs=2,

    step=0.6,
    reduce_step_after=30,
    show_epoch=5,
    shuffle_data=True,
    verbose=True,
    learning_radius=2,
    reduce_radius_after=30,
    std=2,
    reduce_std_after=30,
)

plt.plot(input_data.T[0:1, :], input_data.T[1:2, :], 'ko')
sofmnet.train(input_data, epochs=60)

print("> Start ")
#plt.xlim(-1, 1.2)
#plt.ylim(-1, 1.2)

#plt.plot(sofmnet.weight[0:1, :], sofmnet.weight[1:2, :], 'bx')
#plt.show()

#for data in input_data:
#    print(sofmnet.predict(np.reshape(data, (5, 1)).T))
print(sofmnet.predict(input_data))

