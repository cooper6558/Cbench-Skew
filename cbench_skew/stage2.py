# Plot histogram from numpy file
# Example script to run with job scheduler as stage 2

from matplotlib.pyplot import savefig
from seaborn import barplot
from argparse import ArgumentParser
from numpy import load


def plot(histogram, output, color):
    barplot(
        x=histogram[1].round(1),
        y=histogram[0],
        palette=color
    )
    savefig(output, format='png')


def main():
    parser = ArgumentParser(
        description='Plot histogram from numpy file.'
    )
    parser.add_argument(
        '--input', type=str, required=True,
        help='input file name'
    )
    parser.add_argument(
        '--color', type=str, required=True,
        help='plot color palette'
    )
    parser.add_argument(
        '--output', type=str, required=True,
        help='output image'
    )
    args = parser.parse_args()
    plot(load(args.input), args.output, args.color)


if __name__ == '__main__':
    main()
