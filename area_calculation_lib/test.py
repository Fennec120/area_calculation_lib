import unittest


class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        from area_calculation_lib import area_calculator as ac
        self.triangle = ac()
        self.triangle.triangle_set_params(5,4,3)
        result = self.triangle.triangle_area()
        self.assertEqual(result, 6)



