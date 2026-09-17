from django.shortcuts import render
from inicio.views import JUEGOS


def detalle(request, id):
    juego = next((item for item in JUEGOS if item['id'] == id), None)

    if juego is None:
        return render(request, 'error_juego.html', {'mensaje': 'Juego no existe'})

    return render(request, 'detalle.html', {'juego': juego})


def error_juego(request):
    return render(request, 'error_juego.html', {'mensaje': 'Juego no existe'})

