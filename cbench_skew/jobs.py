from json import load, dump
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(
        description='Generate json job script from list of arguments.'
    )
    parser.add_argument(
        '--script', type=str, required=True,
        help='script file name'
    )
    parser.add_argument(
        '--output', type=str, required=True,
        help='output file name'
    )
    args = parser.parse_args()
    with open(args.script, 'r') as f:
        script = load(f)

    jobs = []
    for input_name in script['inputs']:
        for arg in script['args']:
            jobs.append({
                'exe': script['exe'],
                '--input': input_name,
                'args': arg
            })

    with open(args.output, 'w') as f:
        dump(jobs, f, indent=4)


if __name__ == '__main__':
    main()
