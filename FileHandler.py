from Cipher import *
from CesarStatisticsDecipher import *
import os


class FileHandler:
    def __init__(self):
        pass

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            return data

    def write_to_file(self, file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)

    def encrypt_file(self, file_path, cipher):
        if cipher == "cesar":
            alph = input("Enter alphabet:\n")
            shift = int(input("Enter shift:\n"))
            data = self.read_file(file_path)
            result = CesarCipher(shift).encrypt(data, CesarCipher.alphabets[alph])
            dir_path = os.path.dirname(file_path)
            result_file_path = os.path.join(dir_path, 'result.txt')
            self.write_to_file(result_file_path, result)

        elif cipher == "vigenere":
            alph = input("Enter alphabet:\n")
            keyword = input("Enter keyword:\n")
            data = self.read_file(file_path)
            result = VigenereCipher(keyword).encrypt(data, alph)
            dir_path = os.path.dirname(file_path)
            result_file_path = os.path.join(dir_path, 'result.txt')
            self.write_to_file(result_file_path, result)

        elif cipher == "vernam":
            alph = input("Enter alphabet:\n")
            keyword = input("Enter keyword:\n")
            data = self.read_file(file_path)
            result = VernamCipher(keyword).encrypt(data, alph)
            dir_path = os.path.dirname(file_path)
            result_file_path = os.path.join(dir_path, 'result.txt')
            self.write_to_file(result_file_path, result)

    #
    def decrypt_file(self, file_path, cipher):
        if cipher == "cesar":
            alph = input("Enter alphabet:\n")
            shift = int(input("Enter shift:\n"))
            data = self.read_file(file_path)
            result = CesarCipher(shift).decrypt(data, CesarCipher.alphabets[alph])
            dir_path = os.path.dirname(file_path)
            result_file_path = os.path.join(dir_path, 'result.txt')
            self.write_to_file(result_file_path, result)

        elif cipher == "vigenere":
            alph = input("Enter alphabet:\n")
            keyword = input("Enter keyword:\n")
            data = self.read_file(file_path)
            result = VigenereCipher(keyword).decrypt(data, alph)
            dir_path = os.path.dirname(file_path)
            result_file_path = os.path.join(dir_path, 'result.txt')
            self.write_to_file(result_file_path, result)

        elif cipher == "vernam":
            alph = input("Enter alphabet:\n")
            keyword = input("Enter keyword:\n")
            data = self.read_file(file_path)
            result = VernamCipher(keyword).decrypt(data, alph)
            dir_path = os.path.dirname(file_path)
            result_file_path = os.path.join(dir_path, 'result.txt')
            self.write_to_file(result_file_path, result)


        elif cipher == "statistical_caesar":
            alph = input("Enter alphabet:\n")
            data = self.read_file(file_path)
            shift = CesarStatisticsDecipher().find_opt_step(data, alph)
            result = CesarCipher(shift).encrypt(data, CesarCipher.alphabets[alph])
            dir_path = os.path.dirname(file_path)
            result_file_path = os.path.join(dir_path, 'result.txt')
            self.write_to_file(result_file_path, result)
