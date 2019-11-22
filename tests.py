import unittest
try:
    from lcpy import none, true, false, exception
except ImportError:
    raise OSError("Failed to import the library.")


class Tests(unittest.TestCase):
    def test_values(self):
        self.assertEqual(none, None)

    def test_bools(self):
        self.assertTrue(true, True)
        self.assertFalse(false, False)

    def test_exception(self):
        with self.assertRaises(Exception):
            raise exception("This should be properly thrown!")


if __name__ == '__main__':
    unittest.main()
