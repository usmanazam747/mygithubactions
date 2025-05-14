import unittest

# -------------------------------
# Simple Utility Functions
# -------------------------------

def are_strings_equal(a, b):
    """
    Returns True if two strings are equal, False otherwise.
    """
    return a == b

def are_bools_equal(a, b):
    """
    Returns True if two boolean values are equal, False otherwise.
    """
    return a == b

# -------------------------------
# Calculations Class
# -------------------------------

class Calculations:
    """
    A simple class for basic arithmetic operations.
    """
    def __init__(self, a, b):
        """
        Initialize with two numbers.
        """
        self.a = a
        self.b = b

    def get_sum(self):
        """
        Return the sum of a and b.
        """
        return self.a + self.b

    def get_difference(self):
        """
        Return the difference of a and b.
        """
        return self.a - self.b

    def get_product(self):
        """
        Return the product of a and b.
        """
        return self.a * self.b

    def get_quotient(self):
        """
        Return the quotient of a divided by b.
        Raises ZeroDivisionError if b is zero.
        """
        return self.a / self.b

# -------------------------------
# Unit Tests
# -------------------------------

class TestSimpleFunctions(unittest.TestCase):
    """
    Unit tests for simple utility functions.
    """
    def test_string_equality(self):
        """
        Test that two identical strings are equal.
        """
        self.assertTrue(are_strings_equal('some', 'some'))

    def test_boolean_equality(self):
        """
        Test that two identical boolean values are equal.
        """
        self.assertTrue(are_bools_equal(True, True))

class TestCalculations(unittest.TestCase):
    """
    Unit tests for the Calculations class.
    """
    def setUp(self):
        """
        Set up a Calculations instance for testing.
        """
        self.calc = Calculations(8, 2)

    def test_sum(self):
        """
        Test the sum method.
        """
        self.assertEqual(self.calc.get_sum(), 10, 'The sum is incorrect.')

    def test_difference(self):
        """
        Test the difference method.
        """
        self.assertEqual(self.calc.get_difference(), 6, 'The difference is incorrect.')

    def test_product(self):
        """
        Test the product method.
        """
        self.assertEqual(self.calc.get_product(), 16, 'The product is incorrect.')

    def test_quotient(self):
        """
        Test the quotient method.
        """
        self.assertEqual(self.calc.get_quotient(), 4, 'The quotient is incorrect.')

    def test_zero_division(self):
        """
        Test that dividing by zero raises a ZeroDivisionError.
        """
        calc = Calculations(8, 0)
        with self.assertRaises(ZeroDivisionError):
            calc.get_quotient()

class TestStringMethods(unittest.TestCase):
    """
    Unit tests for Python's built-in string methods.
    """
    def test_upper(self):
        """
        Test the upper() method of strings.
        """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """
        Test the isupper() method of strings.
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """
        Test the split() method of strings.
        """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Test that passing a non-string separator raises a TypeError
        with self.assertRaises(TypeError):
            s.split(2)

# -------------------------------
# Main Block to Run Tests
# -------------------------------

if __name__ == '__main__':
    unittest.main()
