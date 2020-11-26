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
    articles = Article.objects.all()
    rubrics = Rubric.objects.all()
    context = {'articles':articles, 'rubrics':rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    articles = Article.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'articles': articles, 'rubrics': rubrics,
               'current_rubric': current_rubric
               }
    return render(request, 'bboard/by_rubric.html', context)

