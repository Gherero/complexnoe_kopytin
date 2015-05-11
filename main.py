import redis
import hashlib
r = redis.StrictRedis(host='localhost', port=6379, db=0)



A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2  # алфавит
def f(mc, k, op):
    k *= len(mc) // len(k) + 1
    return ''.join([A[A.index(j) + int(k[i]) * op] for i, j in enumerate(mc)])


def encrypt(message, key):      #шифрование текста
    return f(message, key, 1)

def decrypt(ciphertext, key):   #дешифровка
    return f(ciphertext, key, -1)

def regist(username, passwrd):  #регистрация пользователей

    if(not len(passwrd)):
        return -2

    if(r.exists(username)):
        return -1

    hash_object = hashlib.sha256(passwrd.encode())
    hex_dig = hash_object.hexdigest()
    r.set(username,hex_dig)
    return 0

print(regist("kirill",""))
print(encrypt('GRONSFELD', '2015'))  # шифрование

print(decrypt('IRPSUFFQF', '2015'))  # расшифровывание