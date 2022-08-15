# Multistage job scheduler

from argparse import ArgumentParser
from json import load, dump
from os.path import split, join
from itertools import product


def arg_string(combo, arg_dict):
    return [
        key + ' ' + combo[i]
        for i, key in enumerate(arg_dict.keys())
    ], ''.join(combo)


def main():
    parser = ArgumentParser(
        description="Multistage job scheduler."
    )
    parser.add_argument(
        '--script', type=str, required=True,
        help='multistage job script'
    )
    parser.add_argument(
        '--cbench', type=str, required=True,
        help='CBench input json file'
    )
    args = parser.parse_args()
    with open(args.script, 'r') as f:
        data = load(f, parse_int=lambda x: x)
    with open(args.cbench, 'r') as f:
        cbench = load(f)
    input_files = [
        compressor['output-prefix'] + '__' + split(
            cbench['input']['filename']
        )[-1]
        for compressor in cbench['data-reduction']['cbench-compressors']
    ]

    arguments = [
        [combo for combo in product(*arg_dict['args'].values())]
        for arg_dict in data['stages'].values()
    ]
    # hackish way to get ordered list of dict keys
    executables = [key for key in data['stages'].keys()]

    # `stage` is a string, `i` is an integer for each string
    # so iterate through stages
    output = {}
    for i, stage in enumerate(data['stages']):
        output[stage] = []
        print("Stage", i+1)
        output_files = []
        # iterate through argument combinations
        for combo in arguments[i]:
            # iterate through input files
            for j, input_file in enumerate(input_files):
                arg_list = []
                arg_str_combo = arg_string(
                    combo, data['stages'][stage]['args']
                )
                print(executables[i], '\\')
                print('\t--input', input_file, '\\')
                print('\t--output', input_file+'.'+arg_str_combo[1], '\\')
                arg_list.append('--input '+input_file)
                arg_list.append('--output '+input_file+'.'+arg_str_combo[1])

                output_files.append(input_file+'.'+arg_str_combo[1])
                for arg in arg_str_combo[0][:-1]:
                    print('\t'+arg, '\\')
                    arg_list.append(arg)
                print('\t'+arg_str_combo[0][-1])
                arg_list.append(arg_str_combo[0][-1])
                output[stage].append(arg_list)
        input_files = output_files

    with open(join(data['outdir'], data['output']), 'w') as f:
        dump(output, f, indent=4)


if __name__ == '__main__':
    main()
