from django.db import models


class RuleSafety(models.Model):
    rule_id = models.CharField(max_length=20, unique=True)
    riwayat_cedera = models.CharField(max_length=50)
    batasan_gerakan = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rule_id} - {self.riwayat_cedera}"


class RuleKondisiTubuh(models.Model):
    rule_id = models.CharField(max_length=20, unique=True)
    bmi_min = models.FloatField()
    bmi_max = models.FloatField()
    kondisi_tubuh = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rule_id} - {self.kondisi_tubuh}"


class RuleLevel(models.Model):
    rule_id = models.CharField(max_length=20, unique=True)
    pengalaman = models.CharField(max_length=50)
    teknik_dasar = models.CharField(max_length=50)
    frekuensi_sebelumnya = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rule_id} - {self.level}"


class RuleIntensitas(models.Model):
    rule_id = models.CharField(max_length=20, unique=True)
    kondisi_tubuh = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    intensitas_awal = models.CharField(max_length=50)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rule_id} - {self.intensitas_awal}"


class RulePenyesuaian(models.Model):
    rule_id = models.CharField(max_length=20, unique=True)
    tujuan = models.CharField(max_length=50)
    tempat = models.CharField(max_length=50)
    hari = models.CharField(max_length=50)
    waktu = models.CharField(max_length=50)
    penyesuaian = models.CharField(max_length=100)
    split = models.CharField(max_length=100, blank=True, null=True)
    mode_latihan = models.CharField(max_length=100, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rule_id} - {self.penyesuaian}"


class RuleRekomendasi(models.Model):
    rule_id = models.CharField(max_length=20, unique=True)
    batasan_gerakan = models.CharField(max_length=100)
    intensitas_awal = models.CharField(max_length=50)
    penyesuaian = models.CharField(max_length=100)
    paket = models.CharField(max_length=20)
    intensitas_final = models.CharField(max_length=50)
    alasan_rule = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rule_id} - {self.paket}"


class PaketLatihan(models.Model):
    paket = models.CharField(max_length=20, unique=True)
    nama_program = models.CharField(max_length=150)
    fokus_keamanan = models.TextField(blank=True, null=True)
    frekuensi_minggu = models.CharField(max_length=100, blank=True, null=True)
    durasi_sesi = models.CharField(max_length=100, blank=True, null=True)
    rekomendasi_gerakan = models.TextField(blank=True, null=True)
    set_rep = models.TextField(blank=True, null=True)
    istirahat = models.CharField(max_length=100, blank=True, null=True)
    larangan = models.TextField(blank=True, null=True)
    catatan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paket} - {self.nama_program}"

class RulePenyesuaianAlat(models.Model):
    rule_id = models.CharField(max_length=20, unique=True)
    tempat = models.CharField(max_length=50)
    equip_home = models.CharField(max_length=50)
    label_equip_home = models.CharField(max_length=100, blank=True, null=True)
    hari = models.CharField(max_length=50)
    rekomendasi_gerakan = models.TextField()
    catatan_alat = models.TextField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rule_id} - {self.equip_home} - {self.hari}"