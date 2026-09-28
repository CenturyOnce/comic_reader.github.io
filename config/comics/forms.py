from django import forms

THEME_CHOICES = [
    ('light', 'Светлая'),
    ('dark', 'Темная'),
]

class ThemeForm(forms.Form):
    theme = forms.ChoiceField(choices=THEME_CHOICES, widget=forms.RadioSelect, label='Тема оформления')