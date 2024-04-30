class CesarCipher:
    alphabets = dict(
        rus="абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        eng="abcdefghijklmnopqrstuvwxyz"
    )

    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text: str, alph: str) -> str:
        al = self.alphabets[alph]
        data = ''
        for char in text:
            if char.lower() in al:
                if char.lower() == char:
                    data += al[(al.find(char) + self.shift) % len(al)].lower()
                else:
                    data += al[(al.find(char.lower()) + self.shift) % len(al)].upper()
            else:
                data += char
        return data

    def decrypt(self, text: str, alph: str) -> str:
        al = self.alphabets[alph]
        data = ''
        for char in text:
            if char.lower() in al:
                if char.lower() == char:
                    data += al[(al.find(char) - self.shift) % len(al)].lower()
                else:
                    data += al[(al.find(char.lower()) - self.shift) % len(al)].upper()
            else:
                data += char
        return data


def generate_vigenere_table(alphabet: str) -> dict:
    vigenere_tableble = {}
    delta = 0
    for i, char in enumerate(alphabet):
        row = {}
        for j in range(len(alphabet)):
            row[alphabet[(i + j) % len(alphabet)]] = alphabet[(i + j + delta) % len(alphabet)]
        vigenere_tableble[char] = row
        delta += 1

    return vigenere_tableble


alphabets = dict(rus=["абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"],
                 eng=["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
                 all="аАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯaAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ")


def GenKey(keyword, text):
    key = ''
    j = 0
    for i in range(len(text)):
        if text[i] in alphabets["all"]:
            if text[i] == text[i].upper():
                key += keyword[j % len(keyword)].upper()
            elif text[i] == text[i].lower():
                key += keyword[j % len(keyword)].lower()
            j += 1
        else:
            key += text[i]
    return key


class VigenereCipher:

    def __init__(self, keyword):
        self.keyword = keyword

    def encrypt(self, text: str, alph: str) -> str:
        key = GenKey(self.keyword, text)
        vigenere_tableble_small = generate_vigenere_table(alphabets[alph][0])
        vigenere_tableble_big = generate_vigenere_table(alphabets[alph][1])
        encrypted_text = ''
        for i in range(len(text)):
            if text[i] in alphabets[alph][0]:
                encrypted_text += vigenere_tableble_small[text[i]][key[i]]
            elif text[i] in alphabets[alph][1]:
                encrypted_text += vigenere_tableble_big[text[i]][key[i]]
            else:
                encrypted_text += text[i]
        return encrypted_text

    def decrypt(self, text: str, alph: str) -> str:
        key = GenKey(self.keyword, text)
        vigenere_tableble_small = generate_vigenere_table(alphabets[alph][0])
        vigenere_tableble_big = generate_vigenere_table(alphabets[alph][1])
        decrypted_text = ''
        for i in range(len(text)):
            if text[i] in alphabets[alph][0]:
                decrypted_text += vigenere_tableble_small[text[i]][
                    alphabets[alph][0][(len(alphabets[alph][0]) - alphabets[alph][0].find(key[i])) % len(
                        alphabets[alph][0])]]
            elif text[i] in alphabets[alph][1]:
                decrypted_text += vigenere_tableble_big[text[i]][
                    alphabets[alph][1][(len(alphabets[alph][1]) - alphabets[alph][1].find(key[i])) % len(
                        alphabets[alph][1])]]
            else:
                decrypted_text += text[i]
        return decrypted_text


class VernamCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encrypt(self, text: str, alph: str) -> str:
        key = GenKey(self.keyword, text)
        result = ''
        for text_char, key_char in zip(text, key):
            if text_char not in alphabets["all"]:
                result += text_char
            else:
                if text_char in alphabets[alph][0]: i = 0
                else: i = 1
                result += alphabets[alph][i][
                    ((ord(text_char) - ord(alphabets[alph][i][0])) ^ (ord(key_char) - ord(alphabets[alph][i][0]))) % len(
                        alphabets[alph][i])]
        return result

    def decrypt(self, text: str, alph: str) -> str:
        return self.encrypt(text, alph)

