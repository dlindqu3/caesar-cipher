import random

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

def crack(text): 
    pass 

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