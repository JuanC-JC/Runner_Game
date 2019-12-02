import pygame

#clase menu, realiza la seleccion de los botones en el menu, controlador de mouse y controlador de eventos
class Menu():
    def __init__(self,Game):
        self.game = Game
        self.window = self.game.window
        self.buttons = []
        self.Actually_Press = None

    def __Do_Selection(self):
        for button in self.buttons:
            if button == self.Actually_Press:
                button.selected()
            else:
                button.Unselected()

    def Mouse_Controller(self,Click_Pos):
        for button in self.buttons:
            if button.Touching(Click_Pos):
                self.Actually_Press = button
                self.__Do_Selection()      

    def Events_Controller(self,event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                if self.buttons.index(self.Actually_Press) + 1 == len(self.buttons):
                    self.Actually_Press = self.buttons[0]
                else:
                    self.Actually_Press = self.buttons[self.buttons.index(self.Actually_Press)+1]

            elif event.key == pygame.K_UP:
                if self.buttons.index(self.Actually_Press) == 0:
                    self.Actually_Press = self.buttons[len(self.buttons)-1]
                else:
                    self.Actually_Press = self.buttons[self.buttons.index(self.Actually_Press)-1]

            elif event.key == pygame.K_RETURN:
                if self.Actually_Press.text == "Play":
                    self.game.Active_screen = "Lvls_Menu"

                elif self.Actually_Press.text == "Menu":
                    self.game.Active_screen = "Main_Menu"

                elif self.Actually_Press.text == "Back":
                    self.game.Active_screen = "Game"

                elif self.Actually_Press.text == "Exit":
                    self.game.Run = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.Actually_Press.text == "Play":
                    self.game.Active_screen = "Lvls_Menu"

                elif self.Actually_Press.text == "Menu":
                    self.game.Active_screen = "Main_Menu"

                elif self.Actually_Press.text == "Back":
                    self.game.Active_screen = "Game"

                elif self.Actually_Press.text =="Exit":
                    self.game.Run = False

                elif self.Actually_Press.text == "Nivel_1":
                    self.game.Active_screen = "Game"
                    self.game.Player.lvl = self.game.Levels[0]
                    self.game.Player.Reload()

                elif self.Actually_Press.text == "Nivel_2" and self.game.Levels[1].locked == False :
                    self.game.Active_screen = "Game"
                    self.game.Player.lvl = self.game.Levels[1]
                    self.game.Player.Reload()

                elif self.Actually_Press.text == "Nivel_3" and self.game.Levels[2].locked == False:
                    self.game.Active_screen = "Game"
                    self.game.Player.lvl = self.game.Levels[2]
                    self.game.Player.Reload()

        self.__Do_Selection()
   
    def Display(self):
        for button in self.buttons:
            button.draw()

class Button_Game():
    
    def __init__(self,Width,Height,Text,Color=(255,255,255),Position=(250,250),Alpha=(False,(0,0,0),100),Select=False,Screen=None):

        self.screen = Screen
        self.width = Width
        self.height = Height
        self.text = Text
        self.color = Color
        self.position = Position
        self.position_x = self.position[0]
        self.position_y = self.position[1]
        self.alpha = Alpha
        self.select = Select

        if self.select: self.selected() 
        else: self.Unselected()
        
    def selected(self):

        self.__font = pygame.font.SysFont("comicsansms",self.height+10)

        self.render_font = self.__font.render(self.text,True,(0,0,255),None)

        self.rect_render = self.render_font.get_rect()

        self.rect_render.center = (self.position_x,self.position_y)

        self.rect_render.height -= 20

        if self.alpha[0]:
            self.Alpha_Button = pygame.Surface((self.rect_render.width,self.rect_render.height))

            self.Alpha_Button.set_alpha(self.alpha[2])            # alpha level
            self.Alpha_Button.fill(self.alpha[1])                  # this fills the entire surface

    def Unselected(self):
        
        self.__font = pygame.font.SysFont("comicsansms",self.height)

        self.render_font = self.__font.render(self.text,True,self.color,None)

        self.rect_render = self.render_font.get_rect()

        self.rect_render.center = self.position

        self.rect_render.height -=20

        if self.alpha[0] == True:
            self.Alpha_Button = pygame.Surface((self.rect_render.width,self.rect_render.height))

            self.Alpha_Button.set_alpha(self.alpha[2])            # alpha level
            self.Alpha_Button.fill(self.alpha[1])                  # this fills the entire surface

    def draw(self):
        if self.alpha[0]:
            self.screen.blit(self.Alpha_Button,self.rect_render)

        self.screen.blit(self.render_font,self.rect_render)

    def Touching(self,Cl_Pos):
        if (Cl_Pos[0] >= self.rect_render.left and Cl_Pos[0] <= self.rect_render.right and Cl_Pos[1] >= self.rect_render.top and Cl_Pos[1] <= self.rect_render.bottom):
            return True
        else:
            return False


    def __str__(self):
        return self.text

class Main_Menu(Menu):

    def __init__(self,Game,Background):

        super().__init__(Game)

        image = pygame.image.load(Background).convert()
        self.Background = pygame.transform.scale(image,(self.game.width,self.game.height)).convert()
        self.Background_rect = self.Background.get_rect()

        self.Name_Game = Button_Game(100,100,"Can you jump?",Position=(self.game.width//2,100),Screen=self.window)
        self.Play = Button_Game(100,50,"Play",Position=(self.game.width//2,300),Select=True,Screen=self.window,Alpha=(True,(0,0,0),100))
        self.Store = Button_Game(100,50,"Store",Position=(self.game.width//2,370),Screen=self.window,Alpha=(True,(0,0,0),100))
        self.Exit = Button_Game(100,50,"Exit",Position=(self.game.width//2,440),Screen=self.window,Alpha=(True,(0,0,0),100))
        self.buttons = [self.Play,self.Store,self.Exit]
        self.Actually_Press = self.Play

    def display(self):
        self.window.blit(self.Background,self.Background_rect)
        self.Name_Game.draw()
        super().Display()

class Pause_Menu(Menu):
    def __init__(self,Game):
        super().__init__(Game)
        self.Title_Pause = Button_Game(100,80,"PAUSE",Position=(self.game.width//2,150),Alpha=(True,(0,0,0),100),Screen=self.window)
        self.Return = Button_Game(100,50,"Back",Position=(self.game.width//2,250),Alpha=(True,(0,0,0),100),Select=True,Screen=self.window)
        self.Menu = Button_Game(100,50,"Menu",Position=(self.game.width//2,330),Alpha=(True,(0,0,0),100),Screen=self.window)
        self.Exit = Button_Game(100,50,"Exit",Position=(self.game.width//2,410),Alpha=(True,(0,0,0),100),Screen=self.window)

        self.buttons= [self.Return,self.Menu,self.Exit]
        self.Actually_Press = self.Return
        
    def display(self):
        self.Title_Pause.draw()
        super().Display()

class Button_Lvl():
    
    def __init__(self,Width,Height,Image,Name,Position=(0,0),Select=False,Screen=None,Lvl=None):

        self.screen = Screen
        self.width = Width
        self.height = Height
        self.position = Position
        self.position_x = Position[0]
        self.position_y = Position[1]
        self.select = Select

        self.text = Name

        self.Lvl = Lvl
    
        img = pygame.image.load(Image).convert()
        self.Background = pygame.transform.scale(img,(self.width,self.height)).convert()
        self.Background_rect = self.Background.get_rect()

        img = pygame.image.load("./Runner_Game/Images/Locked2.png").convert()
        self.Background_Locked = pygame.transform.scale(img,(self.width,self.height)).convert()

        self.Background_rect.x = self.position_x
        self.Background_rect.y = self.position_y

        if self.select: self.selected() 
        else: self.Unselected()

    def draw(self):

        if self.select: pygame.draw.rect(self.screen,(255,255,255),self.Background_rect,10)
        
        #si esta bloqueado el nivel dibuja la imagen del candado si no, dibuja el background normal
        if self.Lvl.locked:
            self.screen.blit(self.Background_Locked,self.Background_rect)
        else:
            self.screen.blit(self.Background,self.Background_rect)

    def selected(self):
        self.select = True

    def Unselected(self):
        self.select = False

    def Touching(self,Cl_Pos):
        if (Cl_Pos[0] >= self.Background_rect.left and Cl_Pos[0] <= self.Background_rect.right and Cl_Pos[1] >= self.Background_rect.top and Cl_Pos[1] <= self.Background_rect.bottom):
            return True
        else:
            return False

class Levels_Menu(Menu):
    def __init__(self,Game,Background):
        super().__init__(Game)

        image = pygame.image.load(Background).convert()
        self.Background = pygame.transform.scale(image,(self.game.width,self.game.height)).convert()
        self.Background_rect = self.Background.get_rect()

        self.buttons.append(Button_Game(100,50,"Menu",Position=(100,450),Select=False,Screen=self.window,Alpha=(True,(0,0,0),100)))

        self.Actually_Press = self.buttons[0]

    def Display(self):
        self.window.blit(self.Background,self.Background_rect)
        super().Display()

    def Add_Lvl(self,Width,Height,Image,Name,Select,Position,Screen,Lvl):
        self.buttons.append(Button_Lvl(Width,Height,Image,Name,Position,Select,Screen,Lvl))
