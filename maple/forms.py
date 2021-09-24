from django import forms
from .models import Menu, Chicken, Beef, Side

class SideForm(forms.ModelForm):
    class Meta:
        model = Side
        fields = ['name', 'description', 'large', 'regular', 'image']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'one', 'three', 'six', 'image']

class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ['name', 'description', 'large', 'regular', 'image']

class BeefForm(forms.ModelForm):
    class Meta:
        model = Beef
        fields = ['name', 'description', 'large', 'regular', 'image']
