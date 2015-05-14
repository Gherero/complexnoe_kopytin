import redis
import hashlib
import getpass


r = redis.StrictRedis(host='localhost', port=6379, db=0)

A = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ' * 2  # алфавит
def f(mc, k, op): #непосредственно функция шифрования / дешифрования
    k *= len(mc) // len(k) + 1
    return ''.join([A[A.index(j) + int(k[i]) * op] for i, j in enumerate(mc)])


def encrypt(message, key):      #шифрование текста
    return f(message, key, 1)

def decrypt(ciphertext, key):       #дешифрование текста
    return f(ciphertext, key, -1)

def regist(username, passwrd):      #регистрация пользователей

    if(not len(passwrd)):           # если длина пароля 0
        return -3

    if(not len(username)):          # если длина логина 0
        return -2

    if(r.exists(username)):         #если пользователь существует
        return -1

    hash_object = hashlib.sha512(passwrd.encode()) # генерируем хеш
    hex_dig = hash_object.hexdigest()
    r.set(username,hex_dig)                         #заносим в БД имя пользователя (ключ) и хеш пароля (значение)
    return 0                                        #сообщаем об успехе

def auth(username, passwrd):                        #подпрограмма аутентификации

    if( not(len(username) and len(passwrd))):       #проверка длины логина , пароля
        return -1

    if(not r.exists(username)):                     #существует ли пользователь
        return -2

    hash_object = hashlib.sha512(passwrd.encode())  #генирируем хеш введенного пароля
    hex_dig = hash_object.hexdigest()

    dbhash=r.get(username)                          #достаем хеш из БД

    if(dbhash==hex_dig):                            #сравниваем хеш из БД с введенным
        return 0
def generate_key(text):
    key=''
    for element in text:
        key += str(ord(element))
    return key


swith=input(" (Р)регистрация/(А)аутентификация: ")
if  swith=="Р" or  swith=="р":
    print("Регистрация")
elif  swith=="А" or  swith=="а":
    print("Аутентификация")
else:
    print("Ведены не корректные данные \n Для завершения нажмите ENTER")
    input()
    exit()
username=input("Введите имя пользователя: ")
passwrd=getpass.getpass("Введите пароль: ")

if swith=="Р" or swith=="р" :
     status=regist(username,passwrd)
     if status==0:
         print("Регистрация успешна: ",username)
     else:
         print("Неверный логин либо пароль")
         print("Для завершения нажмите ENTER")
         input()
         exit()



elif swith=="А" or  swith=="а" :
    status=auth(username,passwrd)
    if status==0:
        print("Аутентификация успешна: ", username)
    else:
        print("Неверный логин либо пароль")
        print("Для завершения нажмите ENTER")
        input()
        exit()


swith=input("(Ш)шифрование\(Р)расшифровка")
if swith=="Ш" or swith=="ш":
    open_txt = input("Введите открытый текст: ")
    key_txt = input("Введите ключ: ")
    key_dic= generate_key(key_txt)
    print(encrypt(open_txt, key_dic))  # шифрование

elif swith=="Р" or swith=="р":
    secure_txt = input("Введите шифрованный текст: ")
    key_txt = input("Введите ключ: ")
    key_dic= generate_key(key_txt)
    print(decrypt(secure_txt,key_dic))  # расшифровывание

else:
    print("Ведены не корректные данные \n Для завершения нажмите ENTER")
    input()
    exit()