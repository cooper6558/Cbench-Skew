# Plot histogram from numpy file

from matplotlib.pyplot import show
from seaborn import barplot
from argparse import ArgumentParser
from numpy import load


def plot(histogram):
    barplot(
        x=histogram[1].round(1),
        y=histogram[0],
        palette="Blues_d"
    )
    show()


def main():
    parser = ArgumentParser(
        description='Plot histogram from numpy file.'
    )
    parser.add_argument(
        '--input', type=str, required=True,
        help='input file name'
    )
    args = parser.parse_args()
    plot(load(args.input))


if __name__ == '__main__':
    main()
