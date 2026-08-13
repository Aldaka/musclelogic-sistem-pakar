from django.contrib import admin
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


@admin.register(RuleSafety)
class RuleSafetyAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'riwayat_cedera', 'batasan_gerakan')
    search_fields = ('rule_id', 'riwayat_cedera')


@admin.register(RuleKondisiTubuh)
class RuleKondisiTubuhAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'bmi_min', 'bmi_max', 'kondisi_tubuh')
    search_fields = ('rule_id', 'kondisi_tubuh')


@admin.register(RuleLevel)
class RuleLevelAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'pengalaman', 'teknik_dasar', 'frekuensi_sebelumnya', 'level')
    list_filter = ('level',)
    search_fields = ('rule_id', 'level')


@admin.register(RuleIntensitas)
class RuleIntensitasAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'kondisi_tubuh', 'level', 'intensitas_awal')
    list_filter = ('intensitas_awal',)


@admin.register(RulePenyesuaian)
class RulePenyesuaianAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'tujuan', 'tempat', 'hari', 'waktu', 'penyesuaian')
    list_filter = ('tujuan', 'tempat')


@admin.register(RuleRekomendasi)
class RuleRekomendasiAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'batasan_gerakan', 'intensitas_awal', 'penyesuaian', 'paket')
    list_filter = ('paket',)


@admin.register(PaketLatihan)
class PaketLatihanAdmin(admin.ModelAdmin):
    list_display = ('paket', 'nama_program', 'frekuensi_minggu', 'durasi_sesi')
    search_fields = ('paket', 'nama_program')

@admin.register(RulePenyesuaianAlat)
class RulePenyesuaianAlatAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'tempat', 'equip_home', 'label_equip_home', 'hari')
    list_filter = ('tempat', 'equip_home', 'hari')
    search_fields = ('rule_id', 'equip_home', 'label_equip_home', 'keterangan')
