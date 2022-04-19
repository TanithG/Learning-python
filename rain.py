import sys, pygame
from pygame.sprite import Sprite
from random import randint

class Drop(Sprite):
	"""Class that manages a single raindrop."""
	def __init__(self, rain_app):
		"""Initializes the assets."""
		super().__init__()
		self.screen = rain_app.screen
		self.image = pygame.image.load('drop.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height


class Rain:
	"""Class that manages a rainy background."""
	def __init__(self):
		pygame.init()

		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = 10, 10, 25

		self.screen = pygame.display.set_mode(
			(self.screen_width, self.screen_height)
			)
		pygame.display.set_caption('Rainy Day')

		self.drops = pygame.sprite.Group()
		self._create_rain()

	def run_game(self):
		while True:
			self._check_events()
			self.screen.fill(self.bg_color)
			self.drops.draw(self.screen)
			self._update_rain()
			self._delete_off_limits()
			self._check_rain()

			pygame.display.flip()

	def _check_events(self):
		"""Checks all events detected and acts accordingly."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_rain(self):
		"""Updates the position of the raindrops."""
		for drop in self.drops.sprites():
			drop.rect.y += 2		

	def _delete_off_limits(self):
		"""Deletes any raindrops that goes off-limits."""
		for drop in self.drops.copy():
			if drop.rect.bottom >= self.screen_height:
				self.drops.remove(drop)

	def _check_rain(self):
		"""If the amount of drops goes below a certain treshold, adds a new row."""
		# Checks if there is a row missing.
		if len(self.drops) <= ((self.number_drops_x * self.number_rows) - self.number_drops_x):
			self._create_new_row()	

	def _create_rain(self):
		"""Creates a rain grid."""
		drop = Drop(self)
		drop_width, drop_height = drop.rect.size
		available_space_x = self.screen_width - (2 * drop_width)
		self.number_drops_x = available_space_x // (2 * drop_width)
		available_space_y = self.screen_height - (2 * drop_height)
		self.number_rows = available_space_y // (2 * drop_height)

		for row_number in range(self.number_rows):
			for drop_number in range(self.number_drops_x):
				self._create_drop(drop_number, row_number)

	def _create_new_row(self):
		"""Creates a new row at the top of the screen."""
		drop = Drop(self)
		drop_width = drop.rect.width
		available_space_x = self.screen_width - (2 * drop_width)
		number_drops_x = available_space_x // (2 * drop_width)
		for drop_number in range(number_drops_x):
			self._create_drop(drop_number, 0)

	def _create_drop(self, drop_number, row_number):
		"""Creates a raindrop and adds it to the correct position."""
		drop = Drop(self)
		drop_width, drop_height = drop.rect.size
		drop.x = drop_width + 3 * drop_width * drop_number
		drop.rect.x = drop.x
		drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number
		# Randomize the position of the drop rectangle, to make it more realistic.
		drop.rect.x += randint(-25, 25)
		drop.rect.y += randint(-10, 30)
		self.drops.add(drop)


if __name__ == '__main__':
	r_a = Rain()
	r_a.run_game()