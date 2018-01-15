from matplotlib import pyplot

from matplotlib import pyplot as plt
import redis
import sys

plot_type = sys.argv[1]

r = redis.StrictRedis(host='localhost', decode_responses=True, port=6379, db=0)

list_epoch = r.keys("epoch:*")

index = 0
epoch = []
cluster = []
tmax = []
for x in range(len(list_epoch)):
    epoch.append(x)
    epoch_key = "epoch:" + str(x)
    group = r.hgetall(epoch_key)
    cluster.append(int(group["cluster"]))
    tmax.append(float(group["tmax"]))

if plot_type == "cluster":
    plt.plot(epoch, cluster)
    plt.xlabel("epoch")
    plt.ylabel("cluster")
elif plot_type == "tmax":
    plt.plot(epoch, tmax)
    plt.xlabel("epoch")
    plt.ylabel("tmax")
plt.show()
