import pygame
from classes import *
pygame.font.init()
display = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Multiplayer Rocket Thing")

healthText = pygame.font.SysFont("Comicsans", 32, 1)
winText = pygame.font.SysFont("Comicsans", 64, 1)

fps = 240
velocity = 0.2
bulletVelocity = 0.5
maxBullets = 3
rocket1Health = 10
rocket2Health = 10

redBullets = []
yellowBullets = []

spaceBackground = sprite(0, 0, pygame.display.get_window_size()[0], pygame.display.get_window_size()[1], 0, "Multiplayer/Assets/SpaceBG.png")
rocket1 = sprite(pygame.display.get_window_size()[0] * 0.25, pygame.display.get_window_size()[1] / 2, 48, 48, 90, "Multiplayer/Assets/Rocket1.png")
rocket2 = sprite(pygame.display.get_window_size()[0] * 0.75, pygame.display.get_window_size()[1] / 2, 48, 48, 270, "Multiplayer/Assets/Rocket2.png")


def correctRocketPosition(rocket, x1, y1, x2, y2):
  if rocket.x < x1: rocket.x = x1
  elif rocket.x > x2 - rocket.width: rocket.x = x2 - rocket.width
  if rocket.y < y1: rocket.y = y1
  elif rocket.y > y2 - rocket.height: rocket.y = y2 - rocket.height

def renderBullets():
  for i in redBullets: pygame.draw.rect(display, i.color, (i.x, i.y, 4, 4))
  for i in yellowBullets: pygame.draw.rect(display, i.color, (i.x, i.y, 4, 4))

def shoot(rocket):
  if rocket == rocket1:
    redBullets.append(bullet)
    bullet.x, bullet.y, bullet.color = rocket.x + 48, rocket.y + 24, "#ff4444"
  if rocket == rocket2:
    yellowBullets.append(bullet)
    bullet.x, bullet.y, bullet.color = rocket.x, rocket.y + 24, "#ffff44"

def moveBullets():
  for i in redBullets: i.x += bulletVelocity
  for i in yellowBullets: i.x -= bulletVelocity


while 1:
  correctRocketPosition(rocket1, 8, 8, pygame.display.get_window_size()[0] / 2 - 8, pygame.display.get_window_size()[1] - 8)
  correctRocketPosition(rocket2, pygame.display.get_window_size()[0] / 2 + 8, 8, pygame.display.get_window_size()[0] - 8, pygame.display.get_window_size()[1] - 8)


  moveBullets()
  
  
  display.blit(spaceBackground.image, (spaceBackground.x, spaceBackground.y))
  pygame.draw.rect(display, "#111166", (pygame.display.get_window_size()[0] / 2 - 8, 0, 16, pygame.display.get_window_size()[1]))
  renderBullets()
  display.blit(rocket1.image, (rocket1.x, rocket1.y))
  display.blit(rocket2.image, (rocket2.x, rocket2.y))
  display.blit(healthText.render("Health: " + str(rocket1Health), 1, "#000000"), (8, 12))
  display.blit(healthText.render("Health: " + str(rocket2Health), 1, "#000000"), (pygame.display.get_window_size()[0] - 185, 12))
  display.blit(healthText.render("Health: " + str(rocket1Health), 1, "#884444"), (8, 8))
  display.blit(healthText.render("Health: " + str(rocket2Health), 1, "#bbbb88"), (pygame.display.get_window_size()[0] - 185, 8))
  

  if pygame.key.get_pressed()[pygame.K_w]: rocket1.y -= velocity
  if pygame.key.get_pressed()[pygame.K_a]: rocket1.x -= velocity
  if pygame.key.get_pressed()[pygame.K_s]: rocket1.y += velocity
  if pygame.key.get_pressed()[pygame.K_d]: rocket1.x += velocity
  
  if pygame.key.get_pressed()[pygame.K_o]: rocket2.y -= velocity
  if pygame.key.get_pressed()[pygame.K_k]: rocket2.x -= velocity
  if pygame.key.get_pressed()[pygame.K_l]: rocket2.y += velocity
  if pygame.key.get_pressed()[pygame.K_SEMICOLON]: rocket2.x += velocity

  
  pygame.display.update()


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LSHIFT: shoot(rocket1)
      if event.key == pygame.K_SPACE: shoot(rocket2)
    
    if event.type == pygame.QUIT: pygame.quit()