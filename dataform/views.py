from django.shortcuts import render

from django.views import View
from .forms import DataForm

usermessage = 'Здравствуйте, Илья! Хочу с Вами связаться по поводу недвижимости. Жду Вашего звонка!'

class DataFormView(View):

    def get(self, request):
        form = DataForm(initial={'mes': usermessage})
        return render(request, 'dataform/form.html', {'form': form})

    def post(self, request):
        form = DataForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'dataform/form.html', context)
        else:
            return render(request, 'dataform/error.html', {'error': form.errors})
