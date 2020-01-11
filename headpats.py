#!/usr/bin/python
import pygame,math
from pygame.constants import *
import argparse
import time

class Game(object):
	def __init__(self, background_image, hand_image, fullscreen, pats_per_second, pat_amplitude, pat_x, pat_y, framerate):
		background_surf = pygame.image.load(background_image)
		pygame.init()
		pygame.display.set_caption('HEADPATS.EXE')
		flags=0
		if fullscreen:
			flags|=FULLSCREEN
		self.screen=pygame.display.set_mode(background_surf.get_size(),flags)
		self.bg=background_surf.convert()
		self.hand=pygame.image.load(hand_image).convert_alpha()
		self.hand_y=0
		self.clock=pygame.time.Clock()
		self.start_time=time.time()
		self.pats_per_second=pats_per_second
		self.pat_amplitude=pat_amplitude
		self.pat_y=pat_y
		self.pat_x=pat_x
		self.framerate=framerate
	def draw(self):
		screen = self.screen
		screen.blit(self.bg, (0,0))
		screen.blit(self.hand, (self.pat_x,self.hand_y))
		pygame.display.flip()
	def update(self):
		time_offset = time.time()-self.start_time
		self.hand_y = self.pat_y + self.pat_amplitude * math.sin(time_offset*math.pi*self.pats_per_second)
	def main_loop(self):
		self.running=True
		while self.running:
			self.update()
			self.draw()
			if self.framerate > 0:
				self.clock.tick(self.framerate)
			for event in pygame.event.get():
				if event.type==QUIT:
					self.running=False
				elif event.type==KEYUP:
					if event.key==K_ESCAPE:
						self.running=False

if __name__=='__main__':
	parser=argparse.ArgumentParser(description='Dispense headpats')
	parser.add_argument('--background-image', default='bg.jpg', help='set the path for the background image to use')
	parser.add_argument('--hand-image', default='hand.png', help='set the path for the hand image to use')
	parser.add_argument('-f', '--fullscreen', default=False, action='store_true', help='start fullscreen')
	parser.add_argument('--pats-per-second', default=2, type=float, help='set pat frequency')
	parser.add_argument('--pat-amplitude', default=30, type=int, help='set pat amplitude')
	parser.add_argument('-x', '--pat-x', default=160, type=int, help='set horizontal pat position')
	parser.add_argument('-y', '--pat-y', default=-40, type=int, help='set vertical pat position')
	parser.add_argument('--framerate', default=60, type=int, help='set the frame rate limit. 0 or lower disables the frame rate limit.')

	args=parser.parse_args()

	Game(
		background_image=args.background_image,
		hand_image=args.hand_image,
		fullscreen=args.fullscreen,
		pats_per_second=args.pats_per_second,
		pat_amplitude=args.pat_amplitude,
		pat_x=args.pat_x,
		pat_y=args.pat_y,
		framerate=args.framerate
	).main_loop()
