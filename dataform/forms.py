from django import forms


class DataForm(forms.Form):
    name = forms.CharField(label="Имя", min_length=3, max_length=32, help_text="Иванов Иван Иванович")
    email = forms.EmailField(label="Email", min_length=3, max_length=64, help_text="ivan1982ivanovich@mail.ru")
    phone = forms.RegexField(label="Телефон", regex="^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$", help_text="+375445556677")
    mes = forms.CharField(label="Сообщение", max_length=128, help_text="Здравствуйте, Илья! Хочу с Вами связаться по поводу недвижимости. Высылаю неоюходимые материалы.")
    file = forms.FileField(label="Материалы", required=False)

    def clean_phone(self):
        if "+375" or "80" not in self.cleaned_data['phone']:
            raise forms.ValidationError('Используйте полный формат записи телефонного номера.')

