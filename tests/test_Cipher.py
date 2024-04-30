from src.Cipher import *

def test_cipher():
    cesar_obj = CesarCipher(4)
    cesar_obj_1 = CesarCipher(4)

    data = "Питон! Че у тебя тут за заварушка?"
    data_1 = "Умцтс! Ыи ч циег цчц лд лдёдфчьод?"

    assert cesar_obj.encrypt(data, 'rus') == data_1
    assert cesar_obj_1.decrypt(data_1, 'rus') == data

    key = "Гуф"
    vigenere_obj = VigenereCipher(key)
    data_1 = 'Тьжсб! Лз ж жзфу хжж ку ьгхфужмну?'
    assert vigenere_obj.encrypt(data, 'rus') == data_1
    assert vigenere_obj.decrypt(data_1, 'rus') == data

    vernam_obj = VernamCipher(key)
    data_1 = 'Лъёмэ! Гё а ёёск раё дт тгруталит?'
    assert vernam_obj.encrypt(data, 'rus') == data_1



