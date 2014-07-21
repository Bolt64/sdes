"""
This module handles the encryption of 8-bits as a bitstring
"""

import general_functions as gf
import s_des_key_creator as keygen
import s_des_parameters as pa


def SBox(input_bitstring, s_matrix):
    row=int(input_bitstring[0]+input_bitstring[3], 2)
    column=int(input_bitstring[1:3], 2)
    return bin(s_matrix[row][column])[2:].zfill(2)

def MappingF(input_bitstring, keystring):
    expanded_bitstring=gf.permute_key(input_bitstring, pa.mp_EP)
    bitstring=bin(int(expanded_bitstring, 2)^int(keystring, 2))[2:].zfill(8)
    left_bits=bitstring[:4]
    right_bits=bitstring[4:]
    left_out=SBox(left_bits, pa.mp_matrix_s0)
    right_out=SBox(right_bits, pa.mp_matrix_s1)
    return gf.permute_key(left_out+right_out, pa.mp_P4)

def complex_function(left_bitstring, right_bitstring, keystring):
    left_bit=int(left_bitstring, 2)
    left_out=left_bit^int(MappingF(right_bitstring, keystring), 2)
    return bin(left_out)[2:].zfill(4),right_bitstring

def s_des_encrypt(bitstring, key1, key2, decrypt=False):
    if decrypt:
        key2,key1=key1,key2
    bitstring=gf.permute_key(bitstring, pa.en_IP)
    left,right=complex_function(bitstring[:4], bitstring[4:], key1)
    left,right=complex_function(right, left, key2)
    return gf.permute_key(left+right, pa.en_IP_inverse)
