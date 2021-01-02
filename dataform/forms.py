from django import forms


class DataForm(forms.Form):
    name = forms.CharField(label="Имя",
                           min_length=3,
                           max_length=32,
                           widget=forms.TextInput(attrs={"class":"form-control form-text required", "id":"edit-submitted-name",  "placeholder":"Иванов Иван Иванович"})
                           )
    email = forms.EmailField(label="Email",
                             min_length=3,
                             max_length=64,
                             widget=forms.TextInput(attrs={"class":"form-control form-text required", "id":"edit-submitted-email", "placeholder":"ivan1982ivanovich@mail.ru"})
                             )
    phone = forms.RegexField(label="Телефон",
                             regex="^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$",
                             widget=forms.TextInput(attrs={"class": "form-control form-text required", "id": "edit-submitted-phone", "placeholder":"+375xxXXXXXXX"})
                             )
    mes = forms.CharField(label="Сообщение",
                          widget=forms.Textarea(attrs={"class": "form-control form-textarea required", "id": "edit-submitted-message", "cols":"60", "rows":"5"})
                          )
    image = forms.ImageField(label="Изображения",
                           required=False,
                           widget=forms.FileInput(attrs={'multiple': 'multiple', "id": "edit-submitted-file"})
                           )

    # def clean_phone(self):
    #     if "+375" not in self.cleaned_data['phone'] or "80" not in self.cleaned_data['phone']:
    #         raise forms.ValidationError('Используйте полный формат записи телефонного номера.')
