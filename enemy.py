import entity


class Enemy(entity.Entity):
    def __init__(self, health, damage):
        super().__init__(health, damage)

    def __str__(self):
        return "enemy:\n" + super().__str__()
