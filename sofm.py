import numpy as np
from neupy import algorithms, environment
import time
import pprint

import json

start_time = time.time()

environment.reproducible()
file_name = 'gabung'
data = np.genfromtxt(file_name+'.csv', delimiter=',')
learning_rate=0.005
radius=1
sofm = algorithms.SOFM(
    n_inputs=15,
    n_outputs=4,
    step=learning_rate,
    reduce_step_after=30,

    shuffle_data=True,

    learning_radius=radius,
    reduce_radius_after=30,

    std=2,
    reduce_std_after=30,
    #verbose=True,
    
)
sofm.train(data, epochs=1000)

print(file_name+', learning rate:', learning_rate)
predict_data = sofm.predict(data)

from matplotlib import pyplot as plt


''' graph '''
plt.plot(sofm.errors)
plt.title('data gabungan, learning radius '+str(radius))
plt.xlabel('epoch')
plt.ylabel('error')
#plt.show()
plt.savefig('graph_{}_{}.png'.format(file_name, radius), bbox_inches='tight')

''' print result on screen '''
for d in data:
    print((sofm.predict(np.reshape(d, (15, 1)).T)))


''' export result to csv '''
np.savetxt('result_{}_{}.csv'.format(file_name, radius), sofm.predict(data), delimiter=",")


def roundPartial (value, resolution):
    return round (value / resolution) * resolution

index_cluster = []
centroid_cluster = {}
mapped_centroid_cluster = {}
cluster_member = {}

for data_idx, data in enumerate(predict_data):    
    # find cluster index location of '1' in the data
    cluster_idx = list(data).index(1)
    cluster_idx_1 = cluster_idx + 1

    if cluster_idx not in index_cluster:
        # inititate for determine cluster member and total
        
        cluster_member['cluster_'+str(cluster_idx_1)]={'member': [], 'total': 0}

        # flag, cluster is already in centroid
        index_cluster.append(cluster_idx)

        cluster_list = []
        mapped_cluster_list = []
        # centroid
        for idx, weight in enumerate(sofm.weight):
            # centroid value
            centroid_weight = list(weight)[cluster_idx]
            centroid_weight = abs(centroid_weight)
            cluster_list.append(centroid_weight)
            # mapped centroid value
            if idx == 0:
                mapped_cluster_list.append(roundPartial(centroid_weight, 0.5))
            elif idx == 14:
                mapped_cluster_list.append(
                   float(str(round(roundPartial(centroid_weight, 0.337),2)))
                )
            else:
                mapped_cluster_list.append(round(centroid_weight))
        centroid_cluster['cluster_'+str(cluster_idx_1)] = cluster_list
        mapped_centroid_cluster['cluster_'+str(cluster_idx_1)] = mapped_cluster_list

    # update value cluster member and total
    cluster_member['cluster_'+str(cluster_idx_1)]['member'].append(data_idx+1)
    cluster_member['cluster_'+str(cluster_idx_1)]['total'] += 1

with open('centroid_{}_{}.py'.format(file_name, radius), 'w') as f:
	f.write('centroid cluster\n')
	f.write(json.dumps(centroid_cluster, sort_keys=True))
  f.write('\n')


	f.write('mapped centroid cluster\n')
	f.write(json.dumps(mapped_centroid_cluster, sort_keys=True))
  f.write('\n')

	f.write('cluster member\n')
	f.write(json.dumps(cluster_member, sort_keys=True))
  f.write('\n')
	#f.writeln("--- %s seconds ---" % (time.time() - start_time))

'''
example:
print "Rounding to quarters"
print roundPartial (10.38, 0.25)
print roundPartial (11.12, 0.25)
print roundPartial (5.24, 0.25)
print roundPartial (9.76, 0.25)

print "Rounding to tenths"
print roundPartial (9.74, 0.1)
print roundPartial (9.75, 0.1)
print roundPartial (9.76, 0.1)

print "Rounding to hundreds"
print roundPartial (987654321, 100)
'''
