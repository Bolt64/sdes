#!/usr/bin/env python3

import s_des_encryption_tools as sdes
import bit_manipulator as bt
import s_des_key_creator as keygen

def encryptor(src, key, decrypt=False):
    """
    This generates encrypted bytes from the plaintext source file
    """
    assert 0<=key<1023, "key must be a 10 bit binary"
    key1,key2=keygen.s_des_keygen(key)
    for byte in bt.get_bytes(src):
        bitstring=bin(bt.byte_to_bits(byte))[2:].zfill(8)
        cipher_bitstring=sdes.s_des_encrypt(bitstring, key1, key2, decrypt)
        cipher_bit=int(cipher_bitstring, 2)
        yield bt.bits_to_byte(cipher_bit)

def encrypt_file(src, dest, key, decrypt):
    """
    This writes the byte string to a destination file
    """
    bt.write_bytes(dest, encryptor(src, key, decrypt))

if __name__=="__main__":
    from sys import argv
    try:
        src=argv[2]
        dest=argv[3]
        key=int(argv[4])
        decrypt=bool(argv[1]=="-d")
        if decrypt:
            encrypt_file(src, dest, key, decrypt=True)
        else:
            encrypt_file(src, dest, key, decrypt=False)
    except IndexError:
        print("Usage: ./file_encryptor <-e|-d> plaintext ciphertext key(0-1023)")
