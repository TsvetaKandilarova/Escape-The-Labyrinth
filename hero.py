import entity

# just in case
_base_attack_damage = 10


class Hero(entity.Entity):
    # class Hero's constructor and to-string methods
    def __init__(self, name, health, nickname, damage=_base_attack_damage):
        super().__init__(health, damage)
        self.max_health = health
        self.name = name
        self.nickname = nickname
        self.weapon = None

    def __str__(self):
        return "%s:\n%s" % (self.known_as(), super().__str__())

    def known_as(self):
        return "%s the %s"%(self.name, self.nickname)

    # returns True if hero is equipped with a weapon
    def has_weapon(self):
        return self.weapon is not None

    def equip_weapon(self, weapon):
        if self.has_weapon() and self.weapon.tier <= weapon.tier or \
                not self.has_weapon():
            self.weapon = weapon

    # returns the damage that hero does,
    # true damage plus weapon damage,
    # which gets doubled if crits
    def attack(self):
        damage = super().attack()

        if self.has_weapon():
            damage += self.weapon.damage
            if self.weapon.critical_hit():
                damage *= 2
        return damage

    # get health points back.
    # health points can't go above max_health
    def take_healing(self, healing_potion):
        if not self.is_alive():
            return False

        self.health += healing_potion.healing_points
        if self.health > self.max_health:
            self.health = self.max_health
        return True
