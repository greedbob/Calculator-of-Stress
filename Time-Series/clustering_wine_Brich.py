import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster as cluster
import sklearn.metrics as metrics
import sklearn as sk
from clustering import *


def get_score(data, method):
    score = dict()
    # score['n_clusters'] = max(method.labels_)+1
    score['silhouette_score'] = metrics.silhouette_score(data, method.labels_)
    score['calinski_harabaz_score'] = metrics.calinski_harabaz_score(data, method.labels_)
    return score


def select_n_clusters(data, data_pca, n_clusters_range):
    scores = []
    for n in n_clusters_range:
        birch = cluster.Birch(n_clusters=n).fit(data_pca)
        score = get_score(data, birch)
        scores.append(score)
    for i, score_function in enumerate(['silhouette_score', 'calinski_harabaz_score']):
        plt.subplot(1, 2, i+1)
        plt.title(score_function)
        plt.plot(n_clusters_range, [item[score_function] for item in scores])
    plt.show()


def main():
    data_origin = read_data('wine.data')
    data_converted = convert_data(data_origin, 0)
    true_labels = data_converted.iloc[:, 0]
    data_clean = clean_data(data_converted.iloc[:, 1:])

    scaler = sk.preprocessing.StandardScaler().fit(data_clean)
    data_standard = scaler.transform(data_clean)

    pca_components = 4
    pca = sk.decomposition.PCA(n_components=pca_components)
    pca.fit(data_standard)
    data_pca = pca.fit_transform(data_standard)

    n_clusters_range = range(2, 10, 1)
    select_n_clusters(data_clean, data_pca, n_clusters_range)
    return 0


if __name__ == '__main__':
    main()
