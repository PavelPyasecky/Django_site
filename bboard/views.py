from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Article
from .models import Rubric

from .forms import ArticleForm


class ArticleCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def index(request):
    return render(request, 'bboard/index.html')

def buyer_page(request):
    return render(request, 'bboard/buyer.html')

def seller_page(request):
    return render(request, 'bboard/seller.html')

def contact_page(request):
    return render(request, 'bboard/contact.html')

def ilyapiasetski_page(request):
    return render(request, 'bboard/ilyapiasetski.html')

def legal_notice_page(request):
    return render(request, 'bboard/legal-notice.html')
