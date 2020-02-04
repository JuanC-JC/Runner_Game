import pygame
from Menu import *

"""-------------------------Clase Niveles-------------------------
    Recibe parametros como una matriz constructora junto a su ancho y alto
    para ajustar el tamaño de los "Objetos", recibe el juego sobre el cual correra 
    el nivel y recibe una url de imagen de fondo
    """


class level:
    def __init__(self, matrix, width, height, Game, Background, Name, Button_Position):
        
        self.matriz = matrix
        self.width = width
        self.height = height
        self.__game = Game
        self.screen = self.__game.window
        self.Name = Name

        image = pygame.image.load(Background).convert()
        self.Background = pygame.transform.scale(image, (self.__game.width, self.__game.height)).convert()
        self.Background_rect = self.Background.get_rect()

        self.velocity_x = 4
        self.x = 0
        self.stop = False
        self.locked = True

        self.List_Bloques = []
        self.Lista_Coins = []

        #añado el nivel al menu de niveles
        self.__game.Levels_Menu.Add_Lvl(250, 175, Background, Name, False, Button_Position, self.screen, self)

        self.__load()

    # retorna los objetos pertenecientes al nivel "tiles"
    def Objects(self):
        return self.totally

    # Movimiento de todos los tiles en el eje x
    def move(self):

        for block in self.totally:

            block.rect.x -= self.velocity_x

        self.x += self.velocity_x

    # Sistema de colisiones eliminar un tile del nivel si es necesario
    def remove(self, x):
        self.totally.pop(x)

    # actualizar el estado de los bloques "display"
    def Update(self):

        self.screen.blit(self.Background, self.Background_rect)

        for block in self.totally:
            block.draw(self.screen)

    """Carga la matriz del mapa en el juego"""
    def __load(self):

        capa = len(self.matriz)

        y = 0
        for layer in self.matriz:
            x = 0
            for tile in layer:

                if tile == "T":

                    block = Sprite(
                        x,
                        y,
                        self.width // len(layer),
                        self.height // len(self.matriz),
                        capa,
                        "Grass",
                    )

                    self.List_Bloques.append(block)

                elif tile == "*":

                    block = Sprite(
                        x,
                        y,
                        self.width // len(layer),
                        self.height // len(self.matriz),
                        capa,
                        "Coin",
                    )

                    self.Lista_Coins.append(block)

                x = x + self.width // len(layer)

            y = y + self.height // len(self.matriz)

            capa -= 1

        self.totally = self.List_Bloques + self.Lista_Coins

    # Recargar el mapa si reinicia el nivel, si la logica lo requiere debo hacer de nuevo el __load ya que necesito que aparezcan todos los elementos de nuevo
    # ya que al utilizar el remove, eliminaria un dato de la matriz
    def Reload(self):
        self.List_Bloques.clear()
        self.Lista_Coins.clear()
        self.totally.clear()
        self.x = 0
        self.__load()

    # Pierde el nivel
    def Loser(self):
        # crear primero el font
        texto = pygame.font.SysFont("comicsansms", 100)

        # rendereizar el font
        render = texto.render("GAMER OVER!! Loser", True, (0, 0, 0), None)

        render_rect = render.get_rect()
        render_rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)

        # dibujar el font como una imagen --- remplazar por un gamer over bonito
        self.screen.blit(render, render_rect)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, capa, option):
        pygame.sprite.Sprite.__init__(self)

        self.type = option

        self.__Grass = pygame.image.load("./Runner_Game/Images/grass.png").convert()

        if self.type == "Grass":
            self.image = self.__Grass
            self.image = pygame.transform.scale(self.image, (width, height))

        if self.type == "Coin":
            self.Imgs_Coin = []
            self.movement = 1
            for i in range(1, 11):
                self.image = pygame.image.load(
                    "./Runner_Game/Images/Coin/Gold ({}).png".format(i)
                )
                self.image = pygame.transform.scale(
                    self.image,
                    (
                        int(self.image.get_width() / 10),
                        int(self.image.get_height() / 10),
                    ),
                )
                self.Imgs_Coin.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.capa = capa

    def draw(self, screen):

        if self.type == "Coin":

            if self.movement >= len(self.Imgs_Coin * 4):
                self.movement = 0
            else:
                self.image = self.Imgs_Coin[self.movement // 4]
                self.movement += 1

            rect_buffer = self.image.get_rect()     # obtengo un rectangulo de la imagen
            rect_buffer.center = self.rect.center   # Posiciono el rectangulo en el medio de la imagen

            screen.blit(self.image, rect_buffer)

        else:

            screen.blit(self.image, self.rect)
