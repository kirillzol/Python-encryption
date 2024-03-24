# Python-encryption
## Описание проекта

"Шифрование" представляет собой проект на Python, который позволяет проводить шифрование и дешифрование файлов с использованием различных методов и алгоритмов шифрования, а также реализовывать стеганографию. Программа предоставляет возможность выбора различных режимов работы (режимы и пути к файлам задаются с помощью аргументов командной строки) и обеспечивает защиту информации.

## Реализуемый функционал
### Несколько режимов работы:

1. Шифрование и дешифрование файлов шифрами:
  - Цезаря - метод шифрования, при котором каждая буква в открытом тексте заменяется буквой, находящейся на некотором постоянном числе позиций левее или правее неё в алфавите.
  - Виженера - шифр использует ключевое слово и таблицу, известную как табличка Виженера, для шифрования и дешифрования текста. Каждая буква ключевого слова соответствует определенному числу, и эти числа используются для сдвига символов открытого текста в соответствующих позициях.
  - Вернама - криптографический алгоритм, который использует одноразовый блокнот для шифрования и дешифрования сообщений. Он предполагает использование ключа той же длины, что и сообщение, и этот ключ используется только один раз.

2. Взлом шифра Цезаря с использованием методов частотного анализа - этот метод основан на на анализе частоты появления символов в зашифрованном тексте. Для декодирования текста этим методом надо проанализировать частоту вхождения каждой буквы в зашифрованном тексте, после чего сравнить со статистическими показателями языка. Далее найти оптимальный сдвиг и декодировать текст. Этот метод работает эффективно только в случае, если зашифрованный текст достаточно длинный и если частота встречаемости символов в тексте приблизительно соответствует частотам символов в языке сообщения.

3. Возможность работы с текстовыми и графическими файлами.

4. Стеганография:
  - Внедрение текста в изображение формата BMP, используя младшие биты каждого байта пикселя.
  - Извлечение текста из изображения формата BMP.

## Архитектура

- Main.py - Файл Main.py содержит главный модуль программы, который отвечает за обработку аргументов командной строки и запуск нужных функций в зависимости от выбранного режима работы. pars_argument - функция для парсинга аргументов командной строки, main() - запускает программу исходя из аргументов командной строки.

- Cipher.py - содержит в себе 3 класса, внутри которых реализуются 3 основных алгоритма проекта. Класс для алгоритма Цезаря: имееет 2 атрибута - русский и английски алфавиты, а также функции кодирования и декодирования текстового файла по алфавиту и сдвигу. Класс для шифра Виженера - имеет функцию генерации ключа: она генерирует ключ циклически, пока его длина не станет равна длине исходного текста, а также функции кодирования и декодирования текстового файла по ключу. И наконец класс для шифра Вернама: функция генерации ключа: Создается случайная последовательность битов, которая должна быть такой же длины, как и текст, а также функции кодирования и декодирования текстового файла по ключу.

- CesarStatisticsDecipher.py - файл, в котором содержится класс CesarStatisticsDecipher - имеет атрибуты: русский и английски алфавиты, а так же статистические данные по каждому из языков. Метод collect_statistics_from_text возвращает статистические данные по тексту. find_opt_step находит статистически оптимальный сдвиг, сопоставляя данные по тексту и по языку. После чего вызывается decrypt из CesarCipher.

- Steganography.py - содержит класс Steganography: generate_data - преобразует данные в бинарный формат (8-битный ASCII код каждого символа) и возвращает список бинарных кодов. modify_pixels  - модифицирует пиксели изображения в соответствии с бинарными данными. Каждый бит данных встраивается в младший бит каждого компонента цвета RGB. encrypt - кодирует изображение. Она принимает объект изображения и данные, которые нужно внедрить. Затем она вызывает функцию modPix для модификации пикселей изображения. decrypt() - Функция для декодирования данных из изображения.

- FileHandler.py содержит класс FileHandler, который отвечает за обработку файлов в проекте: read_file, generate_file - для чтения и записи файлов. Также этот класс содержит методы для обработки файлов, используемых в процессе шифрования и дешифрования: encrypt_file, decrypt_file.

### Визуализация архитектуры
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
        └── def __init__(self, text, alfavit, step)
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
├── CesarStatisticsDecipher.py
    └── CesarStatisticsDecipher
        └── str alfavit_EU 
        └── str alfavit_RU
        └── statistics_data_eng
        └── statistics_data_ru
        └── def __init__(self, text)
        └── def collect_statistics_from_text(text)
        └── def find_opt_step(text, alfavit, statistics_data_text, statistics_data_lang)
├── Steganography.py
    └── class Steganography
        └── def __init__(self, path)
        └── def generate_data(path)
        └── def modify_pixels(pix, data)
        └── def encrypt(img, data)
        └── def decrypt()
├── FileHandler.py
    └── class FileHandler
        └── def __init__(self, file_path):
        └── def read_file(self)
        └── def generate_file(self, data)
        └── def encrypt_file(self, cipher)
        └── def decrypt_file(self, cipher)
├── Utils.py # вспомогательный файл, возможно не пригодится вовсе
└── README.md
```
## Стек технологий и используемые библиотеки

### Стек технологий: 
Python: Основной язык программирования для разработки проекта.
### Используемые библиотеки:
- PIL (Python Imaging Library): Используется для работы с изображениями, включая извлечение пикселей, модификацию изображений и сохранение изображений.
- argparse: Используется для обработки аргументов командной строки.
- os: Используется для взаимодействия с операционной системой, включая создание директорий и работы с файлами.
- math: Используется для выполнения математических операций, например, для вычисления ключей шифрования и дешифрования.
- random: Используется для генерации случайных чисел, которые могут использоваться в алгоритмах шифрования.

