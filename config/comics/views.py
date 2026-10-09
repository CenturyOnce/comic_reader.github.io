from django.shortcuts import render, redirect
from .forms import ThemeForm

COMICS_DATA = [
    {
        'id': 1,
        'title': 'Человек-паук',
        'description': 'История о супергерое, который борется с преступностью.',
        'image': 'images/Spider_man.jpg'
    },
    {
        'id': 2,
        'title': 'Бэтмен',
        'description': 'Мститель в маске защищает Готэм от злодеев.',
        'image': 'https://placehold.co/150x200?text=Batman'
    },
    {
        'id': 3,
        'title': 'Death in the family',
        'description': 'After the disappearance of his friend Medkit, Sword looks for answers. Join Sword as he inches closer to the secrets of the Inpherno.',
        'image': 'https://placehold.co/150x200?text=Spider-Verse'
    }
]

def index(request):
    current_theme = request.COOKIES.get('theme', 'light')
    context = {
        'comics': COMICS_DATA,
        'theme': current_theme
    }
    return render(request, 'comics/index.html', context)

def settings_view(request):
    current_theme = request.COOKIES.get('theme', 'light')
    
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            selected_theme = form.cleaned_data['theme']
            response = redirect('index')
            response.set_cookie('theme', selected_theme, max_age=31536000)
            return response
    else:
        form = ThemeForm(initial={'theme': current_theme})
        
    return render(request, 'comics/settings.html', {'form': form, 'theme': current_theme})