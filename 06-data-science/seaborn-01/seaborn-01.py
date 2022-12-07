import os

import matplotlib.pyplot as plt
import seaborn as sns

folder = 'graphs'
sns.set(style="darkgrid")


def save_plot(name):
    if not os.path.exists(folder):
        os.makedirs(folder)
    plt.savefig(os.path.join(folder, name))


tips = sns.load_dataset("tips")
tips.head()


def example1():
    sns.relplot(x="total_bill", y="tip", data=tips);
    save_plot('example1.png')


def example2():
    sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);
    save_plot('example2.png')


def example3():
    sns.relplot(x="total_bill", y="tip", hue="smoker",
                style="smoker", data=tips);
    save_plot('example3.png')


def example4():
    sns.relplot(x="total_bill", y="tip",
                hue="smoker", style="time", data=tips);
    save_plot('example4.png')


def example5():
    sns.relplot(x="total_bill", y="tip", hue="size", data=tips);
    save_plot('example5.png')


def example6():
    sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75",
                data=tips);
    save_plot('example6.png')


def example7():
    sns.relplot(x="total_bill", y="tip", size="size", data=tips);
    save_plot('example7.png')


def example8():
    sns.relplot(x="total_bill", y="tip",
                size="size", sizes=(15, 200), data=tips);
    save_plot('example8.png')


def example9():
    sns.relplot(x="total_bill", y="tip", hue="smoker",
                col="time", data=tips);
    save_plot('example9.png')


def example10():
    tips = sns.load_dataset("tips")
    sns.catplot(x="day", y="total_bill", data=tips);
    save_plot('example10.png')


def example11():
    tips = sns.load_dataset("tips")
    sns.catplot(x="day", y="total_bill", jitter=False, data=tips);
    save_plot('example11.png')


def example12():
    sns.catplot(x="day", y="total_bill", kind="swarm", data=tips);
    save_plot('example12.png')


def example13():
    sns.catplot(x="day", y="total_bill",
                hue="sex", kind="swarm", data=tips);
    save_plot('example13.png')


def example14():
    sns.catplot(x="size", y="total_bill", kind="swarm",
                data=tips.query("size != 3"));
    save_plot('example14.png')


def example15():
    sns.catplot(x="smoker", y="tip", order=["No", "Yes"], data=tips);
    save_plot('example15.png')


def example16():
    sns.catplot(x="total_bill", y="day",
                hue="time", kind="swarm", data=tips);
    save_plot('example16.png')


def example17():
    sns.catplot(x="day", y="total_bill", kind="box", data=tips);
    save_plot('example17.png')


def example18():
    sns.catplot(x="day", y="total_bill",
                hue="smoker", kind="box", data=tips);
    save_plot('example18.png')


if __name__ == '__main__':
    example11()

