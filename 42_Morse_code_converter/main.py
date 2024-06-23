import pygame
import time 

#Initializing pygame object
pygame.init()
pygame.mixer.init() 
sound = pygame.mixer.Sound("beep.mp3")

#Mapping letters to morse codes
morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
}

#Uppercasing
user_text = input("Enter Text: ").upper()

#Print Morse code representation of each character
print("Morse Code: ", end="")
for char in user_text:
    print(morse_code.get(char) or char, end=" ")  

#Default frequency
frequency = 1000

#Iterate through Morse code dictionary and play corresponding sounds
for symbol_set in morse_code.values():
    for symbol in symbol_set:
        if symbol == '.':
            sound.play(frequency, 100) #Shortbeep:)
        elif symbol == '-':
            sound.play(frequency, 700)  #Longbeep:D
    print('\n')  
    time.sleep(0.2) #Nobeep:(
