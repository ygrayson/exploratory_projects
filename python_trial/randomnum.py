# Python trial program for Baidu conversational robot


import random

num = random.randomint(1, 10)
pygame.mixer.init()

#random play
if num == 1:
    pygame.mixer.music.load("start1.wav")
else if num == 2:
    pygame.mixer.music.load("start2.wav")
else if num == 3:
    pygame.mixer.music.load("start3.wav")
else if num == 4:
    pygame.mixer.music.load("start4.wav")
else if num == 5:
    pygame.mixer.music.load("start5.wav")
else if num == 6:
    pygame.mixer.music.load("start6.wav")
else if num == 7:
    pygame.mixer.music.load("start7.wav")
else if num == 8:
    pygame.mixer.music.load("start8.wav")
else if num == 9:
    pygame.mixer.music.load("start9.wav")
else if num == 10:
    pygame.mixer.music.load("start10.wav")

#play audio record
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
       continue