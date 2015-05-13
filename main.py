import redis
import hashlib
r = redis.StrictRedis(host='localhost', port=6379, db=0)



A = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' * 2  # алфавит
def f(mc, k, op):
    k *= len(mc) // len(k) + 1
    return ''.join([A[A.index(j) + int(k[i]) * op] for i, j in enumerate(mc)])


def encrypt(message, key):      #шифрование текста
    return f(message, key, 1)

def decrypt(ciphertext, key):       #дешифровка
    return f(ciphertext, key, -1)

def regist(username, passwrd):      #регистрация пользователей

    if(not len(passwrd)):           # если длина пароля 0
        return -3

    if(not len(username)):          # если длина логина 0
        return -2

    if(r.exists(username)):         #если пользователь существует
        return -1

    hash_object = hashlib.sha256(passwrd.encode()) # генерируем хеш
    hex_dig = hash_object.hexdigest()
    r.set(username,hex_dig)                         #заносим в БД имя пользователя (ключ) и хеш пароля (значение)
    return 0                                        #сообщаем об успехе

def auth(username, passwrd):

    if( not(len(username) and len(passwrd))):       #проверка длины логина , пароля
        return -1

    if(not r.exists(username)):                     #существует ли пользователь
        return -2

    hash_object = hashlib.sha256(passwrd.encode())  #генирируем хеш введенного пароля
    hex_dig = hash_object.hexdigest()

    dbhash=r.get(username)                          #достаем хеш из БД

    if(dbhash==hex_dig):                            #сравниваем хеш из БД с введенным
        return 0
    print("Успех")


print(auth("kirill","1234"))
print(encrypt('kirill45', '2015'))  # шифрование

print(decrypt('misnnl', '2015'))  # расшифровывание