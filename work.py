what = str(input('what do you want? \n 1. color\n 2. clear\n 3. New file\n'))

def to_do(code):
    import os
    work = os.system
    if code == '1' or code.lower() == 'color':
        value = str(input('Put a value from 0 - 99: '))
        colour = 'color ' + value
        new_msg = work(colour)
    elif code == '2' or code.lower() == 'clear':
        new_msg = work('cls')
    elif code == '3' or code.lower() == 'new file':
        text = str(input('what do yoou want to name the file? (Add the extension)\n'))
        msg = str(input('1. Text\n2. programming language \n'))
        if msg.lower() == "text" or msg == "1":
            new_msg = work("notepad " + text)
        elif msg.lower() == 'programming language' or msg == "2":
            new_msg = work('code ' + text)
        else:
            print('Error try again!')
            to_do(what)

    else:
        new_msg = str(input('Try Again 1, 2 or 3 (pick one) \n'))
        to_do(new_msg)
    return new_msg

to_do(what)
