from src.FileHandler import *
from src.CesarStatisticsDecipher import *
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Encryption and decryption program')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt data')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt data')
    parser.add_argument('-a', '--algorithm', choices=['caesar', 'vernam', 'vigenere', 'statistical_caesar'],
                        help='Encryption/Decryption algorithm')
    parser.add_argument('-i', '--input_file', help='Input file')
    parser.add_argument('-l', '--lang', choices=['rus', 'eng'], help='Language')
    parser.add_argument('-k', '--key', default='', help='shift for cesar / key for vernam or vigenere / nothing for '
                                                        'statistical_caesar')
    return parser.parse_args()


def main():
    args = parse_arguments()
    file_handler = FileHandler()
    if args.encrypt:
        file_handler.encrypt_file(args.input_file, args.algorithm, args.lang, args.key)
    elif args.decrypt:
        file_handler.decrypt_file(args.input_file, args.algorithm, args.lang, args.key)
    else:
        print('Please specify whether you want to encrypt (-e) or decrypt (-d) the data.')


if __name__ == "__main__":
    main()
