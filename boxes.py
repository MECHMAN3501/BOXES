import pygame
import random
import time
pygame.init()
points=0
font_object = pygame.font.SysFont('consolas', 28)
counter = font_object.render(f'score:{points}', True, 'black', 'white')
font_object2 = pygame.font.SysFont('consolas', 100)

SCREEN_SIZE=SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
screen=pygame.display.set_mode(SCREEN_SIZE)
clock=pygame.time.Clock()
rect_x=50
rect_y=50
speed=5
all_sprite = pygame.sprite.Group() 
player = pygame.sprite.Sprite(all_sprite) 
player.image = pygame.image.load('box.png') 
player.rect = player.image.get_rect() 
player.rect.x = 50
player.rect.y = 50
coin = pygame.sprite.Sprite(all_sprite) 
coin.image = pygame.image.load('coinbox.png') 
coin.rect = player.image.get_rect() 
coin.rect.x = random.randint(100,300)
coin.rect.y = random.randint(100,300)
enemy = pygame.sprite.Sprite(all_sprite) 
enemy.image = pygame.image.load('enemybox.png') 
enemy.rect = player.image.get_rect() 
enemy.rect.x = 400
enemy.rect.y = 400
run=True
while run:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and rect_y!=0:
        rect_y-=5
    if keys[pygame.K_d] and rect_x<368:
        rect_x+=5
    if keys[pygame.K_a] and rect_x!=0:
        rect_x-=5
    if keys[pygame.K_s] and rect_y<368:
        rect_y+=5
    player.rect.x = rect_x
    player.rect.y = rect_y
    if pygame.sprite.collide_rect(player, coin)==True:
        coin.rect.x = random.randint(100,300)
        coin.rect.y = random.randint(100,300)
        points+=100
    if pygame.sprite.collide_rect(enemy, coin)==True:
        coin.rect.x = random.randint(100,300)
        coin.rect.y = random.randint(100,300)
    if pygame.sprite.collide_rect(player, enemy)==True:
        diescreen=font_object2.render(f'WASTED', True, 'red', 'white')
        screen.blit(diescreen, (30, 150))
        run = False
    all_sprite.draw(screen)
    screen.blit(counter, (10, 10))
    if rect_x<enemy.rect.x:
        enemy.rect.x-=2.5
    elif rect_x>enemy.rect.x:
        enemy.rect.x+=2.5
    if rect_y<enemy.rect.y:
        enemy.rect.y-=2.5
    elif rect_y>enemy.rect.y:
        enemy.rect.y+=2.5
    counter = font_object.render(f'score:{points}', False, 'black', 'white')
    pygame.display.update()
    clock.tick(60)
time.sleep(3)
pygame.quit()
