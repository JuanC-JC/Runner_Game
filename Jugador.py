import pygame

#Clase jugador
class Player(pygame.sprite.Sprite):

    def __init__(self,Game,x=0,y=0):

        pygame.sprite.Sprite.__init__(self)                         #player es parte de una super clase llamada sprite

        self.__game = Game
        self.screen = self.__game.window                            #pantalla sobre la cual se dibuja

        self.lvl = None

        self.__load_images(x,y)                                     #cargo todas las imagenes necesarias

        self.rect = pygame.Rect(x,y,37,100)                         # El objeto que manipulo para el "Jugador" 
        self.Frame = 0 

        self.jump = False
        self.jumps = 0
        self.Charge_Jumps = 0

        self.mov_right = True
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.2

        self.lifes = 3

        #Objetos para incluir en el jugador
        self.jecktpack = False
        self.acpm = 0

    
    def __load_images(self,x,y):

        self.__Imgs_Right = []
        self.__Imgs_Lifes = []
        self.__Imgs_Jump = []

        for i in range(1,16):
            image = pygame.image.load("./Runner_Game/Images/Player/Walk ({}).png".format(i))
            image = pygame.transform.scale(image,(122,112))
            self.__Imgs_Right.append(image)

        for i in range (4,16):
            image = pygame.image.load("./Runner_Game/Images/Player/Jump ({}).png".format(i))
            image = pygame.transform.scale(image,(122,112))
            self.__Imgs_Jump.append(image)

        for i in range (1,4):
            image = pygame.image.load("./Runner_Game/Images/Lifes ({}).png".format(i))
            image = pygame.transform.scale(image,(int(image.get_width()/5),int(image.get_height()/5)))
            self.__Imgs_Lifes.append(image)


        self.image = self.__Imgs_Right[0]                     

        self.Image_Life = self.__Imgs_Lifes[0]

    #Gravedad aplicada sobre el jugador
    def __gravedad(self):
        self.velocity_y -= self.gravity
        self.rect.y -= self.velocity_y

    #Efectua el salto segun las condiciones del jugador
    def jumping(self):
        if self.jecktpack and self.acpm > 0:
            self.velocity_y = 7.5
            self.acpm -=1

        elif self.jumps > 0:
            self.jump = True
            self.velocity_y = 7.5
            self.jumps -=1
            self.Frame = 0

    #Realiza el cambio de imagen del jugador segun la direccion o movimiento
    def __next_frame(self):
        if self.jump:
            if self.Frame >= len(self.__Imgs_Jump)*6:
                self.Frame = 0
            else: 
                self.image = self.__Imgs_Jump[self.Frame//6]
                self.Frame += 1
        else:
            if self.Frame >= len(self.__Imgs_Right)*3:
                self.Frame = 0
            else:
                self.image = self.__Imgs_Right[self.Frame//3]
                self.Frame +=1

    #Retorna una lista con todos los elementos que estan siendo tocados por el jugador
    def __collide(self):

        Colisiones = []

        for Plataform in self.lvl.Objects():
            if self.rect.colliderect(Plataform.rect):
                Colisiones.append(Plataform)

        return Colisiones

    def __move(self):   
        
        #Primero se mueve el Mapa para calcular la posicion en la que "ahora estaria el jugador"
        self.lvl.move()

        #conforme se movio el mapa, calculamos si segun la nueva posicion del mapa debo estar muerto o vivo
        self.__Live_Or_Death()

        #Colisiones del eje x
        for colision in self.__collide():
            #Ya que el movimiento del mapa siempre es hacia atras, La colision es entorno a la derecha y por lo tanto se 
            #toma la posicion izquierda del objeto
            self.rect.right = colision.rect.left
            
            #si estoy tocando una moneda paso de nivel
            if colision.type == "Coin":
                self.New_Lvl()

        #Una vez calculo las colisiones de mi objeto en x, efectuo la gravedad

        self.__gravedad()

        #aplicar el movimiento segun la colision en el eje Y
        for colision in self.__collide():

            #calculo la ultima posicion del piso de mi jugador
            Last_Bottom =  self.rect.bottom + self.velocity_y

            # para calcular la posicion anterior del jugador en y es necesario tomar la posicion en Y actual y restarle mi velocidad de caida
            if self.velocity_y > 0:
                Last_Top = self.rect.top - self.velocity_y 
            else:
                Last_Top = self.rect.top + self.velocity_y 

            #si la ultima posicion de mi jugador en el piso es menor que la parte superior del objeto con el que colisione
            if Last_Bottom <= colision.rect.top:
                self.rect.bottom = colision.rect.top
                self.velocity_y = 0
                self.jump = False

                if self.Charge_Jumps <= 100:
                    self.Charge_Jumps += 10
                
                #al estar tocando el suelo, revisa si tiene los saltos cargados al 100 si es asi, asigna 2 saltos si no lo es solo asigna 1 salto
            
                if self.Charge_Jumps >= 100:
                    self.jumps = 2
                else:
                    self.jumps = 1
            
            #si esta colisionando con la cabeza 
            elif Last_Top <= colision.rect.bottom:
                self.rect.top = colision.rect.bottom
                self.velocity_y = 0.2

        #si el contador se encuentra cargado y no tengo mas saltos disponibles, colo el valor del cargador en 0 
        if self.Charge_Jumps > 100 and self.jumps == 0:
            self.Charge_Jumps = 0

        #coloco la nueva imagen
        self.__next_frame()

    def __Live_Or_Death(self):
        if self.rect.top >= self.screen.get_width() or self.rect.right <= 0 :
            self.Reload()
            self.__Lose_Life()

    def __Add_Life(self):
        pass
    
    #Revisar como se pierden las vidas y las imagenes
    def __Lose_Life(self):
        #revisar este codigo que pereza
        if self.lifes > 1:
            self.lifes -= 1
            self.Image_Life = self.__Imgs_Lifes[3-self.lifes]
        else: 
            self.lifes = 0

    def New_Lvl(self):
        self.__game.Levels[self.__game.Levels.index(self.lvl)+1].locked = False
        self.lvl  = self.__game.Levels[self.__game.Levels.index(self.lvl)+1]
        self.Reload()

    def update(self):

        #Actualizo el screen del nivel
              
        self.lvl.Update()
        
        self.__move()                                                                                       #hago que el personaje valide movimientos

        self.screen.blit(self.image,(self.rect.x-10,self.rect.y))                                           #carga el sprite del jugador sobre la pantalla con una posicion en x menor a la normal

        # pygame.draw.rect(self.screen,(0,0,0),self.rect,2)                                                 #sirve para ver el cuadro de coliciones del objeto

        self.screen.blit(self.Image_Life,(self.screen.get_width()-self.Image_Life.get_width()-50,10))       #posiciona la imagen de vida

        pygame.draw.rect(self.screen,(0,0,0),(10,10,(self.Charge_Jumps*2),40))
        pygame.draw.rect(self.screen,(0,0,0),(10,10,220,40),1)

    def Reload(self):
        self.rect.x = 200
        self.rect.y = 0

        self.mov_right = True
        self.jumps = 0
        self.Charge_Jumps = 0

        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.2

        self.lvl.Reload()

