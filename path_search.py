import argparse
import math

from utils import parse_input_data, all_coords_within_grid


def build_route(user_input: str) -> str:
    current_point = (0, 0)
    data = parse_input_data(user_input)
    route = ''

    if not all_coords_within_grid(data['coords'], max_x=data['max_x'], max_y=data['max_y']):
        raise argparse.ArgumentTypeError('Some of the coords are out of grid')

    while len(data['coords']):
        nearest_point_idx = get_nearest_coord_idx(current_point, data['coords'])
        route += drop_pizza(move_to_point(current_point, data['coords'][nearest_point_idx]))
        current_point = data['coords'][nearest_point_idx]
        data['coords'].pop(nearest_point_idx)

    return route


def get_nearest_coord_idx(current_point: tuple, remaining_points: list) -> int:
    min_distance = math.inf
    nearest_coord_idx = None

    for idx in range(len(remaining_points)):
        distance_to_coord = calculate_distance(current_point, remaining_points[idx])
        if distance_to_coord < min_distance:
            min_distance = distance_to_coord
            nearest_coord_idx = idx

    return nearest_coord_idx


def calculate_distance(start_coord: tuple, end_coord: tuple) -> float:
    return math.sqrt((end_coord[0] - start_coord[0]) ** 2 + (end_coord[1] - start_coord[1]) ** 2)


def move_to_point(start_coord: tuple, end_coord: tuple) -> str:
    x_axis_travel = end_coord[0] - start_coord[0]
    y_axis_travel = end_coord[1] - start_coord[1]
    x_axis_direction = ''
    y_axis_direction = ''
    if x_axis_travel > 0:
        x_axis_direction = 'E'
    elif x_axis_travel < 0:
        x_axis_direction = 'W'

    if y_axis_travel > 0:
        y_axis_direction = 'N'
    elif y_axis_travel < 0:
        y_axis_direction = 'S'

    return x_axis_direction * abs(x_axis_travel) + y_axis_direction * abs(y_axis_travel)


def drop_pizza(passed_route: str) -> str:
    return '{}D'.format(passed_route)
