from statistics import *

k4_plaintext =  "EASTNORTHEASTBERLINCLOCK"
k4_ciphertext = "FLRVQQPRNGKSSNYPVTTMZFPK"

print("K4 CIPHERTEXT TO KNOWN PLAINTEXT DIFFS: ")

diffs = []
for i in range(len(k4_ciphertext)):
    ciphertext_char = ord(k4_ciphertext[i])
    plaintext_char = ord(k4_plaintext[i])

    diff = abs(ciphertext_char - plaintext_char)
    diffs.append(diff)

print("Count = ", len(diffs))
print("Mode = ", mode(diffs))
print("Mean = ", mean(diffs))
print("Std Dev = ", stdev(diffs))
