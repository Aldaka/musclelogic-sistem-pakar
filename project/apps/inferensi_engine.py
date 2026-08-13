from .models import (
    RuleSafety,
    RuleKondisiTubuh,
    RuleLevel,
    RuleIntensitas,
    RulePenyesuaian,
    RuleRekomendasi,
    PaketLatihan,
    RulePenyesuaianAlat,
)


def get_rs15_safety(injury, injury_area):
    riwayat_cedera = injury_area if injury == 'YA' else 'TIDAK'
    rule = RuleSafety.objects.filter(riwayat_cedera=riwayat_cedera).first()

    if not rule:
        return None

    return {
        'rule_id': rule.rule_id,
        'riwayat_cedera': rule.riwayat_cedera,
        'batasan_gerakan': rule.batasan_gerakan,
        'keterangan': rule.keterangan,
    }


def get_rs5_kondisi_tubuh(bmi):
    rule = RuleKondisiTubuh.objects.filter(
        bmi_min__lte=bmi,
        bmi_max__gte=bmi
    ).first()

    if not rule:
        return None

    return {
        'rule_id': rule.rule_id,
        'bmi': bmi,
        'kondisi_tubuh': rule.kondisi_tubuh,
        'keterangan': rule.keterangan,
    }


def get_rs6_level(data):
    rule = RuleLevel.objects.filter(
        pengalaman=data['pengalaman_latihan'],
        teknik_dasar=data['teknik_dasar'],
        frekuensi_sebelumnya=data['frekuensi_sebelumnya']
    ).first()

    if not rule:
        return None

    return {
        'rule_id': rule.rule_id,
        'level': rule.level,
        'keterangan': rule.keterangan,
    }


def get_rs3_intensitas(kondisi_tubuh, level):
    rule = RuleIntensitas.objects.filter(
        kondisi_tubuh=kondisi_tubuh,
        level=level
    ).first()

    if not rule:
        return None

    return {
        'rule_id': rule.rule_id,
        'intensitas_awal': rule.intensitas_awal,
        'keterangan': rule.keterangan,
    }


def get_rs4_penyesuaian(data):
    rule = RulePenyesuaian.objects.filter(
        tujuan=data['goal'],
        tempat=data['place'],
        hari=data['days_per_week'],
        waktu=data['time_per_session']
    ).first()

    if not rule:
        return None

    return {
        'rule_id': rule.rule_id,
        'penyesuaian': rule.penyesuaian,
        'split': rule.split,
        'mode_latihan': rule.mode_latihan,
        'keterangan': rule.keterangan,
    }


def get_rs1_rekomendasi(batasan_gerakan, intensitas_awal, penyesuaian):
    rule = RuleRekomendasi.objects.filter(
        batasan_gerakan=batasan_gerakan,
        intensitas_awal=intensitas_awal,
        penyesuaian=penyesuaian
    ).first()

    if not rule:
        return None

    return {
        'rule_id': rule.rule_id,
        'paket': rule.paket,
        'intensitas_final': rule.intensitas_final,
        'alasan_rule': rule.alasan_rule,
    }


def get_paket_latihan(paket):
    rule = PaketLatihan.objects.filter(paket=paket).first()

    if not rule:
        return None

    return {
        'paket': rule.paket,
        'nama_program': rule.nama_program,
        'fokus_keamanan': rule.fokus_keamanan,
        'frekuensi_minggu': rule.frekuensi_minggu,
        'durasi_sesi': rule.durasi_sesi,
        'rekomendasi_gerakan': rule.rekomendasi_gerakan,
        'set_rep': rule.set_rep,
        'istirahat': rule.istirahat,
        'larangan': rule.larangan,
        'catatan': rule.catatan,
    }


def sesuaikan_paket_dengan_input(paket, data):
    if not paket:
        return paket

    focus = data.get('focus')
    place = data.get('place')
    equip_home = data.get('equip_home')

    tambahan_catatan = []

    # Penyesuaian berdasarkan prioritas latihan
    if focus == 'DADA':
        tambahan_catatan.append(
            'Prioritas latihan pengguna adalah dada. Jika tersedia dalam program, lakukan gerakan dada lebih awal saat tubuh masih segar.'
        )
    elif focus == 'KAKI':
        tambahan_catatan.append(
            'Prioritas latihan pengguna adalah kaki dan tubuh bagian bawah. Perhatikan teknik pada gerakan kaki dan jangan memaksakan beban.'
        )
    elif focus == 'LENGAN':
        tambahan_catatan.append(
            'Prioritas latihan pengguna adalah lengan. Tambahkan latihan lengan ringan setelah gerakan utama selesai.'
        )
    elif focus == 'FULL':
        tambahan_catatan.append(
            'Prioritas latihan diarahkan ke seluruh tubuh agar pemula memiliki dasar kekuatan yang merata.'
        )

    # Penyesuaian berdasarkan peralatan rumah
    if place == 'HOME':
        if equip_home == 'NO':
            paket['rekomendasi_gerakan'] = paket['rekomendasi_gerakan'].replace(
                'Band Pull Apart',
                'Wall Angel tanpa alat'
            ).replace(
                'Resistance Band Row',
                'Superman Pull tanpa alat'
            ).replace(
                'Dumbbell Row',
                'Superman Pull tanpa alat'
            ).replace(
                'Dumbbell Curl',
                'Towel Curl ringan'
            ).replace(
                'Dumbbell',
                'beban tubuh'
            ).replace(
                'Resistance Band',
                'gerakan tanpa alat'
            )

            tambahan_catatan.append(
                'Pengguna memilih latihan di rumah tanpa alat, sehingga gerakan disesuaikan menggunakan beban tubuh atau gerakan tanpa alat.'
            )

        elif equip_home == 'BAND':
            tambahan_catatan.append(
                'Pengguna memiliki resistance band, sehingga latihan dapat memanfaatkan band untuk gerakan tarik, bahu ringan, dan aktivasi otot.'
            )

        elif equip_home == 'DUMBELL':
            tambahan_catatan.append(
                'Pengguna memiliki dumbbell, sehingga latihan dapat menggunakan dumbbell ringan dengan tetap mengutamakan teknik.'
            )

    if tambahan_catatan:
        paket['catatan'] = paket['catatan'] + ' ' + ' '.join(tambahan_catatan)

    return paket

def get_rs7_penyesuaian_alat(data):
    if data.get('place') != 'HOME':
        return None

    rule = RulePenyesuaianAlat.objects.filter(
        tempat=data.get('place'),
        equip_home=data.get('equip_home'),
        hari=data.get('days_per_week')
    ).first()

    if not rule:
        return None

    return {
        'rule_id': rule.rule_id,
        'tempat': rule.tempat,
        'equip_home': rule.equip_home,
        'label_equip_home': rule.label_equip_home,
        'hari': rule.hari,
        'rekomendasi_gerakan': rule.rekomendasi_gerakan,
        'catatan_alat': rule.catatan_alat,
        'keterangan': rule.keterangan,
    }

def run_forward_chaining(data, bmi, bmi_cat):
    rs15 = get_rs15_safety(data['injury'], data['injury_area'])
    rs5 = get_rs5_kondisi_tubuh(bmi)
    rs6 = get_rs6_level(data)

    if not rs15 or not rs5 or not rs6:
        return {
            'status': 'Gagal',
            'pesan': 'Rule awal tidak ditemukan.',
            'rs15': rs15,
            'rs5': rs5,
            'rs6': rs6,
            'rs3': None,
            'rs4': None,
            'rs1': None,
            'rs7': None,
            'paket': None,
        }

    rs3 = get_rs3_intensitas(
        rs5['kondisi_tubuh'],
        rs6['level']
    )

    rs4 = get_rs4_penyesuaian(data)

    if not rs3 or not rs4:
        return {
            'status': 'Gagal',
            'pesan': 'Rule intensitas atau penyesuaian tidak ditemukan.',
            'rs15': rs15,
            'rs5': rs5,
            'rs6': rs6,
            'rs3': rs3,
            'rs4': rs4,
            'rs1': None,
            'rs7': None,
            'paket': None,
        }

    rs1 = get_rs1_rekomendasi(
        rs15['batasan_gerakan'],
        rs3['intensitas_awal'],
        rs4['penyesuaian']
    )

    if not rs1:
        return {
            'status': 'Gagal',
            'pesan': 'Rule rekomendasi akhir tidak ditemukan.',
            'rs15': rs15,
            'rs5': rs5,
            'rs6': rs6,
            'rs3': rs3,
            'rs4': rs4,
            'rs1': None,
            'rs7': None,
            'paket': None,
        }

    paket = get_paket_latihan(rs1['paket'])
    rs7 = get_rs7_penyesuaian_alat(data)
    if paket and rs7:
        paket['rekomendasi_gerakan'] = rs7['rekomendasi_gerakan']

        if rs7['catatan_alat']:
            paket['catatan'] = paket['catatan'] + ' ' + rs7['catatan_alat']

    paket = sesuaikan_paket_dengan_input(paket, data)

    return {
        'status': 'Berhasil',
        'pesan': 'Forward chaining berhasil dijalankan.',
        'bmi': bmi,
        'kondisi_tubuh': bmi_cat,
        'rs15': rs15,
        'rs5': rs5,
        'rs6': rs6,
        'rs3': rs3,
        'rs4': rs4,
        'rs1': rs1,
        'rs7': rs7,
        'paket': paket,
    }