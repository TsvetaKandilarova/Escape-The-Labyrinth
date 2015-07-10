import unittest

import weapon


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.w = weapon.Weapon('bow', 30, 1.0, 1)
        self.w2 = weapon.Weapon('bow', 30, 2.0, 1)

    def test_weapon_init(self):
        self.assertEqual('bow', self.w.type)
        self.assertEqual(30, self.w.damage)
        self.assertEqual(1.0, self.w.critical_strike_percent)
        self.assertEqual(1, self.w.tier)

    def test_weapon_init2(self):
        self.assertEqual('bow', self.w2.type)
        self.assertEqual(30, self.w2.damage)
        self.assertEqual(0.0, self.w2.critical_strike_percent)
        self.assertEqual(1, self.w2.tier)

    def test_weapon_init_with_incorrect_argument(self):
        self.assertEqual(0.0, self.w2.critical_strike_percent)

    def test_weapon_to_string(self):
        self.assertEqual('bow\n30 damage\n100% critical strike percent',
                         str(self.w))

    def test_critical_hit(self):
        self.assertTrue(self.w.critical_hit())
        self.assertFalse(self.w2.critical_hit())


if __name__ == '__main__':
    unittest.main()
