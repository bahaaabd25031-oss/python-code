def ceasar_encryption(og_sentance : str) -> str: 
    encrypted_sentance = []
    for letter in og_sentance:
        if (letter.isalpha()):
            new_letter = chr(ord(letter) + 3)
            encrypted_sentance.append(new_letter)
            continue
        encrypted_sentance.append(letter)
    return ''.join(encrypted_sentance)

def ceasar_decryption(encrypted_sentance : str) -> str: 
    decrypted_sentance = []
    for letter in encrypted_sentance:
        if (letter.isalpha()):
            new_letter = chr(ord(letter) - 3)
            decrypted_sentance.append(new_letter)
            continue
        decrypted_sentance.append(letter)
    return ''.join(decrypted_sentance)

og_sentance = input('enter a sentance to encrypt: ')

s = ceasar_encryption(og_sentance)
print('the encryoted sentance is: ',s)

ds = ceasar_decryption(s)
print('the decrypted senatnce is: ',ds)