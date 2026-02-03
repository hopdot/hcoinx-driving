
import pygame
import random
import sys
from hcx_reward import reward_player

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HCoinX Drive Web3")

clock = pygame.time.Clock()
car = pygame.Rect(380, 500, 40, 60)
speed = 6
obstacles = []
score = 0
font = pygame.font.SysFont(None, 36)

def spawn_obstacle():
    x = random.randint(0, WIDTH-40)
    obstacles.append(pygame.Rect(x, -60, 40, 60))

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 900)

running = True
while running:
    screen.fill((30,30,30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_EVENT:
            spawn_obstacle()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.left > 0:
        car.x -= speed
    if keys[pygame.K_RIGHT] and car.right < WIDTH:
        car.x += speed

    for obs in obstacles[:]:
        obs.y += 5
        if obs.colliderect(car):
            player_wallet = input("Enter wallet for HCX reward: ")
            reward_player(player_wallet, 5)
            running = False
        if obs.top > HEIGHT:
            obstacles.remove(obs)
            score += 1

    pygame.draw.rect(screen, (0,200,255), car)
    for obs in obstacles:
        pygame.draw.rect(screen, (200,50,50), obs)

    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
