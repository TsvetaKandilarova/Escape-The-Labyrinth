_base_health = 100
_base_attack_damage = 10


class Entity:
    def __init__(self, health=_base_health, damage=_base_attack_damage):
        self.damage = damage

        if health <= 0:
            self.health = _base_health
        else:
            self.health = health

        self.max_health = self.health

    def __str__(self):
        return "%d/%d health\n%d damage" \
               % (self.health, self.max_health, self.damage)

    def get_health(self):
        return self.health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self):
        return self.damage

    def is_alive(self):
        return self.health > 0