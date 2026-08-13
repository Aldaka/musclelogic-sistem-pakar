from django.shortcuts import render
from .forms import ConsultationForm
from .inferensi_engine import run_forward_chaining


def home(request):
    context = {
        'title' : 'Halaman Beranda'
    }
    return render(request, 'home.html', context)


def hitung_bmi(tinggi_badan, berat_badan):
    tinggi_meter = tinggi_badan / 100
    bmi = berat_badan / (tinggi_meter ** 2)
    return round(bmi, 2)


def kategori_bmi(bmi):
    if bmi < 18.5:
        return "KURUS"
    elif bmi < 25:
        return "NORMAL"
    else:
        return "OVERWEIGHT"

def get_display_data(form, data):
    display_data = {}

    for field_name, value in data.items():
        field = form.fields.get(field_name)

        if field and hasattr(field, 'choices'):
            choices_dict = dict(field.choices)
            display_data[field_name] = choices_dict.get(value, value)
        else:
            display_data[field_name] = value

    return display_data


# def form_konsultasi(request):
#     context = {
#         'title': 'Halaman Konsultasi',
#     }
#     if request.method == 'POST':
#         form = ConsultationForm(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data
#             bmi = hitung_bmi(data['tinggi_badan'], data['berat_badan'])
#             bmi_cat = kategori_bmi(bmi)

#             hasil_inferensi = run_forward_chaining(
#                 data=data,
#                 bmi=bmi,
#                 bmi_cat=bmi_cat
#             )

#             return render(request, 'hasil.html', {
#                 'title': 'Hasil Konsultasi',
#                 'data': data,
#                 'bmi': bmi,
#                 'bmi_cat': bmi_cat,
#                 'hasil_inferensi': hasil_inferensi,
#             })
#     else:
#         form = ConsultationForm()
#     context['form'] = form
#     return render(request, 'form_konsultasi.html', context)

def form_konsultasi(request):
    context = {
        'title': 'Halaman Konsultasi',
    }

    if request.method == 'POST':
        form = ConsultationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            display_data = get_display_data(form, data)

            bmi = hitung_bmi(
                data['tinggi_badan'],
                data['berat_badan']
            )

            bmi_cat = kategori_bmi(bmi)

            hasil_inferensi = run_forward_chaining(
                data=data,
                bmi=bmi,
                bmi_cat=bmi_cat
            )

            return render(request, 'hasil.html', {
                'title': 'Hasil Konsultasi',
                'data': data,
                'display_data': display_data,
                'bmi': bmi,
                'bmi_cat': bmi_cat,
                'hasil_inferensi': hasil_inferensi,
            })

    else:
        form = ConsultationForm()

    context['form'] = form
    return render(request, 'form_konsultasi.html', context)