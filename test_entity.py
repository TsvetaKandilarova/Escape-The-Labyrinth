import unittest
import entity


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.e = entity.Entity(500)

    def test_entity_init(self):
        self.assertEqual(500, self.e.health)
        self.assertEqual(500, self.e.max_health)
        self.assertEqual(entity._base_attack_damage, self.e.damage)

    def test_entity_to_string(self):
        self.assertEqual(
            "500/500 health\n%d damage" % entity._base_attack_damage,
            str(self.e))

    def test_entity_init_with_invalid_argument(self):
        e2 = entity.Entity(-100)
        self.assertEqual(entity._base_health, e2.health)

    def test_get_health(self):
        self.assertEqual(self.e.health, self.e.get_health())

    def test_take_damage(self):
        self.e.take_damage(100)
        self.assertEqual(400, self.e.health)
        self.assertEqual(500, self.e.max_health)

    def test_take_damage_with_more_damage_than_health(self):
        self.e.take_damage(600)
        self.assertEqual(0, self.e.health)

    def test_is_alive(self):
        self.assertTrue(self.e.is_alive())

    def test_is_alive_while_dead(self):
        self.e.take_damage(600)
        self.assertFalse(self.e.is_alive())

    def test_attack(self):
        self.assertEqual(self.e.damage, self.e.attack())


if __name__ == '__main__':
    unittest.main()
