import pygame
import random
import time

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo em python')


bgImg = pygame.image.load('img/ceuEstrelado.jpg').convert_alpha()
bg = pygame.transform.scale(bgImg, (x, y))

alienImg = pygame.image.load('img/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alienImg, (50, 50)) 


playerImg = pygame.image.load('img/nave.png').convert_alpha()
player = pygame.transform.scale(playerImg, (100, 100))
player = pygame.transform.rotate(player, -90)


missilImg = pygame.image.load('img/esfera.png').convert_alpha()
missil = pygame.transform.scale(missilImg, (25, 25))
missil = pygame.transform.rotate(missil, -45)

bossImg = pygame.image.load('img/boss.png').convert_alpha()
boss = pygame.transform.scale(bossImg, (600, 500))
boss = pygame.transform.rotate(boss, -45)

missilBossImg = pygame.image.load('img/missilBoss.png').convert_alpha()
missilBoss = pygame.transform.scale(missilBossImg, (50, 50))





font = pygame.font.SysFont('fonts/fontArcade.ttf', 50)
gameOverFont = pygame.font.SysFont('fonts/fontArcade.ttf', 80)

fraseGameOver = 'Voce perdeu vacilao!'






position_alien_x = 1280
position_alien_y = 360


position_player_x = 200
position_player_y = 300

velocidade_missil_x = 0
position_missil_x = 200
position_missil_y = 300


position_boss_x = 900
position_boss_y = -50

velocidade_missilBoss_x = 0
position_missilBoss_x = 1100
position_missilBoss_y = 300


lifeImg = pygame.image.load('img/life.jpg').convert_alpha()
lifeImg = pygame.transform.scale(lifeImg, (25,25))
life = 3


lifeBoss = 15

pontos = 0

triggered = False

rodando = True

player_rect = player.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()
missilBoss_rect = missilBoss.get_rect()

# funções respawn

def respaw():
    x = 1350
    y = random.randint(1, 640)
    return [x,y]

def respaw_missil():
    triggered = False
    respaw_missil_x = position_player_x 
    respaw_missil_y = position_player_y 
    velocidade_missil_x = 0
    return [(respaw_missil_x + 20), (respaw_missil_y + 30), triggered, velocidade_missil_x]


def respaw_missilBoss():
    
    print('cheguei aqui')
    
    respaw_missilBoss_x = position_boss_x
    respaw_missilBoss_y = position_boss_y
    velocidade_missilBoss_x = 0
   
    return [respaw_missilBoss_x, respaw_missilBoss_y, velocidade_missilBoss_x]


#funçoes colisao

def colisaoInimigo():
    global life

     
    for i in range(life): #range = quantidade de vida
        screen.blit(lifeImg, (50 + i * 30, 50))

         
    if life == 0: 
        gameOver = gameOverFont.render(fraseGameOver, True, (255,255,255))
        screen.blit(gameOver, (350,300))
        return True
    
    elif player_rect.colliderect(alien_rect) or alien_rect.x == 10:  
        life + 1
        life -= 1

        return True
    
    else: 
        return False
 
    
def colisaoMissil():
    global pontos
    global position_alien_x
    global position_alien_y
    global position_missil_x
    global position_missil_y
    global triggered
    global velocidade_missil_x
    
    if missil_rect.x == 1300:
        position_missil_x = respaw_missil()[0]
        position_missil_y = respaw_missil()[1]
        triggered = respaw_missil()[2]
        velocidade_missil_x = respaw_missil()[3] 
   
    if missil_rect.colliderect(alien_rect): 
        position_alien_x = respaw()[0]
        position_alien_y = respaw()[1]
        
        pontos +=100

        return True
    else: 
        return False



# def colisao_bossMissil():

#     global position_missilBoss_x
#     global position_missilBoss_y
    
#     print('tcheguei')
    
#     if position_missilBoss_x == 100:
#         print('to aqui')
#         position_missilBoss_x = respaw_missilBoss()[0]
#         position_missilBoss_y = respaw_missilBoss()[1]
        
        # position_missilBoss_x -= 4
        
            
        
# jogo rodando

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            
    screen.blit(bg, (0, 0))  
    
    relativo_x = x % bg.get_rect().width
    screen.blit(bg, (relativo_x - bg.get_rect().width, 0)) #cria background 

    if relativo_x < 1280:
        screen.blit(bg, (relativo_x, 0))
        
    #comandos 
    
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and position_player_y > 1:
        position_player_y -= 1
        
        if not triggered:
            position_missil_y -= 1
        
    if tecla[pygame.K_DOWN] and position_player_y < 665:
        position_player_y += 1
        
        if not triggered:
            position_missil_y += 1
        
    if tecla[pygame.K_SPACE]:
        triggered = True
        velocidade_missil_x = 4   
    
  
        
        
    # respawn
             
    if position_alien_x == 9 or colisaoInimigo():
        position_alien_x = respaw()[0]
        position_alien_y = respaw()[1]
         
        
    if position_missil_x == 1300 or colisaoMissil():
        position_missil_x = respaw_missil()[0]
        position_missil_y = respaw_missil()[1]
        triggered = respaw_missil()[2]
        velocidade_missil_x = respaw_missil()[3]
        
        
        
     
    #posição rect 
    
    player_rect.x = position_player_x 
    player_rect.y = position_player_y
    
    missil_rect.x = position_missil_x
    missil_rect.y = position_missil_y
    
    alien_rect.x = position_alien_x
    alien_rect.y = position_alien_y
    
    missilBoss_rect.x = position_missilBoss_x
    missilBoss_rect.y = position_missilBoss_y
    
    
            
    # movimento / fases 
    
    # if pontos < 101:  
    #     x -= 1.5 
    #     position_alien_x -= 0.5 
    #     position_missil_x += velocidade_missil_x
    
    # elif pontos < 201: 
    #     x -= 1.5 
    #     position_alien_x -= 0.75
    #     position_missil_x += velocidade_missil_x   
    
    # elif pontos < 301: 
    #     x -= 1.5
    #     position_alien_x -= 1
    #     position_missil_x += velocidade_missil_x   
    
    # el
    if pontos < 101: 
        x -= 1.5 
        position_alien_x -= 1.5
        position_missil_x += velocidade_missil_x 
    
    elif pontos >= 200: 
          
        screen.blit(boss, (position_boss_x, position_boss_y))
        
        
        
        if position_missilBoss_x <= 1100:
            position_missilBoss_x -= 3
            print (position_missilBoss_x)
            
            
            if position_missilBoss_x == 100:
                position_missilBoss_x = respaw_missilBoss()[0]
                position_missilBoss_y = respaw_missilBoss()[1]
                velocidade_missilBoss_x = respaw_missilBoss()[2]
                print(velocidade_missilBoss_x)
            else:
                print(' nao pegou o if')
        else:
            print('to qui')    

    
        x -= 1.5 
       
        position_alien_x = 1300
        position_missil_x += velocidade_missil_x 
    
    # pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
    # pygame.draw.rect(screen, (255, 0, 0), alien_rect, 4)
    # pygame.draw.rect(screen, (255, 0, 0), missil_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), missilBoss_rect, 4)
    
    
    score = font.render(str(pontos), True, (255,255,255))
    screen.blit(score, (1150, 50))
    
    
    
    # posicao inicial do player e inimigo 
    screen.blit(missil, (position_missil_x, position_missil_y)) 
    screen.blit(player, (position_player_x, position_player_y))
    screen.blit(missilBoss, (position_missilBoss_x, position_missilBoss_y))
    screen.blit(alien, (position_alien_x, position_alien_y))

  
            
    pygame.display.update()
