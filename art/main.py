from libs.tanimoto import tanimoto
import redis

r = redis.StrictRedis(host='localhost', decode_responses=True, port=6379, db=0)
r.flushdb()

import sys
import csv
import uuid
import ast

# get argumen from terminal
file_input = sys.argv[1]
koefisien = sys.argv[2]

# openin CSV file
file_open = open(file_input, 'r')
csv_lists = csv.reader(file_open)

index = 0
# loop by number of line in csv file
for datax in csv_lists:
    # print(datax)
    # generate database key from input data
    data_id = "data:" + str(uuid.uuid4())
    # Query all data keys in redis database
    item_keys = r.keys("data:*")
    print("jumlah data: " + str(len(item_keys)))
    print("--------------------")

    # Jika belum ada data sama sekali

    if len(item_keys) == 0:
        # generate "new group key"
        group_key = "group:" + str(uuid.uuid4())
        data_key = data_id
        # value dari key data, di tambah komponen group
        value_data = {"group": group_key, "data": datax}
        # simpan value_data dengan data_key ke database
        r.hmset(data_key, value_data)
        # menambahkan data_key ke group
        r.sadd(group_key, data_key)
        cluster_count = len(r.keys("group:*"))
        epoch_value = {"cluster": str(cluster_count), "tmax": "1"}
        r.hmset("epoch:0", epoch_value)

    else:
        blo = []  # variable menyimpan hasil pengecekan data inputan dengan data yang ada di database
        for item_key in item_keys:
            # Mengektrak isi data dari menggunkan semua key yg ada di database
            data = r.hgetall(item_key)
            # Meubah data yang ada (string) ke format list
            list_data = ast.literal_eval(data["data"])
            # Menghitung koefieisen tanimoto hanya dari kolom 3-17
            tanimoto_val = tanimoto(datax[1 - 16:], list_data[1 - 16:]).check()
            # Data hasil pengechekan
            data_check = {"key": item_key, "tanimoto": str(tanimoto_val)}
            # memasukan data hasil pengchekan ke list "blo"
            blo.append(data_check)


        lst_value = []  # variabel menyimpan semua nilai tanimoto
        # proses mengumpulkan hasil nilai tanimoto
        for x in blo:
            lst_value.append(float(x["tanimoto"]))
        new_data = max(lst_value)  # mencari nilai tanimoto yg terbesar

        # jika tanimoto lebih kecil dari koefisien
        if float(new_data) < float(koefisien):
            print("bedaaaaaaaaaaaa")
            # buat kunci untuk group dan data
            group_key = "group:" + str(uuid.uuid4())
            data_key = data_id
            # value dari data
            value_data = {"group": group_key, "data": datax}
            # memasukan data ke database berdsarkan key, dan memasukan keynya ke group baru
            r.hmset(data_key, value_data)
            r.sadd(group_key, data_key)
        else:
            print("sama")
            # Query berdasarkan tanimoto terbesar di list blo
            get_key = [element for element in blo if element['tanimoto'] == str(new_data)]
            print(str(get_key[0]))
            # Query data bersarkan key data yang memiliki tanimoto terbesar
            get_data = r.hgetall(get_key[0]["key"])
            # Data untuk disimpan
            value_data = {"group": get_data["group"], "data": datax}
            # memasukan data ke database berdsarkan key, dan memasukan keynya ke group baru
            r.hmset(data_id, value_data)
            r.sadd(get_data["group"], data_id)
        cluster_count = len(r.keys("group:*"))
        index += 1
        epoch_key = "epoch:" + str(index)
        epoch_value = {"cluster": str(cluster_count), "tmax": new_data}
        r.hmset(epoch_key, epoch_value)
