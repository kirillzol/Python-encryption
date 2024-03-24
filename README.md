# Python-encryption
## Описание проекта
"Шифрование" представляет собой проект на Python, который позволяет шифрование и дешифрование файлов припомощи различных методов и алгоритмов шифрования, а также для реализации стеганографии. Программа предоставляет возможность выбора различных режимов работы (Режим как и путь к файлу, с которым ведется работа задается с помощью аргументов командной строки) и обеспечивает защиту информации.

## Реализуемый функционал
### Несколько режимов работы:
1. Шифрование и дешифрование файлов шифрами:
  - Цезаря
  - Виженера
  - Вернама

2. Взлом шифра Цезаря с использованием методов частотного анализа.
3. Возможность работы с текстовыми и графическими файлами.
4. Стеганография:
  - Внедрение текста в изображение формата BMP, используя младшие биты каждого байта пикселя.
  - Извлечение текста из изображения формата BMP.
5. Графический интерфейс (если будет)
## Архитектура
```
├── Main.py
    └── import Cipher.py
    └── import Steganography.py
    └── import FileHandler.py
    └── def pars_arguments
    └── def main()
├── Cipher.py
    └── class CesarCipher
        └── str alfavit_EU 
        └── str alfavit_RU
        └── int step
        └── def __init__(self, alfavit, step)
        └── def encrypt(alfavit, step)
        └── def decrypt(alfavit, step)
    └── class VigenereCipher
        └── def generateKey 
        └── def __init__(self, text, keyword)
        └── def encrypt(text, keyword)
        └── def decrypt(text, keyword)
    └── class VernamCipher
        └── def generateKey
        └── def __init__(self, text, keyword)
        └── def encrypt(text, keyword)
        └── def decrypt(text, keyword)
├── Steganography.py
        └── def __init__
        └── def generate_data(self, path)
        └── def modify_pixels(pix, data)
        └── def encrypt
        └── def decrypt
├── FileHandler.py
    └── class FileHandler
        └── def __init__(self, file_path):
        └── def read_file(self)
        └── def generate_file(self, data):
        └── def encrypt_file(self, cipher):
        └── def decrypt_file(self, cipher):
├── GUI.py # файл для граф. интерфейса, если будет
├── Utils.py # вспомогательный файл, возможно не пригодится вовсе
└── README.md
```

