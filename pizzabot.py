import argparse
import re

from path_search import build_route


def grid_arg(user_input: str) -> str:
    if not re.match(r'^\d+x\d+(\(\d+,\d+\))+$', user_input):
        raise argparse.ArgumentTypeError('Invalid input format')

    return user_input


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('user_input', type=grid_arg)
    args = parser.parse_args()

    print(build_route(args.user_input))
