from ex30 import get_option, get_morph
from ex35 import get_freq
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import japanize_matplotlib


def plot_graph(path, freq):
    fig = plt.figure()

    freq = [t[1] for t in freq]
    rank = [n for n in range(1, len(freq)+1)]

    plt.scatter(rank, freq)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('順位')
    plt.ylabel('頻度')
    
    fig.savefig(path)


def main():
    args = get_option()

    sentences = get_morph(args.corpus)

    freq = get_freq(sentences)

    plot_graph(args.result, freq)


if __name__ == '__main__':
    main()
