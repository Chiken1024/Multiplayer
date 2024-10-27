import pygame

class sprite():
  def __init__(self, x, y, width, height, rotation, image):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.rotation = rotation
    self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(image), (width, height)), rotation)

class bullet():
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color