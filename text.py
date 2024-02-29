# This counts the letters in a given text
# Then it shifts that text by 111 letters ahead to encrypt the original message

init_phrase = "Hi! I'm a Software Developer"
init_shift = 111

def text(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

text(init_phrase, init_shift)