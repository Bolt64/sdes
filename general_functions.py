"""
General functions to handle permutations, cyclic shifts, etc
Look for major bottlenecks here
"""

def create_keystring(key, size):
    return bin(key)[2:].zfill(size)

def permute_key(key, permutation):
    rstring=""
    for i in permutation:
        rstring+=key[i]
    return rstring

def left_shift(key, shift):
    return key[shift:]+key[:shift]
