import os
import django
import pandas as pd
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from apps.models import (
    RuleSafety,
    RuleKondisiTubuh,
    RuleLevel,
    RuleIntensitas,
    RulePenyesuaian,
    RuleRekomendasi,
    PaketLatihan,
    RulePenyesuaianAlat,
)


BASE_DIR = Path(__file__).resolve().parent
EXCEL_PATH = BASE_DIR / 'data' / 'ruleset_final_sispak_latihan_detail_database_ready.xlsx'


def clean(value):
    if pd.isna(value):
        return ''
    return str(value).strip()


def main():
    print("Menghapus data lama...")

    RuleSafety.objects.all().delete()
    RuleKondisiTubuh.objects.all().delete()
    RuleLevel.objects.all().delete()
    RuleIntensitas.objects.all().delete()
    RulePenyesuaian.objects.all().delete()
    RuleRekomendasi.objects.all().delete()
    PaketLatihan.objects.all().delete()
    RulePenyesuaianAlat.objects.all().delete()

    print("Import RS15 Safety...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='RS15_Safety')
    for _, row in df.iterrows():
        RuleSafety.objects.create(
            rule_id=clean(row['RULE_ID']),
            riwayat_cedera=clean(row['IF_RIWAYAT_CEDERA']),
            batasan_gerakan=clean(row['THEN_BATASAN_GERAKAN']),
            keterangan=clean(row.get('KETERANGAN', '')),
        )

    print("Import RS5 Kondisi Tubuh...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='RS5_KondisiTubuh')
    for _, row in df.iterrows():
        RuleKondisiTubuh.objects.create(
            rule_id=clean(row['RULE_ID']),
            bmi_min=float(row['BMI_MIN']),
            bmi_max=float(row['BMI_MAX']),
            kondisi_tubuh=clean(row['THEN_KONDISI_TUBUH']),
            keterangan=clean(row.get('KETERANGAN', '')),
        )

    print("Import RS6 Level...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='RS6_Level')
    for _, row in df.iterrows():
        RuleLevel.objects.create(
            rule_id=clean(row['RULE_ID']),
            pengalaman=clean(row['IF_PENGALAMAN']),
            teknik_dasar=clean(row['IF_TEKNIK_DASAR']),
            frekuensi_sebelumnya=clean(row['IF_FREKUENSI_SEBELUMNYA']),
            level=clean(row['THEN_LEVEL']),
            keterangan=clean(row.get('KETERANGAN', '')),
        )

    print("Import RS3 Intensitas Awal...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='RS3_IntensitasAwal')
    for _, row in df.iterrows():
        RuleIntensitas.objects.create(
            rule_id=clean(row['RULE_ID']),
            kondisi_tubuh=clean(row['IF_KONDISI_TUBUH']),
            level=clean(row['IF_LEVEL']),
            intensitas_awal=clean(row['THEN_INTENSITAS_AWAL']),
            keterangan=clean(row.get('KETERANGAN', '')),
        )

    print("Import RS4 Penyesuaian...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='RS4_Penyesuaian')
    for _, row in df.iterrows():
        RulePenyesuaian.objects.create(
            rule_id=clean(row['RULE_ID']),
            tujuan=clean(row['IF_TUJUAN']),
            tempat=clean(row['IF_TEMPAT']),
            hari=clean(row['IF_HARI']),
            waktu=clean(row['IF_WAKTU']),
            penyesuaian=clean(row['THEN_PENYESUAIAN']),
            split=clean(row.get('THEN_SPLIT', '')),
            mode_latihan=clean(row.get('MODE_LATIHAN', '')),
            keterangan=clean(row.get('KETERANGAN', '')),
        )

    print("Import RS1 Rekomendasi...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='RS1_Rekomendasi')
    for _, row in df.iterrows():
        RuleRekomendasi.objects.create(
            rule_id=clean(row['RULE_ID']),
            batasan_gerakan=clean(row['IF_BATASAN_GERAKAN']),
            intensitas_awal=clean(row['IF_INTENSITAS_AWAL']),
            penyesuaian=clean(row['IF_PENYESUAIAN']),
            paket=clean(row['THEN_PAKET']),
            intensitas_final=clean(row.get('THEN_INTENSITAS_FINAL', '')),
            alasan_rule=clean(row.get('ALASAN_RULE', '')),
        )

    print("Import Paket Latihan...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='Paket_Latihan')
    for _, row in df.iterrows():
        PaketLatihan.objects.create(
            paket=clean(row['PAKET']),
            nama_program=clean(row['NAMA_PROGRAM']),
            fokus_keamanan=clean(row.get('FOKUS_KEAMANAN', '')),
            frekuensi_minggu=clean(row.get('FREKUENSI_MINGGU', '')),
            durasi_sesi=clean(row.get('DURASI_SESI', '')),
            rekomendasi_gerakan=clean(row.get('REKOMENDASI_GERAKAN', '')),
            set_rep=clean(row.get('SET_REP', '')),
            istirahat=clean(row.get('ISTIRAHAT', '')),
            larangan=clean(row.get('LARANGAN', '')),
            catatan=clean(row.get('CATATAN', '')),
        )
        
    print("Import RS7 Penyesuaian Alat...")
    df = pd.read_excel(EXCEL_PATH, sheet_name='RS7_PenyesuaianAlat')

    for _, row in df.iterrows():
        RulePenyesuaianAlat.objects.create(
            rule_id=clean(row['RULE_ID']),
            tempat=clean(row['IF_TEMPAT']),
            equip_home=clean(row['IF_EQUIP_HOME']),
            label_equip_home=clean(row.get('LABEL_EQUIP_HOME', '')),
            hari=clean(row['IF_HARI']),
            rekomendasi_gerakan=clean(row['THEN_REKOMENDASI_GERAKAN']),
            catatan_alat=clean(row.get('THEN_CATATAN_ALAT', '')),
            keterangan=clean(row.get('KETERANGAN', '')),
        )

    print("SELESAI! Data ruleset berhasil masuk database.")


if __name__ == '__main__':
    main()