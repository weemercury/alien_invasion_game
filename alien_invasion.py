import sys 

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
        # Назначение цвета фона.
        # self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживаем события клавиатуры и мыши через метод _check_events
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши.""" 
        # Отслеживаем события клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # переместить корабль вправо
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
    
    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.settings.bg_color)
        # Отрисовка корабля.
        self.ship.blitme()       
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
            
            
if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai_game = AlienInvasion()
    ai_game.run_game()