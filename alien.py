import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляющий одного пришельца."""
    
    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        
        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien_2.bmp')
        self.rect = self.image.get_rect()
        
        # Каждый новый пришелец появляется в верхнем левом углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Сохренение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)