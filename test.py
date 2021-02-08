import unittest
from argparse import ArgumentTypeError
from path_search import move_to_point, build_route
from pizzabot import grid_arg
from utils import all_coords_within_grid


class RoteBuilderTestCase(unittest.TestCase):
    def test_move_to_point__returns_proper_route(self):
        self.assertEqual(move_to_point((0, 0), (2, 2)), 'EENN')

    def test_move_to_point_back__returns_proper_directions(self):
        self.assertEqual(move_to_point((2, 2), (0, 0)), 'WWSS')

    def test_build_route__drops_pizza_twice_if_point_is_duplicated(self):
        user_data = '5x5(1,1)(1,1)(2,2)'
        self.assertEqual(build_route(user_data), 'ENDDEND')

    def test_build_route__raises_if_target_point_is_out_of_grid(self):
        with self.assertRaises(ArgumentTypeError):
            user_data = '5x5(1,1)(1,1)(5,5)'
            build_route(user_data)


class UtilsTestCase(unittest.TestCase):
    def test_all_coords_withing_grid__returns_true_for_correct_input(self):
        coords = [(0, 0), (1, 3), (4, 4), (4, 2), (4, 2), (0, 1), (3, 2), (2, 3), (4, 1)]
        max_x = 5
        max_y = 5
        self.assertTrue(all_coords_within_grid(coords, max_x, max_y))

    def test_grid_arg_validator__returns_user_input_if_correct(self):
        user_input = '5x5(0,0)(1,3)(4,4)(4,2)(4,2)(0,1)(3,2)(2,3)(4,1)'
        self.assertEqual(grid_arg(user_input), user_input)

    def test_grid_arg_validator__raises_if_user_input_is_incorrect(self):
        with self.assertRaises(ArgumentTypeError):
            user_input = '55(0,0)(1,3)(4,4)(4,2)(4,2)(0,1)(3,2)(2,3)(4,1)'
            grid_arg(user_input)


if __name__ == '__main__':
    unittest.main()
