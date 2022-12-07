import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

folder = 'graphs'


def save_graph(name):
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.exists(folder + '/' + name + '.png'):
        plt.savefig(folder + '/' + name + '.png')
    else:
        print('File already exists')


def example1():
    df = pd.DataFrame({'x_data': range(1, 11),
                       'y_data': np.random.randn(10)})

    plt.plot('x_data', 'y_data', data=df)
    save_graph('example1')


def example2():
    df = pd.DataFrame({'x_data': range(1, 11),
                       'y_data': np.random.randn(10)})

    plt.plot('x_data', 'y_data', data=df, color='skyblue', linestyle=':',
             linewidth=4)
    save_graph('example2')


def example3():
    data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
    names = list(data.keys())
    values = list(data.values())
    plt.bar(names, values)
    save_graph('example3')


def example4():
    data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
    names = list(data.keys())
    values = list(data.values())
    plt.barh(names, values)
    save_graph('example4')


def example5():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width)
    p2 = plt.bar(ind, womenMeans, width, bottom=menMeans)

    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))

    save_graph('example5')


def example6():
    np.random.seed(19680801)

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)

    plt.scatter(x, y)
    save_graph('example6')


def example7():
    np.random.seed(19680801)

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)

    plt.scatter(x, y, c=colors, alpha=0.5)
    save_graph('example7')


def example8():
    np.random.seed(19680801)

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    save_graph('example8')


def example9():
    n_bins = 10
    x = np.random.randn(1000)

    plt.hist(x, n_bins)
    save_graph('example9')


def example10():
    n_bins = 10
    x = np.random.randn(1000, 3)

    plt.hist(x, n_bins)
    save_graph('example10')


if __name__ == '__main__':
    example10()
