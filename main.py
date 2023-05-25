import random

class Main:
    def __init__(self, cylinder_Number, filename):
        self.cylinder_Number = cylinder_Number
        self.filename = filename

    def random_String(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        with open(self.filename, 'w') as f:
            for i in range(self.cylinder_Number):
                shuffled_alphabet = "".join(random.sample(alphabet, len(alphabet)))
                f.write(shuffled_alphabet + '\n')

    def dictionaryBuild(self):
        dictionary = {}
        with open(self.filename, 'r') as f:
            for i, line in enumerate(f):
                dictionary[i + 1] = line.strip()
        return dictionary

    def is_permutation(self, lst):
        n = len(lst)
        if n != max(lst) or min(lst) != 1:
            return False
        if len(set(lst)) != n:
            return False
        return True

    def read_permutations(self):
        permutations = {}
        with open(self.filename, 'r') as f:
            for i, line in enumerate(f):
                permutations[i + 1] = line.strip()
        return permutations

    def generate_permutation(self, n):
        permutation = list(range(1, n + 1))
        random.shuffle(permutation)
        return permutation

    def letter_cipher(self, letter, permutation):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        index = permutation.index(letter)
        encrypted_letter = permutation[(index + 6) % len(alphabet)]
        return encrypted_letter

    def letter_decipher(self, letter, permutation):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        index = permutation.index(letter)
        decrypted_letter = permutation[(index - 6) % len(alphabet)]
        return decrypted_letter

    def jefferson_encryption(self, text, cylinder, key):
        text = text.upper()
        text = ''.join(filter(str.isalpha, text))

        ciphertext = ''
        for i, letter in enumerate(text):
            permutation = cylinder[int(str(key[i % len(key)]))]
            ciphertext += self.letter_cipher(letter, permutation)
        return ciphertext

    def jefferson_decryption(self, text, cylinder, key):
        text = text.upper()
        text = ''.join(filter(str.isalpha, text))
        deciphertext = ''
        for i, letter in enumerate(text):
            permutation = cylinder[int(str(key[i % len(key)]))]
            deciphertext += self.letter_decipher(letter, permutation)
        return deciphertext

# EXEMPLE D'UTILISATION
main = Main(10, 'test1.txt')
main.random_String()
dictionary = main.dictionaryBuild()
print(dictionary)
cylinder = main.read_permutations()
ciphertext = main.jefferson_encryption('ceciestlemessage', cylinder, [7, 9, 5, 10, 1, 6, 3, 8, 2, 4])
print("Texte chiffré:", ciphertext)
deciphertext = main.jefferson_decryption(ciphertext, cylinder, [7, 9, 5, 10, 1, 6, 3, 8, 2, 4])
print("Texte déchiffré:", deciphertext)
