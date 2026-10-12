from django.shortcuts import render, redirect
from .forms import ThemeForm

COMICS_DATA = [
    {
        'id': 1,
        'title': 'Человек-паук',
        'description': 'История о супергерое, который борется с преступностью.',
        'image': 'comics/images/Spider_man.jpg'
    },
    {
        'id': 2,
        'title': 'Бэтмен',
        'description': 'Мститель в маске защищает Готэм от злодеев.',
        'image': 'comics/images/Batman.jpg'
    },
    {
        'id': 3,
        'title': 'Death in the family',
        'description': 'After the disappearance of his friend Medkit, Sword looks for answers. Join Sword as he inches closer to the secrets of the Inpherno.',
        'image': 'comics/images/ditf.png'
    }
]

def get_user_settings(request):
    return {
        'theme': request.COOKIES.get('theme', 'light'),
        'font_size': request.COOKIES.get('font_size', 'normal'),
        'accent': request.COOKIES.get('accent', 'blue'),
        'username' : request.COOKIES.get('username', 'User')
    }

def index(request):
    settings = get_user_settings(request)
    current_theme = request.COOKIES.get('theme', 'light')
    context = {
        'comics': COMICS_DATA,
        **settings
    }
    response = render(request, 'comics/index.html', context)
    return response

def settings_view(request):
    settings = get_user_settings(request)
    
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            response = redirect('index')
            response.set_cookie('theme', form.cleaned_data['theme'], max_age=31536000)
            response.set_cookie('font_size', form.cleaned_data['font_size'], max_age=31536000)
            response.set_cookie('accent', form.cleaned_data['accent'], max_age=31536000)
            response.set_cookie('username', form.cleaned_data['username'], max_age=31536000)
            return response
    else:
        form = ThemeForm(initial=settings)
        
    return render(request, 'comics/settings.html', {'form': form, **settings})