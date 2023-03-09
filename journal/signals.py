# from allauth.account.signals import user_signed_up
# from django.dispatch import receiver
# from django.core.mail import send_mail


# @receiver(user_signed_up)
# def send_signup_email(sender, request, user, **kwargs):
#     subject = 'Welcome to Trading Journal!'
#     message = f'Hi {user.username},\n\nThank you for signing up on My Site!'
#     from_email = 'tradingjournaltest@gmail.com'
#     recipient_list = [user.email]
#     send_mail(subject, message, from_email, recipient_list, fail_silently=False)
