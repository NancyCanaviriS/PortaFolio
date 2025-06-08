import pygame 
import random

pygame.init()
WIDTH=480
HEIGHT=750


display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pill game")

FPS=60
clock=pygame.time.Clock()

MARI_STATING_LIVES=5
MARI_VELOCITY=15
PELOTA_STARTING_VELOCITY=5
PELOTA_ACCELERATION=0.5

#SCORE
score=0
player_lives=MARI_STATING_LIVES
pelota_velocity=PELOTA_STARTING_VELOCITY

#color
WHITE=(255,255,255)
BLACK=(0,0,0)


#fuentes del videoJuego
font_title_32=pygame.font.Font('horror.ttf',32)
font_title_42=pygame.font.Font('horror.ttf',42)
font_text=pygame.font.Font('texto.ttf',24)

#set title
title_text=font_title_42.render("pildoras de la programacion",True,WHITE,BLACK)
title_rect=title_text.get_rect()
title_rect.centerx=WIDTH // 2
title_rect.y=15

#configuracion del texto de puntaje
score_text=font_text.render(f"Score:"+str(score),True,WHITE,BLACK)
score_rect=score_text.get_rect()
score_rect.topleft=(10,98)

#SET LIVES
lives_text=font_text.render("Lives:"+str(player_lives),True,WHITE,BLACK)
lives_rect=lives_text.get_rect()
lives_rect.topright=(WIDTH-10,90)

#Game over title
gameover_title=font_title_42.render("GAMEOVER",True,WHITE,BLACK)
gameover_rect=gameover_title.get_rect()
gameover_rect.center=(WIDTH // 2, HEIGHT // 2)

#Game over text
continue_text=font_text.render("presiona cualquier tecla",True,WHITE,BLACK)
continue_rect=continue_text.get_rect()
continue_rect.center=(WIDTH // 2, HEIGHT // 2+60)

#imagen de la mariquita
mari_image=pygame.image.load("mari.png")
mari_rect=mari_image.get_rect()
mari_rect.left=10
mari_rect.bottom=HEIGHT-10

#imagen de la hoja 
pelota_image=pygame.image.load("pelota.png")
pelota_rect=pelota_image.get_rect()
pelota_rect.x= random.randint(0,WIDTH-64)
pelota_rect.centery = HEIGHT // 2

game_over = False

# game_loop
while not game_over:
    for event in pygame.event.get():
        if    event.type == pygame.QUIT:
            game_over= True
    keys = pygame.key.get_pressed()
    if keys [pygame.K_a] and mari_rect.left > 0:
        mari_rect.x -= MARI_VELOCITY
    if keys [pygame.K_d] and mari_rect.right<WIDTH:
        mari_rect.x += MARI_VELOCITY

    #movimiento de la pelota
    if pelota_rect.y > HEIGHT:
        player_lives -=1
        pelota_rect.x=random.randint(0,WIDTH-64)
        pelota_rect.y=140
    else:
        pelota_rect.y += pelota_velocity
    if mari_rect.colliderect(pelota_rect):
        score +=1
        pelota_velocity +=PELOTA_ACCELERATION
        pelota_rect.x=random.randint(0,WIDTH-64)
        pelota_rect.y=140
    score_text=font_text.render("score:" +str(score),True,WHITE,BLACK)
    lives_text=font_text.render("lives:" +str(player_lives),True,WHITE,BLACK)

#actualizar los textos de puntaje y vidas
    display.fill(BLACK)
    display.blit(title_text,title_rect)
    display.blit(score_text,score_rect)
    pygame.draw.line(display,WHITE,(0,140),(WIDTH,140),3)
    display.blit(lives_text,lives_rect)
    display.blit(mari_image,mari_rect)
    display.blit(pelota_image,pelota_rect)

    if player_lives==0:
        display.blit(gameover_title,gameover_rect)
        display.blit(continue_text,continue_rect)
        pygame.display.update()
        is_pause=True
        while is_pause:
             for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                    game_over=True
                    is_pause=False
                 if event.type==pygame.KEYDOWN:
                    score=0
                    player_lives=MARI_STATING_LIVES
                    pelota_velocity=PELOTA_STARTING_VELOCITY
                    is_pause=False
    pygame.display.update()
    clock.tick(FPS)






