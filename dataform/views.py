from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.views import View
from .forms import DataForm
from django.conf import settings


usermessage = 'Здравствуйте, Илья! Хочу с Вами связаться по поводу недвижимости. Жду Вашего звонка!'

class DataFormView(View):

    def get(self, request):
        form = DataForm(initial={'mes': usermessage})
        return render(request, 'dataform/form.html', {'form': form})

    def post(self, request):
        form = DataForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            data = {
                'name': context['name'],
                'email': context['email'],
                'phone': context['phone'],
                'mes': context['mes'],
                'file': context['file']
            }

            print(context['name'])
            print(context['email'])
            print(context['phone'])
            print(context['mes'])
            print(open(context['file'], "r"))
            print("-"*20)

            html_body = render_to_string('dataform/index.html', data)
            msg = EmailMultiAlternatives(subject="Feedback - mrealt.by", from_email=settings.EMAIL_HOST_USER, to=["pyasecky2012pavel@mail.ru"])
            msg.attach_alternative(html_body, "text/html")
            msg.send()
            return render(request, 'dataform/form.html', context)
        else:
            return render(request, 'dataform/error.html', {'error': form.errors})
