from statistics import *

plaintext =  "EASTNORTHEASTBERLINCLOCK"
ciphertext = "FLRVQQPRNGKSSNYPVTTMZFPK"

diffs = []
for i in range(len(ciphertext)):
    c = ord(ciphertext[i])
    p = ord(plaintext[i])

    diff = abs(c - p)
    diffs.append(diff)

    print(diff)

print(mean(diffs))
print(stdev(diffs))