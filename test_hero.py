import unittest
import hero
import weapon
import potion


class TestHero(unittest.TestCase):
    def setUp(self):
        self.h = hero.Hero("spiridon", 500, "megamaster")

    def test_hero_init(self):
        self.assertEqual("spiridon", self.h.name)
        self.assertEqual(500, self.h.health)
        self.assertEqual("megamaster", self.h.nickname)

    def test_hero_to_string(self):
        self.assertEqual("spiridon the megamaster:\n500/500 health\n10 damage",
                         str(self.h))

    def test_known_as(self):
        self.assertEqual("spiridon the megamaster", self.h.known_as())

    def test_get_health(self):
        self.assertEqual(self.h.health, self.h.get_health())

    def test_take_damage(self):
        self.h.take_damage(100)
        self.assertEqual(400, self.h.health)
        self.assertEqual("spiridon the megamaster:\n400/500 health\n10 damage",
                         str(self.h))

    def test_take_damage_with_more_damage_than_health(self):
        self.h.take_damage(600)
        self.assertEqual(0, self.h.health)

    def test_is_alive(self):
        self.assertTrue(self.h.is_alive())

    def test_is_alive_while_dead(self):
        self.h.take_damage(600)
        self.assertFalse(self.h.is_alive())

    def test_equip_weapon(self):
        w = weapon.Weapon('bow', 30, 1.0, 1)
        self.h.equip_weapon(w)
        self.assertEqual(w, self.h.weapon)

    def test_equip_weapon1(self):
        w = weapon.Weapon('bow', 30, 1.0, 1)
        self.h.equip_weapon(w)
        w2 = weapon.Weapon('dagger', 10, 1.0, 0)
        self.h.equip_weapon(w2)
        self.assertEqual(w, self.h.weapon)

    def test_has_weapon(self):
        w = weapon.Weapon('bow', 30, 1.0, 1)
        self.assertFalse(self.h.has_weapon())

        self.h.equip_weapon(w)
        self.assertTrue(self.h.has_weapon())

    def test_attack_without_weapon(self):
        self.assertEqual(self.h.damage, self.h.attack())

    def test_attack_with_weapon(self):
        w = weapon.Weapon('bow', 30, 1.0, 1)
        self.h.equip_weapon(w)
        self.assertEqual((self.h.damage + 30) * 2, self.h.attack())

    def test_take_healing(self):
        self.h.take_damage(100)
        potion_ = potion.Potion(50)
        result = self.h.take_healing(potion_)
        self.assertEqual(450, self.h.health)
        self.assertTrue(result)

    def test_take_healing_above_full_health(self):
        potion_ = potion.Potion(50)
        result = self.h.take_healing(potion_)
        self.h.take_healing(potion_)
        self.assertEqual(500, self.h.health)

    def test_take_healing_when_already_dead(self):
        self.h.take_damage(600)
        potion_ = potion.Potion(50)
        result = self.h.take_healing(potion_)
        result = self.h.take_healing(potion_)
        self.assertEqual(0, self.h.health)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
