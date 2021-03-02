from django import forms

class nameForm(forms.Form):
    enter_name = forms.CharField(label= 'Enter your name: ', max_length=100)