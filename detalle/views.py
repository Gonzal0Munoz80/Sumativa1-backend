from django.shortcuts import render


def detalle(request):
    juego = {
        'id': 1,
        'titulo': 'Caminos del Norte',
        'plataforma': 'PC',
        'precio': 24990,
        'horas': 30,
        'multijugador': False,
        'oferta': False,
        'descripcion': 'Aventura de mundo abierto por el desierto de Atacama, con misiones en pueblos mineros y caletas.',
    }
    return render(request, 'detalle.html', {'juego': juego})

