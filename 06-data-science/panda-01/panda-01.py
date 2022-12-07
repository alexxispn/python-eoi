import numpy as np
import pandas as pd


def ejemplo_1():
    mylist = list('abcedfghijklmnopqrstuvwxyz')
    myarr = np.arange(26)
    mydict = dict(zip(mylist, myarr))

    print(pd.Series(mylist), pd.Series(myarr), pd.Series(mydict))


def ejemplo_2():
    mylist = list('abcedfghijklmnopqrstuvwxyz')
    myarr = np.arange(26)
    mydict = dict(zip(mylist, myarr))
    ser = pd.Series(mydict)

    print(pd.DataFrame(ser).reset_index())


def ejemplo_3():
    ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
    ser2 = pd.Series(np.arange(26))
    df = pd.concat([ser1, ser2], axis=1)
    print(df.head(10))


def ejemplo_4():
    ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
    print(ser.diff().tolist())
    print(ser.diff().diff().tolist())


def ejemplo_5():
    url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
    df = pd.read_csv(url, usecols=['crim', 'medv'])
    print(df.head())


def ejemplo_6_1():
    url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
    df = pd.read_csv(url)
    print(df.loc[df['Price'].idxmax(), ['Manufacturer', 'Model', 'Type']])


def ejemplo_6_2():
    url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
    df = pd.read_csv(url)
    row, col = np.where(df.values == np.max(df['Price']))
    print(row, col)


if __name__ == '__main__':
    ejemplo_6_2()
