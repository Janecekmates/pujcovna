from django.shortcuts import render
from .models import Auto, Pujcka
 
def index(request):
    # Na hlavní stránce zobrazíme auta
    auta = Auto.objects.all()  # V tomto případě získáme všechna auta
    return render(request, "pujcovna/index.html", {
        "auta": auta  # Přidáme auta do kontextu
    })
 
def seznam_pujcek(request):
    pujcky_data = []
    for pujcka in Pujcka.objects.select_related('auto').all():
        pocet_dni = (pujcka.Den_vraceni - pujcka.Den_pujceni).days
        celkova_cena = pujcka.penize_za_den * pocet_dni
        pujcky_data.append({
            'pujcka': pujcka,
            'pocet_dni': pocet_dni,
            'celkova_cena': celkova_cena
        })
    return render(request, 'pujcovna/pujcky.html', {
        'pujcky_data': pujcky_data
    })