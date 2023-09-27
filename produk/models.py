from django.db import models

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

class Status(models.Model):
    nama_status = models.CharField(max_length=100)

class Produk(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
