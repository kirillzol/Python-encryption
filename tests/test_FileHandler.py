import shutil

from src.FileHandler import FileHandler
import tempfile
import os


def test_FileHandler():
    file_handler = FileHandler()

    data = "Питон! Че у тебя тут за заварушка?"
    data_1 = "Умцтс! Ыи ч циег цчц лд лдёдфчьод?"
    temp_dir = tempfile.mkdtemp()

    try:
        result_file_path = os.path.join(temp_dir, "Result.txt")
        file_handler.write_to_file(os.path.join(temp_dir, "Result.txt"), '')
        file_handler.write_to_file(os.path.join(temp_dir, "temp_file.txt"), data)
        file_handler.encrypt_file(os.path.join(temp_dir, "temp_file.txt"), 'cesar', 'rus', '4')
        assert file_handler.read_file(result_file_path) == data_1
        file_handler.write_to_file(os.path.join(temp_dir, "temp_file.txt"), data_1)
        file_handler.decrypt_file(os.path.join(temp_dir, "temp_file.txt"), 'cesar', 'rus', '4')
        assert file_handler.read_file(result_file_path) == data
    finally:
        shutil.rmtree(temp_dir)

    key = "Гуф"

    temp_dir = tempfile.mkdtemp()
    try:
        result_file_path = os.path.join(temp_dir, "result.txt")
        file_handler.write_to_file(os.path.join(temp_dir, "result.txt"), '')
        file_handler.write_to_file(os.path.join(temp_dir, "temp_file.txt"), data)
        file_handler.encrypt_file(os.path.join(temp_dir, "temp_file.txt"), 'vigenere', 'rus', key)
        data_1 = 'Тьжсб! Лз ж жзфу хжж ку ьгхфужмну?'
        assert file_handler.read_file(result_file_path) == data_1
        file_handler.write_to_file(os.path.join(temp_dir, "temp_file.txt"), data_1)
        file_handler.decrypt_file(os.path.join(temp_dir, "temp_file.txt"), 'vigenere', 'rus', key)
        assert file_handler.read_file(result_file_path) == data
    finally:
        shutil.rmtree(temp_dir)

    temp_dir = tempfile.mkdtemp()
    try:
        result_file_path = os.path.join(temp_dir, "Result.txt")
        file_handler.write_to_file(os.path.join(temp_dir, "Result.txt"), '')
        file_handler.write_to_file(os.path.join(temp_dir, "temp_file.txt"), data)
        file_handler.encrypt_file(os.path.join(temp_dir, "temp_file.txt"), 'vernam', 'rus', key)
        data_1 = 'Лъёмэ! Гё а ёёск раё дт тгруталит?'
        assert file_handler.read_file(result_file_path) == data_1
        file_handler.write_to_file(os.path.join(temp_dir, "temp_file.txt"), data_1)
        file_handler.decrypt_file(os.path.join(temp_dir, "temp_file.txt"), 'vernam', 'rus', key)
    finally:
        shutil.rmtree(temp_dir)

    data = file_handler.read_file("tests/Test2.txt")
    temp_dir = tempfile.mkdtemp()

    try:
        result_file = os.path.join(temp_dir, "Result.txt")
        file_handler.write_to_file(os.path.join(temp_dir, "Result.txt"), '')
        file_handler.write_to_file(os.path.join(temp_dir, "temp_file.txt"), data)
        file_handler.decrypt_file(os.path.join(temp_dir, "temp_file.txt"), 'statistical_caesar', 'rus')
        assert os.path.exists(result_file)
    finally:
        shutil.rmtree(temp_dir)
