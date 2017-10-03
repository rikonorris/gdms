from django.core.mail import send_mail
from django.template.loader import render_to_string


from system.settings import DEFAULT_FROM_EMAIL


def send_letter(subject, template_name, context, email):

    template_html = render_to_string('emails/' + template_name, context)
    if not type(email) is list:
        email = [email]

    send_mail(
        subject,
        template_html,
        DEFAULT_FROM_EMAIL,
        email,
        html_message=template_html,
    )
