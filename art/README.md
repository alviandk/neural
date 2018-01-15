# Similarity Check
Program untuk mengchek similarity disertasinya bu marliza

## Requirement
Beberapa software yang diperlukan:
* python3
* python3-csv
* python-redis
* redis-server

## Penggunaan
* pastikan redis-server sudah berjalan:
```
<bla bla bla>$ redis-cli -n 0
127.0.0.1:6379>
```
* copy semua data (tanpa header) di XLS yang ada
* paste special hanya number-nya ke XLS baru
* save XLS tersebut ke format .csv di folder yang sama dengan program
* masuk ke folder program
* untuk memproses, jalankan :
```
python3 main.py [nama_file.csv] [koefisien minimal tanimoto]
```
* untuk menghasilkan data, jalankan :
```
python3 get_data.py [nama_file_output.csv]
```
* untuk melihat grafiknya, jalankan :
```
python3 graph.py [cluster|tmax]
```

