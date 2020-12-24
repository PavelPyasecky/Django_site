from django.shortcuts import render

from django.views import View
from .forms import DataForm


class DataFormView(View):

    def get(self, request):
        form = DataForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = DataForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'form.html', context)
        else:
            return render(request, 'error.html', {'error': form.errors})
