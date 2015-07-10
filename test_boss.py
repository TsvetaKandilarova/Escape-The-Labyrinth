import unittest
import boss


class TestBoss(unittest.TestCase):
    def setUp(self):
        self.b = boss.Boss(1200, 150, (2, 1.5))
        self.b2 = boss.Boss(1000, 150, (2, 1.5))

    def test_boss_init(self):
        self.assertEqual(1200, self.b.health)
        self.assertEqual(150, self.b.damage)
        self.assertEqual((2, 1.5), self.b.berserk_tuple)
        self.assertEqual(2, self.b.attacks_till_berserk)

    def test_boss_to_string(self):
        self.assertEqual(
            "big enemy:\n1200/1200 health\n150 damage\n2/150% berserk",
            str(self.b))

    def test_boss_to_string2(self):
        self.assertEqual(
            "big enemy:\n1000/1200 health\n150 damage\n2/150% berserk",
            self.b.__str__())

    def test_take_damage(self):
        self.b.take_damage(100)
        self.assertEqual(1100, self.b.health)

    def test_take_damage_with_more_damage_than_health(self):
        self.b.take_damage(1300)
        self.assertEqual(0, self.b.health)

    def test_is_alive(self):
        self.assertTrue(self.b.is_alive())

    def test_is_alive_while_dead(self):
        self.b.take_damage(1200)
        self.assertFalse(self.b.is_alive())

    def test_attack(self):
        self.assertEqual(150, self.b.attack())

    def test_second_attack(self):
        self.b.attack()
        self.assertEqual(225, self.b.attack())

    def test_third_attack(self):
        self.b.attack()
        self.b.attack()
        self.assertEqual(150, self.b.attack())


if __name__ == '__main__':
    unittest.main()
