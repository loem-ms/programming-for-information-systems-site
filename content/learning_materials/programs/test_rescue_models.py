import unittest
from rescue_models import OfferLine


class OfferLineTests(unittest.TestCase):
    def test_instances_keep_separate_state(self):
        first, second = OfferLine("D1", 3, 4), OfferLine("D1", 3, 1)
        first.containers = 2
        self.assertEqual(first.total_portions(), 6)
        self.assertEqual(second.total_portions(), 3)

    def test_zero_is_allowed_for_planning(self):
        self.assertEqual(OfferLine("D1", 3, 0).total_portions(), 0)

    def test_invalid_creation(self):
        for args in [(" ", 3, 1), ("D1", -1, 1), ("D1", 3, -1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                OfferLine(*args)

    def test_booleans_are_not_counts(self):
        with self.assertRaises(ValueError):
            OfferLine("D1", 3, True)


if __name__ == "__main__":
    unittest.main()
