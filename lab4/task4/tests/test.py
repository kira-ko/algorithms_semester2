import unittest
from lab4.task4.src.main import compute_hashes, get_hash, preprocess_powers


class TestSubstringEquality(unittest.TestCase):
    def setUp(self):
        self.s = "trololo"
        self.x = 31
        self.m1, self.m2 = 10 ** 9 + 7, 10 ** 9 + 9
        self.h1 = compute_hashes(self.s, self.x, self.m1)
        self.h2 = compute_hashes(self.s, self.x, self.m2)
        self.x_pow1 = preprocess_powers(self.x, len(self.s), self.m1)
        self.x_pow2 = preprocess_powers(self.x, len(self.s), self.m2)

    def test_equal_substrings(self):
        self.assertEqual(get_hash(self.h1, 0, 7, self.x_pow1, self.m1), get_hash(self.h1, 0, 7, self.x_pow1, self.m1))
        self.assertEqual(get_hash(self.h2, 0, 7, self.x_pow2, self.m2), get_hash(self.h2, 0, 7, self.x_pow2, self.m2))

        self.assertEqual(get_hash(self.h1, 2, 3, self.x_pow1, self.m1), get_hash(self.h1, 4, 3, self.x_pow1, self.m1))
        self.assertEqual(get_hash(self.h2, 2, 3, self.x_pow2, self.m2), get_hash(self.h2, 4, 3, self.x_pow2, self.m2))

    def test_unequal_substrings(self):
        self.assertNotEqual(get_hash(self.h1, 1, 2, self.x_pow1, self.m1),
                            get_hash(self.h1, 3, 2, self.x_pow1, self.m1))
        self.assertNotEqual(get_hash(self.h2, 1, 2, self.x_pow2, self.m2),
                            get_hash(self.h2, 3, 2, self.x_pow2, self.m2))


if __name__ == "__main__":
    unittest.main()