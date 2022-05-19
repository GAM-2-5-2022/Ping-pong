import pygame, sys

pygame.init()
clock = pygame.time.Clock()

#zaslon
sirina = 600
visina = 500
screen = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption('Pong')

#smjestaj likova
lopta = pygame.Rect(sirina/2-15,visina/2-15,30,30)
igrac1 = pygame.Rect(sirina-20,visina/2-70,10,140)
igrac2 = pygame.Rect(10,visina/2-70,10,140)

#crtanje(surface,colour,rect),boja(red,green,blue)-255max
boja = (200,200,200)
boja_poz = (0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #crtanje
    screen.fill(boja_poz)
    pygame.draw.rect(screen,boja,igrac1)
    pygame.draw.rect(screen,boja,igrac2)
    pygame.draw.ellipse(screen,boja,lopta)
    pygame.draw.aaline(screen,boja,(sirina/2,0),(sirina/2,visina))
    
    pygame.display.flip()
    clock.tick(60)
