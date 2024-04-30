from django.urls import reverse_lazy
from django.conf import settings

from django.views.generic import FormView
from django import forms
#
from .sendgrid_example import send_mail_sendgrid

class EmailForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    


class EnviarMesaje(FormView):
    template_name = 'index.html'
    form_class = EmailForm
    success_url = reverse_lazy('send-mail')
    
    def form_valid(self, form):
        print(form.cleaned_data['email'])
        send_mail_sendgrid()
        return super().form_valid(form)
        
