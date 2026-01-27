#this is my implementation of caesar cipher for alphabets in python

text = str(input("enter the text/message to work on: "))
shift_key = int(input("enter the key to shift the alphabets by: "))
to_do = int(input("what do you want to do? \n 1 encrypt \n 2 decrypt \n select "))

def caesar_encrypt(message, shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ''
    for char in message:
        is_upper = char.isupper()
        val = char.lower()
        if val not in alpha:
            new_message += val
        #if the character is not a space, find its index in the alphabet
        else:
            #finding the index of the character in the alphabet
            index = alpha.find(val)
            new_index = (index + shift) % len(alpha)#this % is to repeat the alphabet if the shift goes beyond 'z'
            new_char = alpha[new_index]
            if is_upper: #this is to maintain the case of the value
                new_message += new_char.upper()
            else:
                new_message += new_char 
    print('unencrypted message: ', message)
    print('caesar encrypted message: ', new_message)

def caesar_decrypt(message, shift):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    decrypted_msg = ""
    for char in message:
        is_upper = char.isupper()
        val = char.lower()
        if val not in alpha:
            decrypted_msg += val
        else:
            index = alpha.find(val)
            new_index = (index - shift) % len(alpha)
            new_char = alpha[new_index]
            if is_upper:
                decrypted_msg += new_char.upper()
            else:
                decrypted_msg += new_char
    print("encrypted message: ", message)
    print("decrypted message: ", decrypted_msg)

if to_do == 1:
    caesar_encrypt(text, shift_key)
elif to_do == 2:
    caesar_decrypt(text, shift_key)
else:
    print("invalid input, Select 1 or 2")
    to_do