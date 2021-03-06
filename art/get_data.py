import redis
r = redis.StrictRedis(host='localhost', decode_responses=True, port=6379, db=0)


import sys

# Mengabil darta dari argumen
nama_file = sys.argv[1]
# Membuka File
file = open(nama_file, "a")
# Mengekstrak semua group key
groups_data = r.keys("group:*")
print("jumlah cluster: "+ str(len(groups_data)))

# Menulis jumlah kluster ke database
file.writelines("jumlah cluster: ," + str(len(groups_data)) + "\n")

# Melakukan loop berdasarkan jumlah group
for index, group_data in enumerate(groups_data):
    # menmpilkan angota dari group
    all_members = r.smembers(group_data)
    print("cluster", index+1)
    print("jumlah anggota:", len(all_members))
    # Menulis ke file
    file.write("cluster {} \n".format(index+1))
    file.write("jumlah anggota: {} \n".format(len(all_members)))
    print("------------------")
    # Loop berdasarkan anggota group
    for all_member in all_members:
        # Mengambil isi data berdasarkan Key data yang ada pada group
        data = r.hgetall(all_member)
        print(data["data"])
        # menghilangkan karakter tidak terpakai di csv ([,], ')
        data_prepro = data["data"].replace("[", "").replace("]", "").replace("'", "")
        # menulis data_repro ke file
        file.write(data_prepro + "\n")
    print("------------------")
file.close()

