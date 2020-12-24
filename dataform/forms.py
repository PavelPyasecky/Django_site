from django.forms import forms


class DataForm(forms.Form):
    name = forms.CharField(label="Имя", min_length=3, max_length=32)