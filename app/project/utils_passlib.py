from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')

password = "aa35ui"
hash = context.hash(secret=password)
print(hash)

is_valid = context.verify(secret=password, hash=hash)
print(is_valid)

