from django.db import models


class Survey(models.Model):
    question_1 = models.CharField(
        verbose_name='1. Model pencarian/searching yang diinginkan berbentuk kategori',
        max_length=225,
        choices=(('A', 'Taxonomy',), ('B', 'Keyword',), ('C', 'Image',))
    )
    question_2 = models.CharField(
        verbose_name='2. Adanya fasilitas Spellcheck',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_3 = models.CharField(
        verbose_name='3. Adanya rekomendasi buku yang relevan',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_4 = models.CharField(
        verbose_name='4. Adanya hasil pencarian yang diranking berdasarkan relevansinya dengan kebutuhan',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_5 = models.CharField(
        verbose_name='5. Navigasi penelusuran pencarian/searching yang dinginkan berbentuk',
        max_length=225,
        choices=(('L', 'Link',), ('I', 'Icon',))
    )
    question_6 = models.CharField(
        verbose_name='6. Icon navigasi yang diinginkan berbentuk ',
        max_length=225,
        choices=(
            ('L', 'Gambar/image (misal intruksi cari bergambar “kaca pembesar”) ',),
            ('I', 'Teks/texts  (misal  intruksi cari bertuliskan “search” )',)
        )
    )
    question_7 = models.CharField(
        verbose_name='7. Ukuran icon navigasi yang diinginkan ',
        max_length=225,
        choices=(('K', 'Kecil',), ('G', 'Besar',))
    )
    question_8 = models.CharField(
        verbose_name='8. Adanya batasan bentuk/tipe  huruf  dalam disain antarmuka OPAC.',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_9 = models.CharField(
        verbose_name='9. Adanya batasan ukuran/size huruf dalam disain antarmuka OPAC',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_10 = models.CharField(
        verbose_name='10. Adanya batasan jumlah warna dalam disain antarmuka OPAC',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_11 = models.CharField(
        verbose_name='11. Warna disain antarmuka  yang diinginkan :',
        max_length=225,
        choices=(('WL', 'Warna Lembut',), ('WM', 'Warna Mencolok',))
    )
    question_12 = models.CharField(
        verbose_name='12. Adanya batasan jumlah warna  background dalam disain antarmuka OPAC  ',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_13 = models.CharField(
        verbose_name='13. Warna background antarmuka yang diinginkan ',
        max_length=225,
        choices=(('WL', 'Warna Lembut',), ('WM', 'Warna Mencolok',))
    )
    question_14 = models.CharField(
        verbose_name='14. Desain antarmuka pencarian/searching dengan bentuk sederhana',
        max_length=225,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_15 = models.CharField(
        verbose_name='15. Hasil pencarian/searching  yang diinginkan Menampilkan:',
        max_length=225,
        choices=(
            ('P', 'Menampilkan semua informasi obyek',),
            ('Q', 'Menampilkan informasi hanya obyek yang diminta',),
            ('R', 'Menampilkan informasi dengan menambahkan referensi sumber',),
            ('S', 'Menampilkan Informasi diurutkan berdasarkan popularitas',)
        )
    )