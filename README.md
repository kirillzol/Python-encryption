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

- CesarStatisticsDecipher.py - файл, в котором содержится класс CesarStatisticsDecipher - имеет атрибуты: русский и английски алфавиты, а так же статистические данные по каждому из языков. Метод collect_statistics_from_text возвращает статистические данные по тексту. find_opt_step находит статистически оптимальный сдвиг при помощи , сопоставляя данные по тексту и по языку. После чего вызывается decrypt из CesarCipher.

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
├── FileHandler.py
    └── class FileHandler
        └── def __init__(self, file_path):
        └── def read_file(self)
        └── def generate_file(self, data)
        └── def encrypt_file(self, cipher)
        └── def decrypt_file(self, cipher)
└── README.md
```
## Стек технологий и используемые библиотеки
### Стек технологий: 
Python: Основной язык программирования для разработки проекта.
### Используемые библиотеки:
- argparse: Используется для обработки аргументов командной строки.
- os: Используется для взаимодействия с операционной системой, включая создание директорий и работы с файлами.
- math: Используется для выполнения математических операций, например, для вычисления ключей шифрования и дешифрования.
- random: Используется для генерации случайных чисел, которые могут использоваться в алгоритмах шифрования.

## Тестирование 
<img width="443" alt="Снимок экрана 2024-04-17 в 23 07 30" src="https://github.com/kirillzol/Python-encryption/assets/97293695/19001d5e-4ff1-4d2a-9b8f-f001db88a6c4">

## Инструкция по запуску
### Установка зависимостей:
Убедитесь, что у вас установлен Python версии 3.x.
```
pip install -r requirements.txt
```
### Запуск программы:
Программа предоставляет возможность шифрования и дешифрования файлов с использованием различных алгоритмов.
```
python main.py -e -a caesar -i input.txt -l eng -k 3
```
Для шифрования файла input.txt с использованием алгоритма Цезаря на английском языке с ключом сдвига равным 3.
```
python main.py -d -a vernam -i encrypted.txt -l rus -k secret_key
```
Для дешифрования файла encrypted.txt с использованием алгоритма Вернама на русском языке с секретным ключом secret_key.

### Опции командной строки:
- -e, --encrypt: Запуск программы в режиме шифрования.
- -d, --decrypt: Запуск программы в режиме дешифрования.
- -a, --algorithm: Выбор алгоритма шифрования/дешифрования (caesar, vernam, vigenere, statistical_caesar).
- -i, --input_file: Путь к входному файлу.
- -l, --lang: Язык текста (rus, eng).
- -k, --key: Ключ для шифрования/дешифрования (сдвиг для Цезаря, ключ для Вернама или Виженера).

Примеры:

Шифрование файла на английском языке с использованием алгоритма Виженера и ключа password123:
```
python main.py -e -a vigenere -i input.txt -l eng -k password123
```
Дешифрование файла на русском языке с использованием алгоритма Цезаря и сдвига 5:
```
python main.py -d -a caesar -i encrypted.txt -l rus -k 5
```

Обратите внимание:
Перед запуском убедитесь, что у вас есть необходимые файлы для входных данных и выбраны правильные параметры для шифрования/дешифрования.
В случае использования алгоритма statistical_caesar ключ не требуется.