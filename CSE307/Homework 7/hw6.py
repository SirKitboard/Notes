import hashlib
import crypt

# value = hashlib.sha512('qwerty'+'password').hexdigest()
# print(hashlib.sha512('qwerty'+'password').hexdigest())

print(crypt.crypt('password', 'qwerty'))
