from src.Cipher import *


class CesarStatisticsDecipher:
    alphabets = dict(rus=["абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"],
                     eng=["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"], )

    def __init__(self):
        pass

    statistics_data_eng = {
        'a': 8.17,
        'b': 1.49,
        'c': 2.78,
        'd': 4.25,
        'e': 12.70,
        'f': 2.23,
        'g': 2.02,
        'h': 6.09,
        'i': 6.97,
        'j': 0.15,
        'k': 0.77,
        'l': 4.03,
        'm': 2.41,
        'n': 6.75,
        'o': 7.51,
        'p': 1.93,
        'q': 0.10,
        'r': 5.99,
        's': 6.33,
        't': 9.06,
        'u': 2.76,
        'v': 0.98,
        'w': 2.36,
        'x': 0.15,
        'y': 1.97,
        'z': 0.07
    }

    statistics_data_ru = {
        'а': 8.01,
        'б': 1.59,
        'в': 4.54,
        'г': 1.70,
        'д': 2.98,
        'е': 8.45,
        'ё': 0.04,
        'ж': 0.94,
        'з': 1.65,
        'и': 7.35,
        'й': 1.21,
        'к': 3.49,
        'л': 4.40,
        'м': 3.21,
        'н': 6.70,
        'о': 10.97,
        'п': 2.81,
        'р': 4.73,
        'с': 5.47,
        'т': 6.26,
        'у': 2.62,
        'ф': 0.26,
        'х': 0.97,
        'ц': 0.48,
        'ч': 1.44,
        'ш': 0.73,
        'щ': 0.36,
        'ъ': 0.04,
        'ы': 1.90,
        'ь': 1.74,
        'э': 0.32,
        'ю': 0.64,
        'я': 2.01
    }

    def collect_statistics_from_text(self, text: str, alph: str) -> dict:
        dictionary = {i: 0 for i in self.alphabets[alph][0]}
        l = 0
        for letter in text:
            if letter.lower() in self.alphabets[alph][0]:
                dictionary[letter.lower()] += 100
                l += 1
        for i in dictionary:
            dictionary[i] /= l
        return dictionary

    def generate_shifted_alph(self, shift: int, alph: str) -> str:
        cyp = CesarCipher(shift)
        return cyp.encrypt(alphabets[alph][0], alph)

    def find_opt_step(self, text: str, alph: str) -> int:
        statistics_data_text = self.collect_statistics_from_text(text, alph)
        if alph == 'eng':
            statistics_data_lang = self.statistics_data_eng
        else:
            statistics_data_lang = self.statistics_data_ru
        """using standard deviation"""
        min_standard_deviation = 1000000
        res = 0
        lst = list(statistics_data_text.values())
        for i in range(0, len(alphabets[alph][0])):
            new_alpha = self.generate_shifted_alph(i, alph)
            temp_dictionary = {j: lst[(new_alpha.index(j)) % len(new_alpha)] for j in new_alpha}
            standard_deviation = (sum(
                (statistics_data_lang[char] - temp_dictionary[char]) ** 2 for char in new_alpha) / len(
                new_alpha)) ** 0.5
            if min_standard_deviation > standard_deviation:
                res, min_standard_deviation = i, standard_deviation
        print(res)
        return res
