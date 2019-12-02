
import pygame

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self,x,y,width,height,capa,option):
        pygame.sprite.Sprite.__init__(self)

        self.type = option

        self.__Grass = pygame.image.load("./Runner_Game/Images/grass.png").convert()

        if self.type == "Grass":
            self.image = self.__Grass
            self.image = pygame.transform.scale(self.image,(width,height))

        if self.type == "Coin":
            self.Imgs_Coin = []
            self.movement = 1
            for i in range(1,11):
                self.image = pygame.image.load("./Runner_Game/Images/Coin/Gold ({}).png".format(i))
                self.image = pygame.transform.scale(self.image,(int(self.image.get_width()/10),int(self.image.get_height()/10)))
                self.Imgs_Coin.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y     
        self.mask = pygame.mask.from_surface(self.image)
        self.capa = capa

    def draw(self,screen):

        if self.type == "Coin":
        
            if self.movement >= len(self.Imgs_Coin*4):
                self.movement = 0
            else:
                self.image = self.Imgs_Coin[self.movement//4]
                self.movement += 1

            rect_buffer = self.image.get_rect()                     #obtengo un rectangulo de la imagen 
            rect_buffer.center = self.rect.center                   # y la centro sobre el rectangulo original
            
            screen.blit(self.image,rect_buffer)
            
        else:

            screen.blit(self.image,self.rect)
