from statistics import *

kryptos_vigenere_table = """
KRYPTOSABCDEFGHIJLMNQUVWXZKRYP
RYPTOSABCDEFGHIJLMNQUVWXZKRYPT
YPTOSABCDEFGHIJLMNQUVWXZKRYPTO
PTOSABCDEFGHIJLMNQUVWXZKRYPTOS
TOSABCDEFGHIJLMNQUVWXZKRYPTOSA
OSABCDEFGHIJLMNQUVWXZKRYPTOSAB
SABCDEFGHIJLMNQUVWXZKRYPTOSABC
ABCDEFGHIJLMNQUVWXZKRYPTOSABCD
BCDEFGHIJLMNQUVWXZKRYPTOSABCDE
CDEFGHIJLMNQUVWXZKRYPTOSABCDEF
DEFGHIJLMNQUVWXZKRYPTOSABCDEFG
EFGHIJLMNQUVWXZKRYPTOSABCDEFGH
FGHIJLMNQUVWXZKRYPTOSABCDEFGHI
GHIJLMNQUVWXZKRYPTOSABCDEFGHIJL
HIJLMNQUVWXZKRYPTOSABCDEFGHIJL
IJLMNQUVWXZKRYPTOSABCDEFGHIJLM
JLMNQUVWXZKRYPTOSABCDEFGHIJLMN
LMNQUVWXZKRYPTOSABCDEFGHIJLMNQ
MNQUVWXZKRYPTOSABCDEFGHIJLMNQU
NQUVWXZKRYPTOSABCDEFGHIJLMNQUV
QUVWXZKRYPTOSABCDEFGHIJLMNQUVW
UVWXZKRYPTOSABCDEFGHIJLMNQUVWX
VWXZKRYPTOSABCDEFGHIJLMNQUVWXZ
WXZKRYPTOSABCDEFGHIJLMNQUVWXZK
XZKRYPTOSABCDEFGHIJLMNQUVWXZKR
ZKRYPTOSABCDEFGHIJLMNQUVWXZKRY
"""

kryptos_alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
kryptos_vigenere_alphabets = kryptos_vigenere_table.split()
kryptos_alphabet_diffs = []

print("KRYPTOS VIGENERE ALPHABET DIFFS: ")

for r in range(len(kryptos_alphabet)):
    for c in range(len(kryptos_alphabet)):
        plaintext_char = ord(kryptos_alphabet[c])
        ciphertext_char = ord(kryptos_vigenere_alphabets[r][c])

        diff = abs(plaintext_char - ciphertext_char)
        kryptos_alphabet_diffs.append(diff)

print("Count = ", len(kryptos_alphabet_diffs))
print("Mode = ", mode(kryptos_alphabet_diffs))
print("Mean = ", mean(kryptos_alphabet_diffs))
print("Std Dev = ", stdev(kryptos_alphabet_diffs))
