print('Tocando um MP3')

'''import pygame
pygame.init()
pygame.mixer.music.load('trigun.MP3')
pygame.mixer.music.play()
pygame.event.wait()'''

print()
from pygame import mixer
mixer.init()
mixer.music.load('trigun.MP3')
mixer.music.play()
input('Agora você escuta? ')
print()

#A primeira versão, ensinada na aula do exercício 021, não funciona. A versão abaixo (ou acima), sim.
 