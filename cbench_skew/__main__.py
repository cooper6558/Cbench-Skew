# Compute and plot histogram for Cbench hdf5 output files

from . stage1 import hist
from . stage2 import plot
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(
        description='Compute and plot histogram for Cbench hdf5 output files.'
    )
    parser.add_argument(
        '--input', type=str, required=True,
        help='input file name'
    )
    parser.add_argument(
        '--dataset', type=str, required=True,
        help='input dataset name'
    )
    parser.add_argument(
        '--bins', type=int, required=True,
        help='number of histogram bins to compute'
    )
    args = parser.parse_args()
    plot(hist(args.input, args.dataset, args.bins))


if __name__ == '__main__':
    main()
