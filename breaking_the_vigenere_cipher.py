from collections import Counter

def get_keyword(ciphertext, key_len):
   
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    COMMON_INDEX = [ ALPHABET.index(l) for l in 'ETAONRIS'] 
      
    def get_bestfit_letter(key_indx):
        cipher_letter_count = Counter(ciphertext[key_indx::key_len]) 
        score, letter = 0, 'A'
        for j,L in enumerate(ALPHABET):
            s = sum(cipher_letter_count[ALPHABET[(indx + j)%26]] for indx in COMMON_INDEX)
            if  s > score: score, letter = s, L
        return letter

    return ''.join( get_bestfit_letter(i) for i in range(key_len))
