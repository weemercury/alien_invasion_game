class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 1280
        self.screen_height = 720
        # self.bg_color = (230, 230, 230)
        self.bg_color = (154, 170, 198)
        
        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Параметры снарядов
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
        
        # Настройки пришельцев.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction = 1 - движение вправо; а -1 - влево
        self.fleet_direction = 1