from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailadmin.utils import send_mail as wagtailadmin_send_mail
from django.core.mail import send_mail as django_send_mail


from wagtailcaptcha.models import WagtailCaptchaEmailForm
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


    def __init__(self, *args, **kwargs):
        super(FormPage, self).__init__(*args, **kwargs)

    def send_mail(self, form):
        addresses = [x.strip() for x in self.to_address.split(',')]
        content = []
        for field in form:
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            if str(field.label) == 'Subject':
                self.subject = value
                continue
            elif str(field.label) == 'Email':
                self.from_address = value
                continue
            content.append('{}: {}'.format(field.label, value))
        content = '\n'.join(content)
        # wagtailadmin_send_mail(self.subject, content, addresses, from_email=self.from_address,)
        # bypassing wagtail's send_mail function for now, due to its conditional statements on defaulting 'from' email
        django_send_mail(self.subject, content, from_email=self.from_address, recipient_list=[self.to_address])
