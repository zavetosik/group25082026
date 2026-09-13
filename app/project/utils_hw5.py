import jwt

import datetime

from time import sleep

JWT_SECRET = 'fjwofjwifnihf9843rhfu93hn3kdoko20dk90i24dj492i0kom'

payload = {
    "sub": '9999',
    "iat": datetime.datetime.now(datetime.UTC),
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=5),

    "userSurname": "Chykota",
    "groupNumber": 25082026,
}

jwt_encode = jwt.encode(
    payload=payload,
    key=JWT_SECRET,
    algorithm='HS256'
)
print(f"{jwt_encode}\n")

# sleep(6)
# decode = jwt.decode(
#     jwt=jwt_encode,
#     key=JWT_SECRET,
#     algorithms=['HS256']
# )
# print(decode)

decode = jwt.decode(
    jwt=jwt_encode,
    key=JWT_SECRET + 'x',
    algorithms=['HS256']
)
print(decode)