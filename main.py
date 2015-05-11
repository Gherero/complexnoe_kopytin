##import redis

A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2  # алфавит
def f(mc, k, op):
    k *= len(mc) // len(k) + 1
    return ''.join([A[A.index(j) + int(k[i]) * op] for i, j in enumerate(mc)])


def encrypt(message, key):
    return f(message, key, 1)

def decrypt(ciphertext, key):
    return f(ciphertext, key, -1)


print(encrypt('GRONSFELD', '2015'))  # шифрование

print(decrypt('IRPSUFFQF', '2015'))  # расшифровывание