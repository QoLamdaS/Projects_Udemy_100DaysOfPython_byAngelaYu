import string

lower_alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode":
        for char in original_text:
            if char in lower_alphabet:
                position = lower_alphabet.index(char)
                new_position = (position + shift_amount) % 26
                end_text += lower_alphabet[new_position]
            else:
                end_text += char
    elif cipher_direction == "decode":
        for char in original_text:
            if char in lower_alphabet:
                position = lower_alphabet.index(char)
                new_position = (position - shift_amount) % 26
                end_text += lower_alphabet[new_position]
            else:
                end_text += char
    return end_text

result = caesar(original_text=text, shift_amount=shift, cipher_direction=direction)
print(f"The {direction}d text is: {result}")