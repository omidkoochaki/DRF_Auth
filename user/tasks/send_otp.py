from celery import shared_task


@shared_task(name='send_activation_sms')
def send_otp(number, code):
    print('Sending SMS -------------------------')
    print(f'the phone number is: {number}')
    print(f'the activation code is {code}')
    print('/ Sending SMS -------------------------')
