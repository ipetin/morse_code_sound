# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:36:56 2022

@author: ipetin
"""

import pygame
import time
import numpy

sampleRate = 44100
freq = 530


MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

TIME_BETWEEN = 0.1

def play_sound(line=True):
    arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
    arr2 = numpy.c_[arr,arr]
    sound = pygame.sndarray.make_sound(arr2)
    sound.play(-1)
    if line: 
        pygame.time.delay(300)
    else:
        pygame.time.delay(100)

    sound.stop()

    
def verify(string):
    keys = list(MORSE.keys())
    for char in string:
        if char not in keys and char != " ":
            print(f"The character {char} cannot be translated.")
            raise SystemExit


def main():
    while True:
        print("\nEnter message: ")
        message = input("> ").upper()
        verify(message)
        pygame.init()
        message_morse = []
        for char in message:
            if char == " ":
                print(" " * 3, end=" ")
                time.sleep(7 * TIME_BETWEEN)
            else:
                message_morse.append(MORSE[char])
        for morse in message_morse:
            print(morse, end=" ")
            for c in morse:
                if c == ".":
                    play_sound(False)
                else:
                    play_sound(True)
                    
            time.sleep(4 * TIME_BETWEEN)


if __name__ == "__main__":
    main()