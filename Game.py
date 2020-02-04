import pygame
from Setups import *
from Jugador import *
from Levels import *
from Menu import *
from Maps import *

pygame.init()

def main():

    clock = pygame.time.Clock()
           
    world_width = 900                      #ancho de la pantalla
    world_height = 506                      #altura de la pantalla
    FPS = 60                               #frames por segundo

    title = "Can you Jump?"                                         #coloco el titulo de la pantalla
    url = "./Runner_Game/Images/stage.jpg"

    #creo el screen del juego con unas especificaciones
    Game_Jumping = New_Game(world_width,world_height,FPS,title,url)

    #main loop
    while Game_Jumping.Run:

        last_Mousepos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Jumping.Run = False

            if Game_Jumping.Controlador_Interfaz.Active_screen == "Game":
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE: Game_Jumping.Player.jumping()

                    if event.key == pygame.K_j:
                        Game_Jumping.Player.acpm = 5
                        Game_Jumping.Player.jecktpack = True

                    if event.key == pygame.K_ESCAPE:
                        Game_Jumping.Controlador_Interfaz.Active_screen = Game_Jumping.Controlador_Interfaz.Menus["Pause"]

            else:
                if last_Mousepos[0] - pygame.mouse.get_pos()[0] != 0 or event.type == pygame.MOUSEBUTTONDOWN:
                    Game_Jumping.Controlador_Interfaz.Mouse_Controller(pygame.mouse.get_pos(),event)
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    Game_Jumping.Controlador_Interfaz.Keyboard_Controller(event)

        if Game_Jumping.Controlador_Interfaz.Active_screen == "Game":
            Game_Jumping.Player.update()
        else:
            Game_Jumping.Controlador_Interfaz.Display()

        pygame.display.update()
                    
        clock.tick(FPS)

main()

#To do

#modificar el sistema de url para las imagenes

#revisar la logica de los botones y controlador de eventos en los menu, no me sigue gustando

#pensar en que elementos del store comprar

#reparar las imagenes o buscar otros background

#revisar la imagen del candado por que al redimensionarla queda horrible :v

#buscar musica para el fondo
