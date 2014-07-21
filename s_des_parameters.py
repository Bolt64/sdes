"""
The parameters for the S-DES algorithm as found William Stalling's
 'Cryptography and Network Security 2nd Edition'.
"""

# Key generation parameters
kg_P10=(2, 4, 1, 6, 3, 9, 0, 8, 7, 5)
kg_P8=(5, 2, 6, 3, 7, 4, 9, 8)

# Encryption parameters
en_IP=(1, 5, 2, 0, 3, 7, 4, 6)
en_IP_inverse=(3, 0, 2, 4, 6, 1, 7, 5)

# Mapping parameters
mp_EP=(3, 0, 1, 2, 1, 2, 3, 0)

mp_matrix_s0=[
               [1, 0, 3, 2],
               [3, 2, 1, 0],
               [0, 2, 1, 3],
               [3, 1, 3, 2]
             ]

mp_matrix_s1=[
               [0, 1, 2, 3],
               [2, 0, 1, 3],
               [3, 0, 1, 0],
               [2, 1, 0, 3]
             ]

mp_P4=(1, 3, 2, 0)

