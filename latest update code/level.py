import pygame 
from settings import *
from tile import Tile
from player import Player


class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = CameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		#this is to check the row and helps to coordinates the pos.y
		for row_index,row in enumerate(WORLD_MAP):
			#check each of the column elements (x,p or empty) and helps to coordinate pos.x
			for col_index, col in enumerate(row):
				#multiply the col and row with the size of our tile so that it can fit
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					#check the pos of column and row and group it under the visible_sprites
					#since the rock will have collision with the player, so we also put it under obstacle_sprites
					Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
				

	def run(self):
		# update and draw the game(display)
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()

#function as camera 
class CameraGroup (pygame.sprite.Group):
  def __init__ (self): 
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.half_w =  self.display_surface.get_size()[0] //2
    self.half_h =  self.display_surface.get_size()[1] //2
    self.offset = pygame.math.Vector2()

  def custom_draw(self, player): 
		#getting the offset 
    self.offset.x = player.rect.centerx - self.half_w
    self.offset.y = player.rect.centery - self.half_h

    for sprite in self.sprites(): 
      offset_pos = sprite.rect.topleft - self.offset 
      self.display_surface.blit (sprite.image, offset_pos)