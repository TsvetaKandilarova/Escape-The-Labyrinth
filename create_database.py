import sqlite3


def create_heroes_table(cursor):
    create_query = '''create table if not exists
        heroes(name text,
              max_health int,
              nickname text,
              damage DOUBLE )'''

    cursor.execute(create_query)

def create_weapons_table(cursor):
    create_query = '''create table if not exists
        weapons(type text,
              damage int,
              critical_chance double,
              tier int)'''

    cursor.execute(create_query)


def insert_hero_into_table(cursor, name, max_health, nickname, damage):
    insert_query = "insert into heroes values(?, ?, ?, ?)"
    cursor.execute(insert_query, (name, max_health, nickname, damage))


def insert_weapon_into_table(cursor, type_, damage, critical_chance, tier):
    insert_query = "insert into weapons values(?, ?, ?, ?)"
    cursor.execute(insert_query, (type_, damage, critical_chance, tier))


def create():
    conn = sqlite3.connect("labyrinth.db")
    cursor = conn.cursor()

    _weapons = {("dagger", 10, 0.0, 1),
                ("staff", 30, 0.25, 2),
                ("bow", 20, 0.80, 2),
                ("rapier", 25, 0.50, 2),
                ("elder rod", 30, 0.50, 3),
                ("snaken bow", 30, 1.00, 3),
                ("long sword", 35, 0.75, 3)}

    _heroes = [("sharik", 400, "pythonslayer", 40),
               ("arya", 380, "shadow princess", 40),
               ("chuck", 1000, "great norris", 50)]

    create_heroes_table(cursor)
    create_weapons_table(cursor)

    for _ in _heroes:
        insert_hero_into_table(cursor, *_)

    for _ in _weapons:
        insert_weapon_into_table(cursor, *_)
    conn.commit()
    conn.close()
