from FileHandler import *
import argparse

# file = "/Users/macbook/Desktop/Test.txt"
# File_Handler = FileHandler()
#
# File_Handler.decrypt_file(file, "statistical_caesar")
# # File_Handler.encrypt_file(file, "cesar")



def parse_arguments():
    parser = argparse.ArgumentParser(description='Encryption and decryption program')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt data')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt data')
    parser.add_argument('-a', '--algorithm', choices=['caesar', 'vernam', 'vigenere', 'statistical_caesar'],
                        help='Encryption/Decryption algorithm')
    parser.add_argument('-i', '--input_file', help='Input file')
    return parser.parse_args()


def main():
    args = parse_arguments()
    file_handler = FileHandler()
    if args.encrypt:
        file_handler.encrypt_file(args.input_file, args.algorithm)
    elif args.decrypt:
        file_handler.decrypt_file(args.input_file, args.algorithm)
    else:
        print('Please specify whether you want to encrypt (-e) or decrypt (-d) the data.')


if __name__ == "__main__":
    main()
