import redis
import csv
import uuid
import pandas as pd
import ast

from django.shortcuts import render
from django.http import HttpResponse

from .forms import SurveyForm, IdentityForm, LimitForm

questions = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6',
             'question_7', 'question_8', 'question_9', 'question_10', 'question_11', 'question_12',
             'question_13', 'question_14', 'question_15'
            ]
cluster_1 = ['A', 'Y', 'Y', 'Y', 'I', 'C', 'G', 'Y', 'Y', 'Y', 'WM', 'Y', 'WL', 'Y', 'S']
cluster_2 = ['B', 'Y', 'Y', 'Y', 'L', 'T', 'G', 'Y', 'Y', 'Y', 'WL', 'Y', 'WL', 'Y', 'R']


def download(request):
    return render(request, 'download_xul.html')


def download_xul(request, cluster_name):
    response = HttpResponse(cluster_name)
    download_file = cluster_name.replace(' ', '_') + '.xul'
    with open('main.xul') as fh:
        lines = fh.readlines()
    with open('main.js') as fj:
        js_lines = fj.readlines()
        with open(download_file, 'w') as fc:
            fc.writelines(lines)
            centroid = []
            for cluster in request.session['result']['cluster']:
                # print(cluster)
                if cluster_name == cluster['name']:
                     centroid = cluster['centroid']
            fc.write(
                'var centroid=' + str(centroid) + ';'
            )
            fc.writelines(js_lines)

    with open(download_file, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.mozilla.xul+xml")
        response['Content-Disposition'] = 'inline; filename=' + cluster_name + '.xul'
    return response


def generate(request):
    limit_form = LimitForm()
    if request.method == 'POST':
        limit_form = LimitForm(request.POST)
        if limit_form.is_valid():
            limit = request.POST.get('limit')
            main_art(koefisien=limit)

    result = out_art()
    request.session['result'] = result
    return render(request, 'generate_cluster.html', {'limit_form': limit_form, 'result': result})


def index(request):
    identity_form = IdentityForm()
    survey_form = SurveyForm()
    context = {}
    if request.method == 'POST':
        survey_form = SurveyForm(request.POST)
        identity_form = IdentityForm(request.POST)
        if survey_form.is_valid():
            post = survey_form.cleaned_data
            uire = []

            uire_file = open('gabung_char2.csv')
            numline = len(uire_file.readlines())
            current_index = numline + 1
            # print(numline+1)
            uire.append(current_index)

            for question in questions:
                uire.append(post[question])
            print(uire)
            # tani_1 = tanimoto(uire, cluster_1).check()
            # tani_2 = tanimoto(uire, cluster_2).check()
            # print('tani 1', tani_1)
            # print('tani 2', tani_2)
            # cluster = compare_tani(tani_1, tani_2)
            # print(cluster)

            uire = str(uire).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            fd = open('gabung_char2.csv', 'a')
            fd.write(uire+'\n')
            fd.close()

            main_art()
            message = 'success'
            context['message'] = message
            # return render(request, 'result.html', {'cluster': cluster})
    context['survey_form'] = survey_form
    context['identity_form'] = identity_form

    return render(request, 'index.html', context)


def compare_tani(tani_1, tani_2):
    if tani_1 == tani_2:
        return 'cluster 1'
    max_tani = max(tani_1, tani_2)
    if max_tani < 0.4:
        return 'cluster baru'
    elif max_tani == tani_1:
        return 'cluster 1'
    elif max_tani == tani_2:
        return 'cluster 2'
    else:
        return 'cluster baru'


class tanimoto(object):
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def check(self) -> object:
        intersection = []
        for index, common_item in enumerate(self.list1):
            if self.list1[index] == self.list2[index]:
                intersection.append(common_item)

        return float(len(intersection)) / (len(self.list1) + len(self.list2) - len(intersection))


def main_art(koefisien=0.57):
    r = redis.StrictRedis(host='localhost', decode_responses=True, port=6379, db=0)
    r.flushdb()
    index = 0

    # openin CSV file
    file_open = open('gabung_char2.csv', 'r')
    csv_lists = csv.reader(file_open)

    # loop by number of line in csv file
    for idex, datax in enumerate(csv_lists):
        # print(datax)
        # generate database key from input data
        data_id = "data:" + str(idex)
        # Query all data keys in redis database
        item_keys = r.keys("data:*")
        print("jumlah data: " + str(len(item_keys)))
        print("--------------------")

        # Jika belum ada data sama sekali

        if len(item_keys) == 0:
            # generate "new group key"
            group_key = "group:" + str(idex)
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


def out_art():
    result = {}
    r = redis.StrictRedis(host='localhost', decode_responses=True, port=6379, db=0)
    file = open('gabung_out.csv', "w")
    # Mengekstrak semua group key
    groups_data = r.keys("group:*")
    print("jumlah cluster: "+ str(len(groups_data)))
    result['cluster_count'] = len(groups_data)
    result['total_members'] = 0
    result['cluster'] = []

    # Menulis jumlah kluster ke database
    file.writelines("jumlah cluster: " + str(len(groups_data)) + "\n\n")

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
        file.write("------------------\n")

        # Loop berdasarkan anggota group
        panda_data={}
        for idx, all_member in enumerate(all_members):
            # Mengambil isi data berdasarkan Key data yang ada pada group
            data = r.hgetall(all_member)
            list_data = ast.literal_eval(data["data"])
            list_data.pop(0)
            panda_data["data {}".format(idx+1)] = list_data
            print(data["data"])
            # menghilangkan karakter tidak terpakai di csv ([,], ')
            data_prepro = data["data"].replace("[", "").replace("]", "").replace("'", "")
            # menulis data_repro ke file
            file.write(data_prepro + "\n")

        df = pd.DataFrame(panda_data)
        print('\ncentroid: {}'.format(list(df.mode(axis=1)[0])))
        result['cluster'].append(
            {
                'name': "cluster " + str(index + 1),
                'member_count': len(all_members),
                'centroid': list(df.mode(axis=1)[0])
            }
        )
        result['total_members'] += len(all_members)
        print("------------------\n")
        file.write('centroid: {}\n'.format(list(df.mode(axis=1)[0])))
        file.write("------------------\n\n")

    file.close()
    return result
