import unittest

import enemy


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.e = enemy.Enemy(800, 100)

    def test_enemy_init(self):
        self.assertEqual(800, self.e.health)
        self.assertEqual(100, self.e.damage)

    def test_enemy_to_string(self):
        self.assertEqual("enemy:\n800/800 health\n100 damage", str(self.e))

    def test_take_damage(self):
        self.e.take_damage(100)
        self.assertEqual(700, self.e.health)

    def test_take_damage_with_more_damage_than_health(self):
        self.e.take_damage(900)
        self.assertEqual(0, self.e.health)

    def test_is_alive(self):
        self.assertTrue(self.e.is_alive())

    def test_is_alive_while_dead(self):
        self.e.take_damage(900)
        self.assertFalse(self.e.is_alive())


if __name__ == '__main__':
    unittest.main()
