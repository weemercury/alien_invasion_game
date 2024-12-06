class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует статические настройки игры."""
        
        # Настройки экрана
        self.screen_width = 1280
        self.screen_height = 720
        # self.bg_color = (230, 230, 230)
        self.bg_color = (154, 170, 198)
        
        # Настройки корабля
        self.ship_limit = 0
        
        # Параметры снарядов
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
        
        # Настройки пришельцев.
        self.fleet_drop_speed = 100
        
        # Темп ускорения игры
        self.speedup_scale = 1.1
        
        # Темп роста очков за сбитого пришельца
        self.score_scale = 2
        
        self._initialize_dynamic_settings()
        
    def _initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 1.0
        
        # fleet_direction = 1 - движение вправо; а -1 - влево
        self.fleet_direction = 1
        
        # Подсчет очков
        self.alien_points = 10
        
    def increase_speed(self):
        """
        Увеличивает настройки скорости и кол-во очков за подбитых пришельцев.
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)        