from time import localtime
import pygame

Hour = input ("Ingresar la hora en formato 24H ==> ")
Minute = input ("Ingresar los minutos de la hora ==>")
pygame.mixer.init()
if int(Hour) < 24:
    if int(Minute) <60:
        while True:
            if localtime().tm_hour == int (Hour) and localtime().tm_min == int (Minute):
              pygame.mixer.music.load('sonido.mp3')
              pygame.mixer.music.play()
              print('sonido de alarma')  
              while pygame.mixer.music.get_busy():
                  continue 
              break                 
    else:
        print('minuto no valido')
else:
    print('Hora no valida')
