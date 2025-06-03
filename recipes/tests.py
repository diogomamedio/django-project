from django.test import TestCase


class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        """
        A simple test to ensure that pytest is set up correctly.
        """
        self.assertEqual(1, 1, "This should always pass.")
        print("pytest is working!")
