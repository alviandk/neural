from django import forms

from .models import Survey


class SurveyModelForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SurveyModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class SurveyForm(forms.Form):
    question_1 = forms.ChoiceField(
        label='1. Model pencarian/searching yang diinginkan berbentuk kategori',
        widget=forms.RadioSelect,
        choices=(('A', 'Taxonomy',), ('B', 'Keyword',), ('C', 'Image',))
    )
    question_2 = forms.ChoiceField(
        label='2. Adanya fasilitas Spellcheck',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_3 = forms.ChoiceField(
        label='3. Adanya rekomendasi buku yang relevan',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_4 = forms.ChoiceField(
        label='4. Adanya hasil pencarian yang diranking berdasarkan relevansinya dengan kebutuhan',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_5 = forms.ChoiceField(
        label='5. Navigasi penelusuran pencarian/searching yang dinginkan berbentuk',
        widget=forms.RadioSelect,
        choices=(('L', 'Link',), ('I', 'Icon',))
    )
    question_6 = forms.ChoiceField(
        label='6. Icon navigasi yang diinginkan berbentuk ',
        widget=forms.RadioSelect,
        choices=(
            ('C', 'Gambar/image (misal intruksi cari bergambar “kaca pembesar”) ',),
            ('T', 'Teks/texts  (misal  intruksi cari bertuliskan “search” )',)
        )
    )
    question_7 = forms.ChoiceField(
        label='7. Ukuran icon navigasi yang diinginkan ',
        widget=forms.RadioSelect,
        choices=(('K', 'Kecil',), ('G', 'Besar',))
    )
    question_8 = forms.ChoiceField(
        label='8. Adanya batasan bentuk/tipe  huruf  dalam disain antarmuka OPAC.',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_9 = forms.ChoiceField(
        label='9. Adanya batasan ukuran/size huruf dalam disain antarmuka OPAC',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_10 = forms.ChoiceField(
        label='10. Adanya batasan jumlah warna dalam disain antarmuka OPAC',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_11 = forms.ChoiceField(
        label='11. Warna disain antarmuka  yang diinginkan :',
        widget=forms.RadioSelect,
        choices=(('WL', 'Warna Lembut',), ('WM', 'Warna Mencolok',))
    )
    question_12 = forms.ChoiceField(
        label='12. Adanya batasan jumlah warna  background dalam disain antarmuka OPAC  ',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_13 = forms.ChoiceField(
        label='13. Warna background antarmuka yang diinginkan ',
        widget=forms.RadioSelect,
        choices=(('WL', 'Warna Lembut',), ('WM', 'Warna Mencolok',))
    )
    question_14 = forms.ChoiceField(
        label='14. Desain antarmuka pencarian/searching dengan bentuk sederhana',
        widget=forms.RadioSelect,
        choices=(('Y', 'Ya',), ('T', 'Tidak',))
    )
    question_15 = forms.ChoiceField(
        label='15. Hasil pencarian/searching  yang diinginkan Menampilkan:',
        widget=forms.RadioSelect,
        choices=(
            ('P', 'Menampilkan semua informasi obyek',),
            ('Q', 'Menampilkan informasi hanya obyek yang diminta',),
            ('R', 'Menampilkan informasi dengan menambahkan referensi sumber',),
            ('S', 'Menampilkan Informasi diurutkan berdasarkan popularitas',)
        )
    )

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class IdentityForm(forms.Form):
    nama = forms.CharField()
    umur = forms.IntegerField()
    pekerjaan = forms.CharField()
    jenis_kelamin = forms.ChoiceField(choices=(('L', 'Laki-Laki'), ('P', 'Perempuan')))
    pendidikan = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(IdentityForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LimitForm(forms.Form):
    limit = forms.FloatField(help_text='between 0-1')

    def __init__(self, *args, **kwargs):
        super(LimitForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
