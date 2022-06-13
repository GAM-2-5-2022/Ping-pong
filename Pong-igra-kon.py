import pygame, sys, random


def lopta_animacija():
    global vloptax,vloptay,brigrac1,brigrac2,score_time
    lopta.x += vloptax
    lopta.y += vloptay
    
    if lopta.top <= 0 or lopta.bottom >= visina:
        vloptay *= -1
        
    if lopta.left <= 0:
        score_time=pygame.time.get_ticks()
        brigrac1+=1
    if lopta.right >= sirina:
        score_time=pygame.time.get_ticks()
        brigrac2 +=1
    if lopta.colliderect(igrac1) or lopta.colliderect(igrac2):
        vloptax *= -1

def restartaj():
    global vloptay, vloptax,score_time
    vrijeme_sada = pygame.time.get_ticks()
    lopta.center=(sirina/2,visina/2)
    
    if vrijeme_sada-score_time < 700:
        broj3=font.render("3",False,boja)
        screen.blit(broj3,(sirina/2, visina/2+20))

    if 700 < vrijeme_sada-score_time < 1400:
        broj2=font.render("2",False,boja)
        screen.blit(broj2,(sirina/2, visina/2+20))

    if 1400 < vrijeme_sada-score_time < 2100:
        broj1=font.render("1",False,boja)
        screen.blit(broj1,(sirina/2, visina/2+20))
    
    if vrijeme_sada-score_time < 2100:
        vloptax = 0
        vloptay = 0
    else:
        vloptay = 7 * random.choice((1,-1))
        vloptax = 7 * random.choice((1,-1))
        score_time = None
        
    

def igrac1_animacija():
    #inf za igrac
    igrac1.y += vigrac1
    if igrac1.top <=0:
        igrac1.top = 0
    if igrac1.bottom >=visina:
        igrac1.bottom = visina

def igrac2_animacija():
    if igrac2.top > lopta.y:
        igrac2.y -= vigrac2
    if igrac2.bottom < lopta.y:
        igrac2.y += vigrac2
    if igrac2.top <=0:
        igrac2.top = 0
    if igrac2.bottom >=visina:
        igrac2.bottom = visina
    
    

pygame.init()
clock = pygame.time.Clock()

#zaslon
sirina = 1000
visina = 800
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
vloptax = 7 * random.choice((1,-1))
vloptay = 7 * random.choice((1,-1))
vigrac1 = 0
vigrac2 = 7

#tekst/score
brigrac1 = 0
brigrac2 = 0
font = pygame.font.Font("freesansbold.ttf",32)

#timer
score_time = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #igrac1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vigrac1 += 7
            if event.key == pygame.K_UP:
                vigrac1 -= 7
        if event.type == pygame.KEYUP:
            vigrac1=0

       
            
    lopta_animacija()
    igrac1_animacija()
    igrac2_animacija()
    

            
    #crtanje
    screen.fill(boja_poz)
    pygame.draw.rect(screen,boja,igrac1)
    pygame.draw.rect(screen,boja,igrac2)
    pygame.draw.ellipse(screen,boja,lopta)
    pygame.draw.aaline(screen,boja,(sirina/2,0),(sirina/2,visina))

    if score_time:
        restartaj()
        
    #tekst
    igrac1_tekst=font.render(f'{brigrac1}',False,boja)
    screen.blit(igrac1_tekst,(535,320))
    igrac2_tekst=font.render(f'{brigrac2}',False,boja)
    screen.blit(igrac2_tekst,(450,320))
    
    pygame.display.flip()
    clock.tick(60)
