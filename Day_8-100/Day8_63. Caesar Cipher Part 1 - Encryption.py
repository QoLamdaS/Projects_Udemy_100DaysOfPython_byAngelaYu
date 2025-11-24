import string

lower_alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, cipher_direction):
    end_text = ""
    