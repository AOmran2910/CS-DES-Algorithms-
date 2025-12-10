# 1. PERMUTATION TABLES + SBOXES

IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

FP = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

P = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

S_BOXES = [
    # S1
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    ],

    # S2
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
    ],

    # S3
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
    ],

    # S4
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
    ],

    # S5
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
    ],

    # S6
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
    ],

    # S7
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
    ],

    # S8
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11],
    ]
]

# PC-1 (Key → 56 bits)
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# PC-2 (56 → 48 bits)
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

ROT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# ----------------------------------------------------------
# 2.permutation function
# ----------------------------------------------------------


def permute(bits, table):
# builds new bit string by reading specific positions 
    new = ""
    for pos in table:
        new += bits[pos-1]
    return new


# ----------------------------------------------------------
# 3. Generates all 16 DES round keys
# ----------------------------------------------------------

def make_round_keys(key64):
    # first apply PC1 to shrink key to 56 bits
    key56 = permute(key64, PC1)

    # split into left (C) and right (D) halves
    C = key56[:28]
    D = key56[28:]

    round_keys = []

    # rotate key halves for each round
    for r in ROT:
        C = C[r:] + C[:r]
        D = D[r:] + D[:r]
        round_keys.append(permute(C + D, PC2))  # PC2 → 48 bits

    return round_keys


# ----------------------------------------------------------
# 4. Feistel function f(R, K)
# ----------------------------------------------------------

def feistel(R, K):
    # Step 1: Expand R from 32 → 48 bits
    ER = permute(R, E)

    # Step 2: XOR expanded R with the round key
    x = int(ER, 2) ^ int(K, 2)
    x = f"{x:048b}"

    # Step 3: S-boxes reduce 48 → 32 bits
    out = ""
    for i in range(8):
        block = x[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        out += f"{S_BOXES[i][row][col]:04b}"

    # Step 4: Apply P-box permutation
    return permute(out, P)


# ----------------------------------------------------------
# 5. Encrypts one 64-bit block
# ----------------------------------------------------------

def des_encrypt_block(block64, key64):
    keys = make_round_keys(key64)

    # Initial Permutation
    block = permute(block64, IP)
    L = block[:32]
    R = block[32:]

    # 16 rounds
    for i in range(16):
        newL = R
        f_out = feistel(R, keys[i])
        newR = f"{int(L,2) ^ int(f_out,2):032b}"
        L, R = newL, newR

    # Final permutation after swapping
    final = permute(R + L, FP)
    return final


# ----------------------------------------------------------
# 6. Decrypts one 64-bit block (keys reversed)
# ----------------------------------------------------------

def des_decrypt_block(block64, key64):
    keys = make_round_keys(key64)[::-1]  # reverse keys

    block = permute(block64, IP)
    L = block[:32]
    R = block[32:]

    for i in range(16):
        newL = R
        f_out = feistel(R, keys[i])
        newR = f"{int(L,2) ^ int(f_out,2):032b}"
        L, R = newL, newR

    final = permute(R + L, FP)
    return final


# ----------------------------------------------------------
# 7. SIMPLE MESSAGE FUNCTIONS (Beginner-Friendly)
# ----------------------------------------------------------

# This function adds padding so the message is a multiple of 8 bytes.
# DES needs blocks that are exactly 8 bytes long.
def pad_message(message_bytes):
    padding_needed = 8 - (len(message_bytes) % 8)

    # Add padding bytes (each padding byte stores the padding size)
    padding_bytes = bytes([padding_needed]) * padding_needed
    return message_bytes + padding_bytes


# This removes the padding added before encryption.
def remove_padding(message_bytes):
    last_byte = message_bytes[-1]   # tells us how many padding bytes there are
    return message_bytes[:-last_byte]


# Encrypt a normal string using DES (block by block)
def encrypt_message(text, key_bits):

    # Convert string to bytes
    message_bytes = text.encode("utf-8")

    # Pad so length is divisible by 8
    message_bytes = pad_message(message_bytes)

    final_cipher_hex = ""

    # Process each 8-byte block one at a time
    for i in range(0, len(message_bytes), 8):
        block = message_bytes[i:i+8]       # extract 8 bytes

        # Convert the 8 bytes into a 64-bit binary string
        block_bits = ""
        for b in block:
            block_bits += f"{b:08b}"

        # Encrypt the 64-bit block using DES
        encrypted_bits = des_encrypt_block(block_bits, key_bits)

        # Convert binary → bytes → hex
        encrypted_value = int(encrypted_bits, 2)
        encrypted_block_bytes = encrypted_value.to_bytes(8, "big")
        final_cipher_hex += encrypted_block_bytes.hex()

    return final_cipher_hex



# Decrypt HEX ciphertext back into a normal string
def decrypt_message(cipher_hex, key_bits):

    cipher_bytes = bytes.fromhex(cipher_hex)
    final_plain_bytes = bytearray()

    # Go through the encrypted message 8 bytes at a time
    for i in range(0, len(cipher_bytes), 8):
        block = cipher_bytes[i:i+8]

        # Convert block to 64-bit binary
        block_bits = ""
        for b in block:
            block_bits += f"{b:08b}"

        # DES decryption
        decrypted_bits = des_decrypt_block(block_bits, key_bits)

        # Convert decrypted bits → bytes
        decrypted_value = int(decrypted_bits, 2)
        decrypted_bytes = decrypted_value.to_bytes(8, "big")

        final_plain_bytes.extend(decrypted_bytes)

    # Remove padding and turn back into text
    final_plain_bytes = remove_padding(final_plain_bytes)
    return final_plain_bytes.decode("utf-8")



# ----------------------------------------------------------
# 8. DEMO
# ----------------------------------------------------------
import random

def generate_random_key():
    # Generate a 64-bit random key as a binary string
    return ''.join(random.choice('01') for _ in range(64))

def run_demo():
    # Get message from the user
    msg = input("Enter your message: ")

    # Generate a random key
    key = generate_random_key()

    print("Input message:", msg)
    print("Key (binary):", key)
    print("Key (hex):   ", hex(int(key, 2))[2:])

    # Encrypt the message
    encrypted = encrypt_message(msg, key)

    # Decrypt the message
    decrypted = decrypt_message(encrypted, key)
    print("Decrypted message:", decrypted)

run_demo()


