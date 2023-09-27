from django.shortcuts import render
from django.http import JsonResponse
import requests
from produk.models import Produk

def home(request):
    # Mengambil semua produk
    produk_list = Produk.objects.all()
    return render(request, 'home.html', {'produk_list': produk_list})

def ambil_data_api(request):
    url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
    username = 'tesprogrammer270923C16'
    password = 'bisacoding-27-09-23'  # Sesuaikan dengan format yang diberikan

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'message': 'Gagal mengambil data dari API'}, status=500)

def tampilkan_data(request):
    url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
    username = 'tesprogrammer270923C16'
    password = 'bisacoding-21-09-23'  # Sesuaikan dengan format yang diberikan

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        return render(request, 'home.html', {'data': data})
    else:
        return JsonResponse({'message': 'Gagal mengambil data dari API'}, status=500)
