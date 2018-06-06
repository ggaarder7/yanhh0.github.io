import pandas
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

IRIS_FILENAME = 'iris-dataset.csv'
COLOURS, MARKERS = 'bgbrycmk', 'op*<>^1234shH+xDd|_'

if __name__ == '__main__':
    iris_dat = pandas.read_csv(IRIS_FILENAME,
                               names=['v1', 'v2', 'v3', 'v4',
                                      'label'],
                               index_col=False)
    types = iris_dat['label'].unique()
    iris_by_types = {t: iris_dat.loc[iris_dat['label'] == t]
                     for t in types}
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for (t, dat), c, m in zip(iris_by_types.items(),
                              COLOURS, MARKERS):
        ax.scatter(dat['v1'], dat['v2'], dat['v3'],
                   label=t, c=c, marker=m)

    ax.legend()
    ax.set_xlabel('v1 Label')
    ax.set_ylabel('v2 Label')
    ax.set_zlabel('v3 Label')

    plt.show()
    
