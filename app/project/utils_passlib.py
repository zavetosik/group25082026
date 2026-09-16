from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')

password = "aa"
hash = context.hash(secret=password)
print(hash)

