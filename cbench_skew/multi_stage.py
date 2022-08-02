# Multistage job scheduler

from argparse import ArgumentParser
from json import load, dump, dumps
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
        '--output', type=str, required=True,
        help='output job list'
    )
    args = parser.parse_args()
    with open(args.script, 'r') as f:
        data = load(f, parse_int=lambda x: x)

    arguments = [
        [combo for combo in product(*arg_dict.values())]
        for arg_dict in data['stages'].values()
    ]
    # hackish way to get ordered list of dict keys
    executables = [key for key in data['stages'].keys()]
    input_files = data['data']
    # `stage` is a string, `i` is an integer for each string
    # so iterate through stages
    output = {}
    for i, stage in enumerate(data['stages']):
        output[stage] = []
        print("Stage", i+1)
        output_files = []
        # iterate through argument combinations
        for combo in arguments[i]:
            # output[stage] = []
            # iterate through input files
            for j, input_file in enumerate(input_files):
                l = []
                arg_str_combo = arg_string(combo, data['stages'][stage])
                print(executables[i], '\\')
                print('\t--input', input_file, '\\')
                print('\t--output', input_file+'.'+arg_str_combo[1], '\\')
                # print(
                #     executables[i],
                #     '--input', input_file,
                #     '--output', input_file+'.'+arg_str_combo[1],
                #     arg_str_combo[0]
                # )
                l.append('--input '+input_file)
                l.append('--output '+input_file+'.'+arg_str_combo[1])

                output_files.append(input_file+'.'+arg_str_combo[1])
                # output[stage].append(
                #     [
                #         '--input ' + input_file,
                #         '--output ' + input_file + '.' + arg_str_combo[1]
                #     ]
                # )
                for arg in arg_str_combo[0][:-1]:
                    print('\t'+arg, '\\')
                    l.append(arg)
                print('\t'+arg_str_combo[0][-1])
                l.append(arg_str_combo[0][-1])
                # print(l)
                output[stage].append(l)
                # print(output[stage][j])
        input_files = output_files
        # print(outputs)

    # print(
    #     dumps(
    #         output, indent=4
    #     )
    # )
    # print(len(output["python -m cbench_skew.stage2"]))

    with open(args.output, 'w') as f:
        dump(output, f, indent=4)


if __name__ == '__main__':
    main()
