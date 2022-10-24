try:
    import pyperclip  
except ImportError:
    pass  
 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    while True: 
        print('Do you want to (e)ncrypt or (d)ecrypt?') 
        response = input('> ').lower()
        
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt' 
            break
        print('Please enter the letter e or d.')
        
    while True:  
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').upper()
        
        if response.isalpha():
            myKey = response
            break
        
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')
    
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)
        
    print('%sed message:' % (myMode.title()))
    print(translated)
    
    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  
 
def encryptMessage(message, key):
    return translateMessage(message, key, 'encrypt')
 
 
def decryptMessage(message, key):
    return translateMessage(message, key, 'decrypt')
 
def translateMessage(message, key, mode):
    translated = []  
    keyIndex = 0
    key = key.upper()
      
    for symbol in message: 
        num = LETTERS.find(symbol.upper())
        if num != -1: 
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
            
            num %= len(LETTERS)  
            
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            
            keyIndex += 1  
            
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)


if __name__ == '__main__':
    main()