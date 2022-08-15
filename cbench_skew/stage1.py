# Compute histogram for Cbench hdf5 output files
# Example script to run with job scheduler as stage 1

from numpy import histogram, vstack, save
from h5py import File
from argparse import ArgumentParser


def hist(input_file, dataset, num_bins, bounds=None):
    with File(input_file, 'r') as f:
        data = histogram(f[dataset], bins=num_bins, range=bounds)
        center = (data[1][:-1] + data[1][1:]) / 2
        return vstack((data[0], center))


def main():
    parser = ArgumentParser(
        description='Compute histogram for Cbench hdf5 output files.'
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
    parser.add_argument(
        '--output', type=str, required=True,
        help='output file name'
    )
    args = parser.parse_args()
    with open(args.output, 'wb') as f:
        save(f, hist(args.input, args.dataset, args.bins))


if __name__ == '__main__':
    main()
