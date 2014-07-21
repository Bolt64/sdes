"""
A module to transparently allow manipulation of files as 8-bit blocks
"""

import struct

def get_bytes(filename):
    with open(filename, 'rb') as fileobject:
        byte=fileobject.read(1)
        while byte != b'':
            yield byte
            byte=fileobject.read(1)

def write_bytes(filename, byte_generator):
    with open(filename, 'wb') as fileobject:
        for byte in byte_generator:
            fileobject.write(byte)

def byte_to_bits(byte):
    return ord(byte)

def bits_to_byte(bits):
#   The "B" option ensure the input is packed with 8 bits
    return struct.pack("B", bits)
