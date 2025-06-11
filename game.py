from math import gamma

import pygame
import random
from pygame.locals import (K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT)
pygame.init()

running_game = True  # renamed to avoid conflict with the old "def game"

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

hp = 3

game_font1 = pygame.font.SysFont("Catamaran", 50)
survival_time = 0
start_time = pygame.time.get_ticks()
game_over = False
end_font = pygame.font.SysFont("RobotoMono", 60)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("jet.png")
        self.image = pygame.transform.scale(self.image, (84, 32))
        self.surf = self.image.convert()
        self.surf.set_colorkey((255,255,255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed):
        if pressed[K_w]:
            self.rect.move_ip(0, -4)
        if pressed[K_s]:
            self.rect.move_ip(0,4)
        if pressed[K_a]:
            self.rect.move_ip(-4,0)
        if pressed[K_d]:
            self.rect.move_ip(4,0)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100), random.randint(0, SCREEN_HEIGHT))
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super(Rocket, self).__init__()
        self.image = pygame.image.load("missile.png")
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.surf = self.image.convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(SCREEN_WIDTH+25, SCREEN_WIDTH+100), random.randint(0, SCREEN_HEIGHT))
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

plane = Player()
clock = pygame.time.Clock()

ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY, 1000)
pygame.time.set_timer(ADDCLOUD, 1000)

clouds = pygame.sprite.Group()
rockets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(plane)

running = True
while running:
    if game_over == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_rocket = Rocket()
                rockets.add(new_rocket)
                all_sprites.add(new_rocket)
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)



        pressed = pygame.key.get_pressed()
        plane.update(pressed)
        clouds.update()
        rockets.update()
        screen.fill((148, 227, 246))

        for i in all_sprites:
            screen.blit(i.surf, i.rect)

        if pygame.sprite.spritecollideany(plane, rockets):
            obj = pygame.sprite.spritecollideany(plane, rockets)
            obj.kill()
            hp -= 1

        if hp == 3:
            healthimg = pygame.image.load("3hearts.png").convert_alpha()
        elif hp == 2:
            healthimg = pygame.image.load("2hearts.png").convert_alpha()
        elif hp == 1:
            healthimg = pygame.image.load("1heart.png").convert_alpha()
        elif hp == 0:
            survival_time = (pygame.time.get_ticks() - start_time) // 1000
            print("You survived for", survival_time, "seconds.")
            plane.kill()
            game_over = True

        if hp > 0:
            healthimg.set_colorkey((255, 255, 255), pygame.RLEACCEL)
            screen.blit(healthimg, (SCREEN_WIDTH - 270, -70))



        survival_time = (pygame.time.get_ticks() - start_time) // 1000
        timer_text = game_font1.render("Time: " + str(survival_time) + " sec", True, (0, 0, 255))
        screen.blit(timer_text, (10,10))

    else: # if game_over == True:
        screen.fill((148, 227, 246))
        game_over_text = game_font1.render("GAME OVER", True, (255, 0, 0))
        survival_text = game_font1.render("You survived for: "+str(survival_time) + " seconds", True, (0,0,0))
        instructions_text = game_font1.render("Press R to play again, ESC to quit", True, (0,0,0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 250))
        screen.blit(survival_text, (SCREEN_WIDTH // 2 - survival_text.get_width() // 2, 330))
        screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, 410))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    plane = Player()
                    hp = 3
                    clouds.empty()
                    rockets.empty()
                    all_sprites.empty()
                    all_sprites.add(plane)
                    start_time = pygame.time.get_ticks() # reload timer
                    survival_time = 0
                    game_over = False


    pygame.display.flip()
    clock.tick(120)