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
                self.Controlador_Interfaz = Controlador_Interfaz(self)

                #crear los menus
                self.Main_Menu = Main_Menu(self,"./Runner_Game/Images/Background_Menu.png","Main")
                self.Pause_Menu = Pause_Menu(self,"Pause")
                self.Levels_Menu = Levels_Menu(self,"./Runner_Game/Images/stage.jpg","Levels")
        
                #Agregar los controladores 
                self.Controlador_Interfaz.Add_Menu(self.Main_Menu)
                self.Controlador_Interfaz.Add_Menu(self.Pause_Menu)
                self.Controlador_Interfaz.Add_Menu(self.Levels_Menu)
                
                #activar main como pantalla activo
                self.Controlador_Interfaz.Active_screen = self.Controlador_Interfaz.Menus["Main"]

                #activar el boton play inicial
                self.Controlador_Interfaz.Positioned = self.Main_Menu.buttons[0]

                #Creo el jugador, el parametro self hace referencia al mismo objeto "New_Game" que estoy creando en este init
                self.Player = Player(self,x=200)

                #creo los niveles y añado el nivel inicial
                self.Levels = []
                self.Levels.append(level(Map_1,self.width+6450,self.height,self,"./Runner_Game/Images/stage.jpg","Nivel_1",(50,50)))
                self.Levels.append(level(Map_2,self.width+4000,self.height,self,"./Runner_Game/Images/Background_Lvl.png","Nivel_2",(325,50)))
                self.Levels.append(level(Map_3,self.width+4000,self.height,self,"./Runner_Game/Images/Locked2.png","Nivel_3",(600,50)))
                self.Levels.append(level(Map_3,self.width+4000,self.height,self,"./Runner_Game/Images/Background_Lvl.png","Nivel_4",(50,50+175+10)))
                self.Levels.append(level(Map_3,self.width+4000,self.height,self,"./Runner_Game/Images/Background_Lvl.png","Nivel_5",(325,50+175+10)))
                self.Levels.append(level(Map_3,self.width+4000,self.height,self,"./Runner_Game/Images/Background_Lvl.png","Nivel_6",(600,50+175+10)))
                
                #siempre dejo desbloqueado solo el primer nivel
                self.Levels[0].locked = False
                