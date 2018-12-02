
# ## Caeser Cipher
# 1. Define the alphabet map. We need to map a-z to 0-25.

from pprint import pprint

ch_map = {}
for counter in range(0,26):
    ch = chr(counter+65)
    ch_map[ch]=counter
pprint(ch_map)


# #### 1.2 Encrytion Algorithm
# 1. $p$: the original position which provided by char_map of a given character.
# 2. $k$: number of shifts from the original position.
# 3. $C$: encrypted char 
# 
#    $C= E(k,p) = (p + k)\ mod \ 26$

def caeser(p,k=3):
    c = (p-k)%26
    return c


def wrapper(plain_text):
    ciphertext  = ''
    for letter in plain_text:
        p = ch_map[letter]
        c=caeser(p)
        cipher_letter=chr(c+97)
        ciphertext = ciphertext+cipher_letter
    return ciphertext
c1=wrapper('ZHDUHVHFXULWBHASHUWV')
print(c1)

