# Launch jobs from json script
from json import load
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(
        description='Launch jobs from json script.'
    )
    parser.add_argument(
        '--script', type=str, required=True,
        help='script file name'
    )
    args = parser.parse_args()
    with open(args.script) as f:
        script = load(f)['jobs']
    for job in script:
        print(job['name'])
        print(job['exe'], '\\')
        if 'output' in job:
            print('\t--output', job['output'], '\\')
        if 'args' in job:
            print('\t' + job['args'])
        print('\t--input', job['input'], '\n')


if __name__ == '__main__':
    main()
