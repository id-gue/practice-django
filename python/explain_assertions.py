# Assertions in Unit tests and integration tests

assert 2 == 2   # passes
assert 2 == 3   # fails

if assert 2 != 3:
    raise Exeption('fail')

assert == "make sure"

# AssertIs means the objects are identical
# AssertEqual means Values are the same

# very generally speaking:
# F - error in code or tests are to strict
# E - error in test


# code from ana
# assertions in unittests
import unittest

class A:
    pass

class B:
    pass

class TestMyCode(unittest.TestCase):

    def test_calculations(self):
        self.assertEqual(1, 1)
        #self.assertEqual(1, 2)
        self.assertNotEqual(1,2)
        self.assertTrue(True)
        #self.assertTrue(False)
        x = False # this is usually a result of a function call
        #self.assertTrue(x)
        #self.assertEqual(x, True) # equivalent to line 18
        x = 2
        self.assertIn(x, [1,2,3])
        #self.assertIn(x, [1,3])
        self.assertNotIn(x, [1,3])
        x = None
        self.assertIsNone(x)
        #self.assertIsNotNone(x)
        a = A()
        self.assertIsInstance(a, A)
        self.assertNotIsInstance(a, B)
        #self.assertIsInstance(a, B)


if __name__ == '__main__':
    unittest.main()