class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 1280
        self.screen_height = 720
        # self.bg_color = (230, 230, 230)
        self.bg_color = (37, 40, 80)
        
        # Настройки корабля
        self.ship_speed = 1.5
        
        # Параметры снарядов
        self.bullet_speed = 1 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        