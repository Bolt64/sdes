"""
This module handles the generation of 2 8-bit keys from a 10-bit key
"""

import general_functions as gf
import s_des_parameters as pa

def s_des_keygen(key):
    primary_key=gf.create_keystring(key, 10)
    primary_key=gf.permute_key(primary_key, pa.kg_P10)
    primary_key=gf.left_shift(primary_key[:5], 1) + gf.left_shift(primary_key[5:], 1)
    key1=gf.permute_key(primary_key, pa.kg_P8)
    primary_key=gf.left_shift(primary_key[:5], 2) + gf.left_shift(primary_key[5:], 2)
    key2=gf.permute_key(primary_key, pa.kg_P8)
    return key1,key2
