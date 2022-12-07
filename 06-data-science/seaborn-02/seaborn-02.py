import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

folder = 'graphs'

sns.set(style="darkgrid")

titanic = sns.load_dataset("titanic")
titanic.head()


def save_plot(name):
    if not os.path.exists(folder):
        os.makedirs(folder)
    plt.savefig(os.path.join(folder, name))


def example1():
    sns.catplot(x="survived", kind="count", palette="ch:.25", data=titanic)
    save_plot('example1.png')


def example2():
    sns.catplot(x="pclass", hue="survived", kind="count", palette="pastel",
                edgecolor=".6", data=titanic)
    save_plot('example2.png')


def example3():
    sns.catplot(x="sex", hue="survived", kind="count", palette="pastel",
                edgecolor=".6", data=titanic)
    save_plot('example3.png')


def example4():
    sns.catplot(x="embarked", hue="survived", kind="count", palette="pastel",
                edgecolor=".6", data=titanic)
    save_plot('example4.png')


def example5():
    sns.catplot(x="sibsp", hue="survived", kind="count", palette="pastel",
                edgecolor=".6", data=titanic)
    save_plot('example5.png')


def example6():
    titanic['age'] = pd.cut(titanic['age'], [0, 10, 20, 30, 40, 50, 80])
    sns.catplot(x="age", hue="survived", kind="count", palette="pastel",
                edgecolor=".6", data=titanic)
    save_plot('example6.png')


def example7():
    titanic['fare'] = pd.cut(titanic['fare'], [0, 10, 20, 30, 40, 50, 80])
    g = sns.FacetGrid(titanic, col="survived", row="fare")
    g.map(plt.hist, "age")
    save_plot('example7.png')


def example8():
    sns.catplot(x="pclass", y="age", hue="sex", kind="swarm", data=titanic)
    save_plot('example8.png')


def example9():
    sns.jointplot(x="fare", y="age", data=titanic)
    save_plot('example9.png')


def example10():
    sns.distplot(titanic['fare'], bins=10)
    save_plot('example10.png')


def example11():
    sns.boxplot(x="pclass", y="age", data=titanic)
    save_plot('example11.png')


def example12():
    sns.swarmplot(x="pclass", y="age", data=titanic)
    save_plot('example12.png')


def example13():
    sns.countplot(x="sex", data=titanic)
    save_plot('example13.png')


def example14():
    sns.heatmap(titanic.corr(), annot=True)
    save_plot('example14.png')


if __name__ == '__main__':
    example14()
