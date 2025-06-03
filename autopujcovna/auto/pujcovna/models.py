from django.db import models
 
class Auto(models.Model):
    Znacka = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Rok_vyroby = models.IntegerField()
    Motor = models.CharField(max_length=100)
    Palivo = models.CharField(max_length=50)
    Prevodovka = models.CharField(max_length=50)
    Vykon = models.IntegerField()
    Kategorie = models.CharField(max_length=50)
    SPZ = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='obrazky/', null=True, blank=True)  # Přidání pole pro obrázek
 
    def __str__(self):
        return f"{self.Znacka} {self.Model}"
 
class Pujcka(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    Den_pujceni = models.DateField()
    Den_vraceni = models.DateField()
    penize_za_den = models.DecimalField(max_digits=10, decimal_places=2)
 
    def __str__(self):
        return f"Půjčka pro {self.auto.Znacka} {self.auto.Model}"