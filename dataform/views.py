from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


from .models import EmailForm, EmailImage

from django.views import View
from .forms import DataForm
from django.conf import settings

from datetime import date

from email.mime.image import MIMEImage




usermessage = 'Здравствуйте, Илья! Хочу с Вами связаться по поводу недвижимости. Жду Вашего звонка!'

class DataFormView(View):

    def get(self, request):
        form = DataForm(initial={'mes': usermessage})
        return render(request, 'dataform/form.html', {'form': form, 'form_window': True})

    def post(self, request):
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            context = form.cleaned_data
            name = context['name'],
            email = context['email'],
            phone = context['phone'],
            mes = context['mes'],
            image = request.FILES.getlist('image')

            print(request.FILES.getlist('image'))



            attempts = EmailForm.objects.filter(phone=phone, date__gte=date.today()).count()

            print('Attempts today: ', attempts)
            if attempts < 5:
                data_form = EmailForm.objects.create(name=name, email=email, phone=phone, mes=mes)
                for item in image:
                    EmailImage.objects.create(form=data_form, image=item)

                last = EmailForm.objects.last()
                data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'mes': mes,
                    'image': last.images.all()
                }

                print(image[0].content_type)


                html_body = render_to_string('dataform/email.html', data)
                msg = EmailMultiAlternatives(subject="Feedback - mrealt.by", from_email=settings.EMAIL_HOST_USER,
                                             to=["pyasecky2012pavel@mail.ru"])

                msg.attach_alternative(html_body, "text/html")

                for img_file in image:
                    # rewind file object, make sure it open
                    img_file.open('rb')
                    try:
                        # directly read in data from uploaded file object
                        img_data = img_file.read()
                        msg_img = MIMEImage(img_data)
                        msg.attach(msg_img)
                    finally:
                        # not strictly mandated by django, but why not
                        img_file.close()

                msg.send()

                success = "Форма успешно отправлена! Благодарим за Ваше участие!"
                return render(request, 'dataform/form.html', {'success': success, 'form_window': False})
            else:
                alarm = ("К сожалению, вы израсходовали Вашу дневную норму отправки формы! (5 попыток)", "Благодарим за понимание!")
                return render(request, 'dataform/form.html', {'alarm': alarm, 'form_window': False})

        else:
            form_new = DataForm(request.POST, request.FILES)
            return render(request, 'dataform/email.html', {'form': form_new, 'error': form.errors, 'form_window': True})
