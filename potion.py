class Potion:
    def __init__(self, healing_points):
        self.healing_points = healing_points

    def __str__(self):
        return "healing potion: %d hp" % self.healing_points

    def get_healing_points(self):
        return self.healing_points
