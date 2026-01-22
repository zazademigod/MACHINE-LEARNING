#this is my implementation of caesar cipher for alphabets in python
text = str(input("enter the text/message to ecrypt: "))
shift_key = int(input("enter the key to shift the alphabets by: "))

def caesar(message, shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ''
    for val in message.lower():
        if val not in alpha:
            new_message += val
        #if the character is not a space, find its index in the alphabet
        else:
            #finding the index of the character in the alphabet
            index = alpha.find(val)
            new_index = (index + shift) % len(alpha)#this % is to repeat the alphabet if the shift goes beyond 'z'
            new_message += alpha[new_index]
    print('original message: ', message)
    print('caesar encrypted message: ', new_message)

caesar(text, shift_key)