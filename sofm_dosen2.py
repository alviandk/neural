import numpy as np
from neupy import algorithms, environment

environment.reproducible()

data = np.genfromtxt('dosen.csv', delimiter=',')
learning_rate=0.005
sofm = algorithms.SOFM(
    n_inputs=15,
    n_outputs=10,
    step=learning_rate,
    reduce_step_after=30,

    shuffle_data=True,

    learning_radius=2,
    reduce_radius_after=30,

    std=2,
    reduce_std_after=30,
    #verbose=True,
    
)
sofm.train(data, epochs=1000)

print('dosen, learning rate:', learning_rate)
#print(sofm.predict(data))
# ubah ke csv
index_cluster = []
center_cluster = {}
predict_data = sofm.predict(data)

for data in predict_data:
    idx = list(data).index(1)
    if idx not in index_cluster:
        index_cluster.append(idx)
        print(index_cluster)
        cluster_list = []
        for w in sofm.weight:
            cluster_list.append(list(w)[idx])
        center_cluster['cluster_'+str(idx)] = cluster_list
        print(center_cluster)
    else:
        continue

#for d in data:
#    print((sofm.predict(np.reshape(d, (15, 1)).T)).index(1))
#    break
#np.savetxt("dosen_export.csv", sofm.predict(data), delimiter=",")
print('w')
#print(sofm.weight)
#for w in sofm.weight:
#    print(w)
#    print(w[0], 'wo')
