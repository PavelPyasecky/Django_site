from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import EmailForm, EmailImage

from django.views import View
from .forms import DataForm
from django.conf import settings

from datetime import date




usermessage = 'Здравствуйте, Илья! Хочу с Вами связаться по поводу недвижимости. Жду Вашего звонка!'

class DataFormView(View):

    def get(self, request):
        form = DataForm(initial={'mes': usermessage})
        return render(request, 'dataform/form.html', {'form': form})

    def post(self, request):
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            context = form.cleaned_data
            name = context['name'],
            email = context['email'],
            phone = context['phone'],
            mes = context['mes'],
            image = context['image']




            # all = EmailForm.objects.all()
            # for item in all:
            #     print(f'Name: {item.name}, phone: {item.phone}, email: {item.email}, message: {item.mes}, image: {item.image}, image.url: {item.image.url}')

            attempts = EmailForm.objects.filter(phone=phone, date__gte=date.today()).count()

            print('Attempts today: ', attempts)
            if attempts < 100:
                data_form = EmailForm(name=name, email=email, phone=phone, mes=mes)
                data_form.save()
                img = EmailImage(form=data_form, image=image)
                img.save()
            else:
                return render(request, 'dataform/error.html', {'error': form.errors})

            print(context['name'])
            print(context['email'])
            print(context['phone'])
            print(context['mes'])
            print(image)

            print("-"*50)
            last = EmailForm.objects.last()
            data = {
                'name': name,
                'email': email,
                'phone': phone,
                'mes': mes,
                'image': last.emailimage_set.all()
            }

            # str_text = ''
            # for line in file:
            #     str_text = str_text + line.decode()  # "str_text" will be of `str` type

            html_body = render_to_string('dataform/email.html', data)
            msg = EmailMultiAlternatives(subject="Feedback - mrealt.by", from_email=settings.EMAIL_HOST_USER, to=["pyasecky2012pavel@mail.ru"])
            msg.attach_alternative(html_body, "text/html")
            #msg.attach(file.name, content=data_file, mimetype=file.content_type)
            #msg.send()

            return render(request, 'dataform/form.html', data)
        else:
            return render(request, 'dataform/error.html', {'error': form.errors})
