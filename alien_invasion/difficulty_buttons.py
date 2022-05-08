import pygame.font

class Diff_Button:
	"""Class that manages difficulty buttons for Alien Invasion."""
	def __init__(self, ai_game):
		"""Initialize button attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.text_color = (255, 255, 255)

		self.font = pygame.font.SysFont(None, 48)
		self.easy_button()
		self.mid_button()
		self.hard_button()
		
	def easy_button(self):
		"""Create an easy settings button."""
		self.easy_button_color = (0, 255, 0)
		self.easy_image = self.font.render('Easy', True, 
			self.text_color, self.easy_button_color)
		self.easy_image_rect = self.easy_image.get_rect()
		self.easy_rect = pygame.Rect(0, 0, self.width, self.height)
		self.easy_rect.left = self.screen_rect.left + 40
		self.easy_rect.y = (self.screen_rect.height // 2) + 40
		self.easy_image_rect.center = self.easy_rect.center

	def draw_easy_button(self):
		"""Draws blank button and then draws the message."""
		self.screen.fill(self.easy_button_color, self.easy_rect)
		self.screen.blit(self.easy_image, self.easy_image_rect)

	def mid_button(self):
		"""Create an easy settings button."""
		self.mid_button_color = (255, 230, 70)
		self.mid_image = self.font.render('Normal', True, 
			self.text_color, self.mid_button_color)
		self.mid_image_rect = self.mid_image.get_rect()
		self.mid_rect = pygame.Rect(0, 0, self.width, self.height)
		self.mid_rect.center = self.screen_rect.center
		self.mid_rect.y = (self.screen_rect.height // 2) + 40
		self.mid_image_rect.center = self.mid_rect.center

	def draw_mid_button(self):
		"""Draws blank button and then draws the message."""
		self.screen.fill(self.mid_button_color, self.mid_rect)
		self.screen.blit(self.mid_image, self.mid_image_rect)

	def hard_button(self):
		"""Create an easy settings button."""
		self.hard_button_color = (255, 0, 0)
		self.hard_image = self.font.render('Hard', True, 
			self.text_color, self.hard_button_color)
		self.hard_image_rect = self.hard_image.get_rect()
		self.hard_rect = pygame.Rect(0, 0, self.width, self.height)
		self.hard_rect.right = self.screen_rect.width - 40
		self.hard_rect.y = (self.screen_rect.height // 2) + 40
		self.hard_image_rect.center = self.hard_rect.center

	def draw_hard_button(self):
		"""Draws blank button and then draws the message."""
		self.screen.fill(self.hard_button_color, self.hard_rect)
		self.screen.blit(self.hard_image, self.hard_image_rect)