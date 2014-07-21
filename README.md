sdes
====

Simplified Data Encryption Standard
====

This is a python implementation of the Simplified Data Encryption Standard
(S-DES) based on the book "Cryptography and Network Security 2nd Edition" by
William Stallings. 
This implementation is merely a prototype and shouldn't be actually used to
encrypt anything important because:
    
    1. The key is only 10-bit, which brute force a very easy.
    2. The python implementation is slow as molasses, taking up to 2 minutes to
       encrypt a 5 mb file on a Core i3, and up to 46 minutes to do the same on
       a Raspberry Pi.

Usage:
    
    1. Encryption: ./file_encryptor -e plaintext ciphertext key(0-1023)
    2. Decryption: ./file_encryptor -d ciphertext plaintext key(0-1023)
