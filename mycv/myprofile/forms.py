from django import forms
from django.conf import settings

from .mail import send_mail_template


class ContactForm(forms.Form):

    subject = forms.CharField(label='Subject', max_length=100)
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)

    def send_mail(self):
        print(self.cleaned_data)
        subject = self.cleaned_data['subject']
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'pages/contact_email.html'

        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
