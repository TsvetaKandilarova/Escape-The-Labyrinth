import sqlite3
import create_database
from hero import Hero


class DatabaseManager:
    def __init__(self, db_name="labyrinth.db"):
        self.name = db_name
        self.conn = sqlite3.connect(db_name)

    @staticmethod
    def create_database():
        create_database.create()

    def get_weapons_by_tier(self):
        c = self.conn.cursor()
        weapons = c.execute('''SELECT * FROM weapons''').fetchall()
        return weapons

    def get_heroes(self):
        c = self.conn.cursor()
        return [Hero(*i) for i in
                c.execute('''SELECT * FROM heroes''').fetchall()]

    def get_heroes_by_name(self):
        heroes = self.get_heroes()
        return {hero.name: hero for hero in heroes}

    def get_weapons_type(self):
        c = self.conn.cursor()
        return [_[0] for _ in
                c.execute('''SELECT type FROM weapons''').fetchall()]

    def get_weapons(self):
        c = self.conn.cursor()
        return {weapon[0]: (weapon[1], weapon[2]) for weapon in c.execute(
            '''SELECT type,damage,critical_chance FROM weapons''').fetchall()}
