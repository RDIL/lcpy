try:
    from lcpy import none, true, false
except ImportError:
    raise OSError("Failed to import the library.")


class Tests(unittest.TestCase):
    def test_values(self):
        self.assertEqual(none, None)
        
    def test_bools(self):
        self.assertTrue(true, True)
        self.assertFalse(false, False)


if __name__ == '__main__':
    unittest.main()
