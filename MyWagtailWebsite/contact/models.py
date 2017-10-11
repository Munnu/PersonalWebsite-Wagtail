from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.core.mail import send_mail as django_send_mail
from django.core.mail import get_connection
from django.core.mail.message import EmailMultiAlternatives

from wagtailcaptcha.models import WagtailCaptchaEmailForm
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)

from wagtail.wagtailadmin.utils import send_mail as wagtailadmin_send_mail

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
        super(FormPage, self).__init__(*args, **kwargs)  # inheriting the WagtailCaptchaEmailForm constructor
        self.reply_to = None

    def send_mail(self, form, from_email=None):
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
                self.reply_to = value
                continue
            content.append('{}: {}'.format(field.label, value))
        content = '\n'.join(content)

        # took this line from wagtail_send_email
        if not from_email:
            if hasattr(settings, 'WAGTAILADMIN_NOTIFICATION_FROM_EMAIL'):
                from_email = settings.WAGTAILADMIN_NOTIFICATION_FROM_EMAIL
            elif hasattr(settings, 'DEFAULT_FROM_EMAIL'):
                from_email = settings.DEFAULT_FROM_EMAIL
            else:
                from_email = 'webmaster@localhost'

        # wagtailadmin_send_mail(self.subject, content, addresses, from_email=self.from_address,)
        # bypassing wagtail's send_mail function for now, due to its conditional statements on defaulting 'from' email
        # commenting this section out below because I want the form submission email addr in my email criteria
        # django_send_mail(self.subject, content, from_email=self.from_address, recipient_list=[self.to_address])
        send_mail_with_reply_to_field(self.subject, content, from_email, recipient_list=[self.to_address],
                         reply_to=[self.reply_to])


def send_mail_with_reply_to_field(subject, message, from_email, recipient_list,
                                  fail_silently=False,  reply_to=None, auth_user=None, auth_password=None,
                                  connection=None, html_message=None):
    """
    This function replaces send_mail in django.core.mail in order to have reply_to functionality.

    Easy wrapper for sending a single message to a recipient list. All members
    of the recipient list will see the other recipients in the 'To' field.

    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    Note: The API for this method is frozen. New code wanting to extend the
    functionality should use the EmailMessage class directly.
    """
    connection = connection or get_connection(
        username=auth_user,
        password=auth_password,
        fail_silently=fail_silently,
    )  # get_connection imported from django.core.mail
    mail = EmailMultiAlternatives(subject, message, from_email, recipient_list,
                                  reply_to=reply_to, connection=connection)
    if html_message:
        mail.attach_alternative(html_message, 'text/html')

    return mail.send()

