from django import forms


PENGALAMAN_CHOICES = [
    ('TIDAK_PERNAH', 'Belum pernah melakukan latihan beban'),
    ('PERNAH', 'Pernah melakukan latihan beban'),
]

TEKNIK_CHOICES = [
    ('BELUM', 'Belum yakin atau belum memahami teknik dasar'),
    ('CUKUP', 'Cukup memahami teknik dasar'),
]

FREKUENSI_SEBELUMNYA_CHOICES = [
    ('0', 'Belum pernah atau belum rutin berlatih'),
    ('1-2', '1–2 kali per minggu'),
    ('3+', '3 kali atau lebih per minggu'),
]

GOAL_CHOICES = [
    ('FATLOSS', 'Mengurangi lemak tubuh'),
    ('GAIN', 'Menambah massa otot'),
    ('RECOMP', 'Mengurangi lemak dan menambah otot secara bertahap'),
]

FOCUS_CHOICES = [
    ('FULL', 'Saya belum tahu, rekomendasikan latihan seluruh tubuh'),
    ('DADA', 'Saya ingin tambahan latihan dada'),
    ('KAKI', 'Saya ingin tambahan latihan kaki dan tubuh bawah'),
    ('LENGAN', 'Saya ingin tambahan latihan lengan'),
]

PLACE_CHOICES = [
    ('GYM', 'Gym atau pusat kebugaran'),
    ('HOME', 'Rumah'),
]

EQUIP_HOME_CHOICES = [
    ('NO', 'Tidak memiliki peralatan latihan'),
    ('BAND', 'Resistance Band'),
    ('DUMBELL', 'Dumbbell'),
]

DAYS_CHOICES = [
    ('2', '2 hari per minggu'),
    ('3', '3 hari per minggu'),
    ('4-5', '4–5 hari per minggu'),
]

TIME_CHOICES = [
    ('<=30', '30 menit atau kurang'),
    ('31-45', '31–45 menit'),
    ('46-60', '46–60 menit'),
]

INJURY_CHOICES = [

    ('TIDAK', 'Tidak memiliki riwayat cedera'),
    ('YA', 'Memiliki riwayat cedera'),
]

INJURY_AREA_CHOICES = [
    ('', '-- Pilih bagian tubuh yang mengalami cedera --'),
    ('BAHU', 'Bahu'),
    ('LUTUT', 'Lutut'),
    ('PUNGGUNG', 'Punggung'),
]


class ConsultationForm(forms.Form):
    tinggi_badan = forms.FloatField(
        label='Berapa tinggi badan Anda? (cm)',
        min_value=100,
        max_value=250
    )

    berat_badan = forms.FloatField(
        label='Berapa berat badan Anda? (kg)',
        min_value=30,
        max_value=300
    )

    pengalaman_latihan = forms.ChoiceField(
        label='Apakah Anda pernah melakukan latihan beban sebelumnya?',
        choices=PENGALAMAN_CHOICES
    )

    teknik_dasar = forms.ChoiceField(
        label='Seberapa yakin Anda memahami teknik dasar latihan?',
        choices=TEKNIK_CHOICES
    )

    frekuensi_sebelumnya = forms.ChoiceField(
        label='Dalam beberapa minggu terakhir, seberapa sering Anda berlatih?',
        choices=FREKUENSI_SEBELUMNYA_CHOICES
    )

    goal = forms.ChoiceField(
        label='Apa hasil utama yang ingin Anda capai?',
        choices=GOAL_CHOICES
    )

    focus = forms.ChoiceField(
        label='Apakah ada bagian tubuh yang ingin diberi tambahan fokus?',
        choices=FOCUS_CHOICES,
        initial='FULL',
        help_text='Jika belum tahu, pilih rekomendasi latihan seluruh tubuh. Pilihan ini digunakan sebagai arahan tambahan.'
    )

    place = forms.ChoiceField(
        label='Di mana Anda berencana melakukan latihan?',
        choices=PLACE_CHOICES
    )

    equip_home = forms.ChoiceField(
        label='Peralatan apa yang tersedia di rumah?',
        choices=EQUIP_HOME_CHOICES,
        required=False
    )

    days_per_week = forms.ChoiceField(
        label='Berapa hari dalam seminggu Anda dapat meluangkan waktu untuk latihan?',
        choices=DAYS_CHOICES
    )

    time_per_session = forms.ChoiceField(
        label='Berapa lama waktu yang tersedia dalam satu sesi latihan?',
        choices=TIME_CHOICES
    )

    injury = forms.ChoiceField(
        label='Apakah Anda memiliki riwayat cedera?',
        choices=INJURY_CHOICES
    )

    injury_area = forms.ChoiceField(
        label='Bagian tubuh mana yang mengalami cedera?',
        choices=INJURY_AREA_CHOICES,
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()

        place = cleaned_data.get('place')
        equip_home = cleaned_data.get('equip_home')
        injury = cleaned_data.get('injury')
        injury_area = cleaned_data.get('injury_area')

        if place == 'HOME' and not equip_home:
            self.add_error('equip_home',
                           'Pilih peralatan yang tersedia agar rekomendasi latihan dapat disesuaikan.')

        if place == 'GYM':
            cleaned_data['equip_home'] = ''

        if injury == 'YA' and not injury_area:
            self.add_error('injury_area', 
                           'Pilih bagian tubuh yang mengalami cedera.')

        if injury == 'TIDAK':
            cleaned_data['injury_area'] = ''

        return cleaned_data