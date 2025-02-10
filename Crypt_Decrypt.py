from hashlib import sha256
entree = input('put the name of the files to crypt or decrypt : ')
sortie = input('put the final name of the files: ')
key = input('put the key: ')

keys = sha256(key.encode('utf-8')).digest()

with open(entree, 'rb') as fentree:
    with open(sortie, 'wb') as fsortie:
        i = 0
        while fentree.peek():
            c = ord(fentree.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            fsortie.write(b)
            i = i + 1