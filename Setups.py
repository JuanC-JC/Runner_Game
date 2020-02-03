import pygame
from Menu import *
from Jugador import *
from Levels import *
from Maps import  *

#setup
pygame.init()

class New_Game():
        def __init__(self,width,height,FPS,Title,Image_Bg):

                self.width = width
                self.height = height
                self.fps = FPS
                self.title = Title
                self.window = pygame.display.set_mode((self.width,self.height))
                pygame.display.set_caption(self.title)  

                image = pygame.image.load(Image_Bg).convert()
                self.Background = pygame.transform.scale(image,(self.width,self.height)).convert()
                self.Background_rect = self.Background.get_rect()

                self.Screens= {}
                self.Run = True

                #crear los menus
                self.Main_Menu = Main_Menu(self,"./Runner_Game/Images/Background_Menu.png")
                self.Pause_Menu = Pause_Menu(self)
                self.Levels_Menu = Levels_Menu(self,"./Runner_Game/Images/stage.jpg")
                
                self.Active_screen = "Main_Menu"

                #Creo el jugador, el parametro self hace referencia al mismo objeto "New_Game" que estoy creando en este init
                self.Player = Player(self,x=200)

                #creo los niveles y añado el nivel inicial
                self.Levels = []
                self.Levels.append(level(Map_1,self.width+6450,self.height,self,"./Runner_Game/Images/stage.jpg","Nivel_1",(50,50)))
                self.Levels.append(level(Map_2,self.width+4000,self.height,self,"./Runner_Game/Images/Background_Lvl.png","Nivel_2",(325,50)))
                self.Levels.append(level(Map_3,self.width+4000,self.height,self,"./Runner_Game/Images/Locked2.png","Nivel_3",(600,50)))
                self.Levels.append(level(Map_3,self.width+4000,self.height,self,"./Runner_Game/Images/Background_Lvl.png","Nivel_4",(50,50+175+10)))
                
                self.Levels_Menu.Actually_Press = self.Levels_Menu.buttons[1]
                
                #siempre dejo desbloqueado solo el primer nivel
                self.Levels[0].locked = False
                