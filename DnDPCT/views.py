from django.shortcuts import render
from .forms import ModifierForm

def stats(request):
    form = ModifierForm(request.POST or None)

    if form.is_valid():
        modifier_value = form.cleaned_data['modifier']
        request.session['modifier_value'] = modifier_value

    attributes = ['Fuerza', 'Destreza', 'Constitución', 'Sabiduría', 'Inteligencia', 'Carisma']
    desc = ['Mide la potencia física en situaciones en que se puede ejercer puro poderío físico',
            'Mide la agilidad, los reflejos y el equilibrio al moverte con rapidez o en silencio',
            'Mide la salud, el aguante y el vigor. Sirve para calcular tu Clase de Armadura',
            'Mide la comprensión sobre tu entorno y es útil para cuidar a una persona herida',
            'Mide la agudeza mental, la exactitud de los recuerdos y la capacidad de razonar',
            'Mide tu capacidad para interactuar de forma efectiva con otros']

    context = {
        'form': form,
        'attr_desc' : zip(attributes, desc),
        'cards': 6,
    }

    return render(request, 'stats.html', context)


def transfondo(request):
    # Añadir contexto if needed
    return render(request, 'background.html')

def hechizos(request):
    # Añadir contexto if needed
    return render(request, 'spells.html')

def notas(request):
    # Añadir contexto if needed
    return render(request, 'notas.html')

def index(request):
    # Añadir contexto if needed
    return render(request, 'index.html')