from statistics import *

ciphertext = "FLRVQQPRNGKSSNYPVTTMZFPK"
plaintext =  "EASTNORTHEASTBERLINCLOCK"

diffs = []
for i in range(len(ciphertext)):
    c = ord(ciphertext[i])
    p = ord(plaintext[i])

    diff = abs(c - p)
    diffs.append(diff)

    print(diff)

print(mean(diffs))
print(stdev(diffs))
