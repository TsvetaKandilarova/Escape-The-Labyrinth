import unittest
import potion


class TestPotion(unittest.TestCase):
    def setUp(self):
        self.p = potion.Potion(100)
        self.p2 = potion.Potion(50)

    def test_potion_init(self):
        self.assertEqual(100, self.p.healing_points)

    def test_potion_init2(self):
        self.assertEqual(50, self.p2.healing_points)

    def test_potion_to_string(self):
        self.assertEqual("healing potion: 100 hp", str(self.p))

    def test_get_healing_points(self):
        self.assertEqual(p.get_healing_points(), 100)


if __name__ == '__main__':
    unittest.main()
