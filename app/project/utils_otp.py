import pyotp
import qrcode

secret = 'dkjdjksdjsoidjkoedko'

totp = pyotp.TOTP(secret)

uri = totp.provisioning_uri(
    name='user@example.com',
    issuer_name='MyApp',
    image='https://cdn.pixabay.com/photo/2017/05/31/16/39/windows-2360920_1280.png'
)

print(uri)

qr = qrcode.make(uri)
qr.show()

otp_user = input('enter otp: ')
is_vaild = totp.verify(otp_user)
print(is_vaild)
