import time

Morse = {'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-', '\'':'.----.', '!':'-.-.--', ',':'--..--'}

def findletter(s):
    M = list(Morse.items())
    i = 0
    while(i <= len(M) and M[i][1] != s):
        i += 1
    return M[i][0]

def findLenLetter(code):
    i = 0
    while(i < len(code) and code[i+1] != ' '):
        i += 1
    return i + 1

def translateFromMorse(code):
    i = 0
    code += ' '
    S = ""
    while(i < len(code) - 1):
        if i < len(code) - 2:
            if code[i] == ' ' and code[i+1] == ' ':
                S += ' '
                i += 2
            elif code[i] == ' ' and code[i+1] != ' ':
                i += 1
            else:
                letterLen = findLenLetter(code[i:])
                letter = findletter(code[i:i+letterLen])
                S += letter
                i += letterLen
        else:
            letter = findletter(code[i:])
            S += letter
            break
    return S

def findLetterCode(charOriginal):
    char = charOriginal.capitalize()
    M = list(Morse.items())
    i = 0
    while(i < len(M) and M[i][0] != char):
        i += 1
    letterCode = M[i][1]
    return letterCode

def translateToMorse(phrase):
    i = 0
    S = ""
    while(i < len(phrase)):
        if phrase[i] != ' ':
            letterCode = findLetterCode(phrase[i])
            S += letterCode
            if i != len(phrase) - 1:
                S += ' '
        else:
            S += "  "
        i += 1
    return S

def start():
    while(True):
        print("What do you which to do? (1: International Morse Code -> Alphabet, 2: Alphabet -> International Morse Code)")
        choice = int(input())
        if choice == 1:
            print("Internal Morse Code -> Alphabet:")
            phrase = input()
            print(translateFromMorse(phrase))
        elif choice == 2:
            print("Alphabet -> Internal Morse Code:")
            phrase = input()
            print(translateToMorse(phrase))
        else:
            print("Error: Try again.")
            startSoftware()
        time.sleep(3)
        print("\nTo end, press x. Any other key keeps the program running.")
        end = input() == 'x'
        if end: break
    print("Program ended")
