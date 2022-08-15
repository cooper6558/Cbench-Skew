# Run from job list

from json import load
from argparse import ArgumentParser
from os import system


def main():
    parser = ArgumentParser(
        description="Run from job list"
    )
    parser.add_argument(
        "--jobs", type=str, required=True,
        help='json file from multi_stage module'
    )
    args = parser.parse_args()
    with open(args.jobs, 'r') as f:
        data = load(f)
    for key in data.keys():
        for job in data[key]:
            run_string = key
            for option in job:
                run_string += ' '+option
            system(run_string)


if __name__ == '__main__':
    main()
