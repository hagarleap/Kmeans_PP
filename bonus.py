import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

def main():
    iris = datasets.load_iris()

    X =[k for k in range(1,11)]
    inertias=[]

    for k in range (1,11):
        model = KMeans(n_clusters=k, init='k-means++', random_state=0)
        model.fit(iris.data)
        inertias.append(model.inertia_)

    Y = np.array(inertias)
    plt.plot(X, Y)
    plt.xlabel('k value')
    plt.ylabel('inertias')
    r=15
    plt.plot(X[1],Y[1], marker='o', color='black', ls='dashed', ms=r, mfc='none')
    plt.annotate('Elbow Point', xy=(2, 154.34), xytext=(3.5, 300),
                arrowprops=dict(facecolor='black', shrink=0.005),
                )
    plt.title('Elbow Method for selection of optimal "K" clusters')
    #plt.show()
    plt.savefig('elbow.png')

if __name__=="__main__":
    main()
