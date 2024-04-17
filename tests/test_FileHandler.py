from src.FileHandler import FileHandler


def test_FileHandler():
    file_handler = FileHandler()

    data = "Питон! Че у тебя тут за заварушка?"
    data_1 = "Умцтс! Ыи ч циег цчц лд лдёдфчьод?"

    file_handler.write_to_file('tests/Test3.txt', data)
    file_handler.encrypt_file('tests/Test3.txt', 'cesar', 'rus', '4')
    assert file_handler.read_file('tests/Result.txt') == data_1

    file_handler.write_to_file('tests/Test3.txt', data_1)
    file_handler.decrypt_file('tests/Test3.txt', 'cesar', 'rus', '4')

    assert file_handler.read_file('tests/Result.txt') == data

    key = "Гуф"
    file_handler.write_to_file('tests/Test3.txt', data)
    file_handler.encrypt_file('tests/Test3.txt', 'vigenere', 'rus', key)
    data_1 = 'Тьжсб! Лз ж жзфу хжж ку ьгхфужмну?'

    assert file_handler.read_file('tests/Result.txt') == data_1

    file_handler.write_to_file('tests/Test3.txt', data_1)
    file_handler.decrypt_file('tests/Test3.txt', 'vigenere', 'rus', key)

    assert file_handler.read_file('tests/Result.txt') == data

    file_handler.write_to_file('tests/Test3.txt', data)
    file_handler.encrypt_file('tests/Test3.txt', 'vernam', 'rus', key)
    data_1 = 'Лъёмэ! Гё а ёёск раё дт тгруталит?'

    assert file_handler.read_file('tests/Result.txt') == data_1
    file_handler.decrypt_file('tests/Test3.txt', 'vernam', 'rus', key)

    file_handler.decrypt_file('tests/Test2.txt', 'statistical_caesar', 'rus')
    assert file_handler.read_file('tests/Result.txt') == file_handler.read_file('tests/Test.txt')
