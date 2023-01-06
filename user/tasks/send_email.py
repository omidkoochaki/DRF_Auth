from celery import shared_task


@shared_task(name='send_activation_email')
def send_email(email, code):
    print('Sending Email -------------------------')
    print(f'the Email Address is: {email}')
    print(f'the activation URL is localhost:8000/?email={email}&code={code}')
    print('/ Sending Email -------------------------')
