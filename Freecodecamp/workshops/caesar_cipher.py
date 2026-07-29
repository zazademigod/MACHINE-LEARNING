purpose = int(input('What do you want to do? 1. Encrypt or 2. Decrypt(1 or 2)'))
text = input('What text do you want to work on?')
shift = int(input('what is the shift key?'))

def caesar(text, shift, encrypt = True):
    if not isinstance(shift, int):
        return 'Shift should be a number'
    if shift < 1 or shift > 25:
        return 'shift should be between 1 and 25'
    if not encrypt:
        shift = -shift
    alphabet ='abcdefghijklmnopqrsuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text
def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)
if purpose == 1:
    encryption = encrypt(text, shift)
    print(encryption)
if purpose == 2:
    encryption = decrypt(text, shift)
    print(encryption)