# Plot histogram from numpy file

from matplotlib.pyplot import show, savefig
from seaborn import barplot
from argparse import ArgumentParser
from numpy import load


def plot(histogram, output):
    barplot(
        x=histogram[1].round(1),
        y=histogram[0],
        palette="Blues_d"
    )
    show()
    savefig(output+'.png')


def main():
    parser = ArgumentParser(
        description='Plot histogram from numpy file.'
    )
    parser.add_argument(
        '--input', type=str, required=True,
        help='input file name'
    )
    parser.add_argument(
        '--output', type=str, required=True,
        help='output image'
    )
    args = parser.parse_args()
    plot(load(args.input), args.output)


if __name__ == '__main__':
    main()
