from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

RESET_PASSWORD_MAIL = '../templates/reset_password_email.html'
VALIDATION_ACCOUNT = '../templates/mail_validation_compte.html'


def sendmail_to_customer(token, user, type_mail, base_url, goal):
    ctx = {
        'username': user.username,
        'token': token,
        'baseUrl': base_url,
        'goal': goal
    }
    subject = "Plateforme AT_TAGGING"
    html_content = render_to_string(type_mail, context=ctx)
    text_content = "Don't reply"
    from_email = 'noreply@gmail.com'
    to = user.email
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
