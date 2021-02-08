import ast
import functools
import re


def all_coords_within_grid(coords: list, max_x: int, max_y: int) -> bool:
    return functools.reduce(
        lambda prev_res, next_res: prev_res and next_res[0] <= max_x and next_res[1] <= max_y,
        coords,
        True
    )


def parse_input_data(user_input: str) -> dict:
    grid_width, grid_height = re.match(r'\d+x\d+', user_input).group(0).split('x')
    coords_substring = re.sub(r'\d+x\d+', '', user_input)
    coords = [
        ast.literal_eval(coord_pair_str.group(0))
        for coord_pair_str in re.finditer(r'\((\d+),\s*(\d+)\)', coords_substring)
    ]

    return {
        'max_x': int(grid_width) - 1,
        'max_y': int(grid_height) - 1,
        'coords': coords
    }
