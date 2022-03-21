"""
Employee class tests.
"""
import unittest

from pruebatecnicahabi import property


class TestSearchProperties(unittest.TestCase):
    """Test the search properties method of the property class."""

    def setUp(self):
        """Set up test fixtures."""

    def test_search_properties_returns_a_list(self):
        """Whether search properties returns a float."""
        self.assertIsInstance(property.search_properties(), list)

    def test_properties_amount(self):
        """whether get the right amount of properties without filter"""
        self.assertEqual(len(property.search_properties()), 55)

    def test_properties_with_state_filter_amount(self):
        """whether get the right amount of properties with status filter filter."""
        self.assertEqual(len(property.search_properties(status=3)), 35)

    def test_properties_with_year_filter_amount(self):
        """whether get the right amount of properties with status filter filter."""
        self.assertEqual(len(property.search_properties(year=2011)), 4)

    def test_properties_with_city_filter_amount(self):
        """whether get the right amount of properties with city filter filter."""
        self.assertEqual(len(property.search_properties(city='bogota')), 8)

    def test_properties_with_many_filters_amount(self):
        """whether get the right amount of properties with city filter filter."""
        self.assertEqual(len(property.search_properties(
            city='bogota', year=2011, status=4)), 1)


if __name__ == "__main__":
    unittest.main()
