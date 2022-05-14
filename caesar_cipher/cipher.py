from email import message
import random
import re 
from caesar_cipher.is_english_word import count_words
from caesar_cipher.corpus_loader import word_list

letters ='abcdefghijklmnopqrstuvwxyz'
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, key):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            initial_index = upper_letters.index(char)
            shifted_index = (initial_index + key) % 26 
            shifted_letter = upper_letters[shifted_index]
            encrypted_text += shifted_letter
        elif char.islower(): 
            initial_index = letters.index(char)
            shifted_index = (initial_index + key) % 26 
            shifted_letter = letters[shifted_index]
            encrypted_text += shifted_letter
        else: 
            encrypted_text += char 

    return encrypted_text


def decrypt(text, key):
    return encrypt(text, -key)

#take encrypted  message and return it to original state without the key 
def crack(text): 
    pattern = r'[^a-zA-Z]+' 
    #length of alphabet 
    for num in range(1, 26): 
        current_str = decrypt(text, num)
        current_words = current_str.split()
        english_words = 0
        for word in current_words: 
            #regex that grabs only the letters 
            current_word = re.sub(pattern, "", word)
            #word list from corpus
            if current_word.lower() in word_list: 
                english_words += 1 
        if english_words // len(current_words) >= .5:
            return current_str
    return ""


if __name__ == "__main__":
    pins = [
        # "abc",
        "xyz",
        # "bill",
        # "hello world",
    ]

    for pin in pins:
        key = random.randint(1, 9)
        print("plain pin", pin)
        encrypted_pin = encrypt(pin, key)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, key)
        print("decrypted_pin", decrypted_pin)