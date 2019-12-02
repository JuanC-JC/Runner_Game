import pygame

pygame.init()

clock = pygame.time.Clock()

world_width = 900                      #ancho de la pantalla
world_height = 506                      #altura de la pantalla
fps = 60                               #frames por segundo

world = pygame.display.set_mode((world_width,world_height))                             #configuro la pantalla con un ancho y alto
pygame.display.set_caption("Plataform Game")                                            #coloco el titulo de la pantalla

backdrop = pygame.image.load("./Project_Game/Images/stage.jpg").convert()               #cargo la imagen
backdrop = pygame.transform.scale(backdrop,(world_width+1000,world_height)).convert()
backdropbox = backdrop.get_rect()                                                       #obtengo un rectangulo en posicion 0,0 ya que inicia sobre la imagen

game = True

class personaje():

    def __init__(self):
        self.x = 0
        self.jump = False

    def move(self):
        if self.jump:
            self.x += 1

    def update(self):
        self.move()
        print(self.x)


x = personaje()

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                x.jump = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_SPACE:
                x.jump = False
        
    
    x.update()
    pygame.display.update()
    clock.tick(60)
