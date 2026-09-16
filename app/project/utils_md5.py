import hashlib

data = 'krgkefriogjeifogjeogfi'.encode()
print(data)

hash_md5 = hashlib.md5(data).hexdigest()
print(hash_md5)