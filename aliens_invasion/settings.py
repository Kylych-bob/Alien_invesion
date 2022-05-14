class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (230, 230, 220)

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (170, 0, 0)
        self.bullets_allowed = 3

        # Скорость корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1



