# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from constants import *


def main():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	clock = pygame.time.Clock()
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
		
		screen.fill("black")
		dt = clock.tick(60) / 1000
		pygame.display.flip()
		

	
	

if __name__ == "__main__":
	main()


