import redis
import hashlib
r = redis.StrictRedis(host='localhost', port=6379, db=0)



A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2  # алфавит
def f(mc, k, op):
    k *= len(mc) // len(k) + 1
    return ''.join([A[A.index(j) + int(k[i]) * op] for i, j in enumerate(mc)])


def encrypt(message, key):
    return f(message, key, 1)

def decrypt(ciphertext, key):
    return f(ciphertext, key, -1)

def regist(username, passwrd):
    if(r.exist(username)):
        return -1

    if(not len(passwrd)):
        return -1
    hash_object = hashlib.sha256(passwrd.encode())
    hex_dig = hash_object.hexdigest()
    r.set(username,passwrd)
    return 0


print(encrypt('GRONSFELD', '2015'))  # шифрование

print(decrypt('IRPSUFFQF', '2015'))  # расшифровывание