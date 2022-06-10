import pygame, sys

def lopta_animacija():
    #inf za loptu
    global vloptax,vloptay
    lopta.x += vloptax
    lopta.y += vloptay
    if lopta.top <= 0 or lopta.bottom >= visina:
        vloptay *= -1
    if lopta.left <= 0 or lopta.right >= sirina:
        vloptax *= -1
    if lopta.colliderect(igrac1) or lopta.colliderect(igrac2):
        vloptax *= -1

pygame.init()
clock = pygame.time.Clock()

#zaslon
sirina = 1000
visina = 700
screen = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption('Pong')

#smjestaj likova
lopta = pygame.Rect(sirina/2-15,visina/2-15,30,30)
igrac1 = pygame.Rect(sirina-20,visina/2-70,10,140)
igrac2 = pygame.Rect(10,visina/2-70,10,140)

#crtanje(surface,colour,rect),boja(red,green,blue)-255max
boja = (200,200,200)
boja_poz = (0,0,0)

#pocetno
vloptax = 7
vloptay = 7
vigrac1 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #igrac
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vigrac1 += 7
            if event.key == pygame.K_UP:
                vigrac1 -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                vigrac1 -= 7
            if event.key == pygame.K_UP:
                vigrac1 += 7
            
    lopta_animacija()       

    #inf za igrac
    igrac1.y += vigrac1


            
    #crtanje
    screen.fill(boja_poz)
    pygame.draw.rect(screen,boja,igrac1)
    pygame.draw.rect(screen,boja,igrac2)
    pygame.draw.ellipse(screen,boja,lopta)
    pygame.draw.aaline(screen,boja,(sirina/2,0),(sirina/2,visina))
    
    pygame.display.flip()
    clock.tick(60)
