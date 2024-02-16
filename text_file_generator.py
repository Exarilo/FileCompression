import os
import random
import string

size = ''
while not size.isnumeric():
    size = input('Taille du fichier en MB : ')

size = int(size) * 1000000  

name = input('Nom du fichier : ')

file_path = os.path.join("1_Initial", name + ".txt")

with open(file_path, 'w') as file:
    for _ in range(size // 100):
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        file.write(random_chars)

print('Fichier généré avec succès!')
