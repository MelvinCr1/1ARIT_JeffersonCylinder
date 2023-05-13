import random

cylinder_Number = 10
filename = 'test1.txt'


def random_String(filename, cylinder_Number):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open(filename, 'w') as f:
        for i in range(cylinder_Number):
            shuffled_alphabet = "".join(random.sample(alphabet, len(alphabet)))
            f.write(shuffled_alphabet + '\n')


def dictionaryBuild(filename):
    dictionary = {}
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            dictionary[i + 1] = line.strip()
    return dictionary


def is_permutation(lst):
    n = len(lst)
    # Vérification si la liste a la même longueur que l'intervalle [1, n]
    if n != max(lst) or min(lst) != 1:
        return False
    # Vérification si il y a des doublons
    if len(set(lst)) != n:
        return False
    else:
        return True


def read_permutations(file_name):
    permutations = {}
    with open(file_name, 'r') as f:
        for i, line in enumerate(f):
            permutations[i + 1] = line.strip()
    return permutations


def generate_permutation(n):
    permutation = list(range(1, n + 1))  # Création de la liste [1, 2, ..., n]
    random.shuffle(permutation)  # Mélange aléatoire de la liste
    return permutation


def letter_cipher(letter, permutation):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = permutation.index(letter)
    encrypted_letter = permutation[(index + 6) % len(alphabet)]
    return encrypted_letter
"""
#TEST / letter_cipher
print('-----TEST / letter_cipher-----')
permutation = 'NOZUTWDCVRJLXKISEFAPMYGHBQ'
lettre = 'Z'
lettre_chiffree = letter_cipher(lettre, permutation)
print(lettre_chiffree) # Output : 'V'

lettre = 'B'
lettre_chiffree = letter_cipher(lettre, permutation)
print(lettre_chiffree) # Output : 'T'
"""

def letter_decipher(letter, permutation):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = permutation.index(letter)
    decrypted_letter = permutation[(index - 6) % len(alphabet)]
    return decrypted_letter
"""
#TEST / letter_decipher
print('-----TEST / letter_decipher-----')
permutation = 'NOZUTWDCVRJLXKISEFAPMYGHBQ'
lettre = 'V'
lettre_chiffree = letter_decipher(lettre, permutation)
print(lettre_chiffree) # Output : 'Z'

lettre = 'T'
lettre_chiffree = letter_decipher(lettre, permutation)
print(lettre_chiffree) # Output : 'B'
"""

def jefferson_encryption(text, cylinder, key):
    text = text.upper()
    text = ''.join(filter(str.isalpha, text))

    ciphertext = ''
    for i, letter in enumerate(text):
        permutation = cylinder[int(str(key[i % len(key)]))]
        ciphertext += letter_cipher(letter, permutation)
    return ciphertext

def jefferson_decryption(text, cylinder, key):
    text = text.upper()
    text = ''.join(filter(str.isalpha, text))
    deciphertext = ''
    for i, letter in enumerate(text):
        permutation = cylinder[int(str(key[i % len(key)]))]
        deciphertext += letter_decipher(letter, permutation)
    return deciphertext


# EXECUTION/
"""
print("-----Tests global encryption-----")
#test = random_String('test1.txt', cylinder_Number)
dictionary = dictionaryBuild('test1.txt')
print(dictionary)
cylinder = read_permutations('test1.txt')
ciphertext = jefferson_encryption('ceciestlemessage', cylinder, [7, 9, 5, 10, 1, 6, 3, 8, 2, 4])
print("Texte chiffré", ciphertext)
"""

"""
print("-----Tests global decryption-----")
dictionary1 = dictionaryBuild('test1.txt')
print(dictionary)
cylinder = read_permutations('test1.txt')
deciphertext = jefferson_decryption('HFDTKCVCMRVG', cylinder, [7, 9, 5, 10, 1, 6, 3, 8, 2, 4])
print("Texte déchiffré", deciphertext)
"""