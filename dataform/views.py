from django.shortcuts import render

from django.views import View
from .forms import DataForm


class DataFormView(View):

    def get(self, request):
        form = DataForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        mes = request.POST.get('mes')
        file = request.FILES.get('file')
        content = file.read()
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'mes': mes,
            'file': content,
        }
        return render(request, 'form.html', context)
