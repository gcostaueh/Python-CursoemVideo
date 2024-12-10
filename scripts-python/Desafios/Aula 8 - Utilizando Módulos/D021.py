# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Não consegui fazer esse programa, vou usar a resposta do Guanabara na correção:

import pygame
pygame.init()
pygame.mixer.music.load('D021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
