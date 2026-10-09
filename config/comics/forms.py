from django import forms

class ThemeForm(forms.Form):
    theme = forms.ChoiceField(
        choices=[('light', 'Светлая'), ('dark', 'Темная')], 
        widget=forms.RadioSelect, label='Тема оформления'
    )
    font_size = forms.ChoiceField(
        choices=[('normal', 'Обычный'), ('large', 'Крупный')], 
        widget=forms.RadioSelect, label='Размер шрифта'
    )
    accent = forms.ChoiceField(
        choices=[('blue', 'Синий'), ('orange', 'Оранжевый'), ('green', 'Зеленый')], 
        widget=forms.RadioSelect, label='Цвет акцента'
    )