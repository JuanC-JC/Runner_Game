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

            if Game_Jumping.Active_screen == "Game":

                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE: Game_Jumping.Player.jumping()

                    if event.key == pygame.K_j:
                        Game_Jumping.Player.acpm = 5
                        Game_Jumping.Player.jecktpack = True

                    if event.key == pygame.K_ESCAPE:
                        Game_Jumping.Active_screen = "Stop_Menu"
            
            elif Game_Jumping.Active_screen == "Main_Menu":
                if last_Mousepos[0] - pygame.mouse.get_pos()[0] != 0:
                    Game_Jumping.Main_Menu.Mouse_Controller(pygame.mouse.get_pos())
                else:
                    Game_Jumping.Main_Menu.Events_Controller(event)

            elif Game_Jumping.Active_screen == "Stop_Menu":
                if last_Mousepos[0] - pygame.mouse.get_pos()[0] != 0:
                    Game_Jumping.Pause_Menu.Mouse_Controller(pygame.mouse.get_pos())
                else:
                    Game_Jumping.Pause_Menu.Events_Controller(event)

            elif Game_Jumping.Active_screen =="Lvls_Menu":
                if last_Mousepos[0] - pygame.mouse.get_pos()[0] != 0:
                    Game_Jumping.Levels_Menu.Mouse_Controller(pygame.mouse.get_pos())
                else:
                    Game_Jumping.Levels_Menu.Events_Controller(event)

        if Game_Jumping.Active_screen == "Main_Menu":
            Game_Jumping.Main_Menu.display()
            
        elif Game_Jumping.Active_screen =="Stop_Menu":
            Game_Jumping.Player.lvl.Update()
            Game_Jumping.Pause_Menu.display()

        elif Game_Jumping.Active_screen == "Lvls_Menu":
            Game_Jumping.Levels_Menu.Display()
            
        elif Game_Jumping.Active_screen == "Game":
            Game_Jumping.Player.update()
 
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
