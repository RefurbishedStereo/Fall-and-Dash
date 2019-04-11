import pygame
import random

pygame.init()

screenWidth = 800
screenHeight = 700
screenColor = (150, 150, 0)
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("Fall and Dash Alpha Build")

class Button():
	def __init__(x, y, text, color, size):
		self.x = x
		self.y = y
		self.

class Game():
	def __init__(self):
		self.width = screenWidth
		self.height = screenHeight
		self.color = screenColor
		self.mouse = pygame.mouse.get_pos()
	def draw(self):
		True
game = Game()

class Player():
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.size = size
		self.vel = 0.05
		self.fric = 0.01
	def update(self):
		True
	def draw(self):
		True

class Bar():
	def __init__(self, x, y, vel, gvel, gx, gwid):
		self.x = x
		self.y = y
		self.vel = vel
		self.gvel = gvel
		self.gx = gx
		self.gwid = gwid
	def update(self):
		True
	def draw(self):
		True

class Turret():
	def __init__(self, x, y, rof, rot, size, angle):
		self.x = x
		self.y = y
		self.rof = rof
		self.rot = rot
		self.size = size
		self.angle = angle
	def fire(self, x, y, angle, vel, size):
		True
	def update(self):
		True
	def draw(self):
		True

class Bullet():
	def __init__(self, x, y, angle, vel, size):
		self.x = x
		self.y = y
		self.angle = angle
		self.vel = vel
		self.size = size
	def update(self):
		True
	def draw(self):
		True
def main():
	active = True
	clock = pygame.time.Clock()
	while active:
		clock.tick(60)
		screen.fill(game.color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				active = False
		
		pygame.display.update()
	pygame.quit()
	
if __name__ == "__main__":
	main()