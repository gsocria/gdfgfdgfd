import pygame
import random

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo em python')


bgImg = pygame.image.load('img/ceuEstrelado.jpg').convert_alpha()
bg = pygame.transform.scale(bgImg, (x, y))

alienImg = pygame.image.load('img/spaceship.png').convert_alpha()
alien = pygame.transform.scale(alienImg, (50, 50)) 


playerImg = pygame.image.load('img/space.png').convert_alpha()
player = pygame.transform.scale(playerImg, (50, 50))
player = pygame.transform.rotate(player, -90)


missilImg = pygame.image.load('img/missile.png').convert_alpha()
missil = pygame.transform.scale(missilImg, (25, 25))
missil = pygame.transform.rotate(missil, -45)




position_alien_x = 1290
position_alien_y = 360


position_player_x = 200
position_player_y = 300

velocidade_missil_x = 0
position_missil_x = 200
position_missil_y = 300



triggered = False

rodando = True

# funções

def respaw():
 x = 1350
 y = random.randint(1, 640)
 return [x,y]



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
        
    # respawn
        
    if position_alien_x == -10:
        position_alien_x = respaw()[0]
        position_alien_y = respaw()[1]    
        
            
    # movimento    
    x -= 1.5 
    position_alien_x -= 0.5
    position_missil_x += velocidade_missil_x
    
    # posicao inicial do player e inimigo 
    screen.blit(missil, (position_missil_x, position_missil_y)) 
    screen.blit(player, (position_player_x, position_player_y))
    screen.blit(alien, (position_alien_x, position_alien_y)) 
  
            
    pygame.display.update()

