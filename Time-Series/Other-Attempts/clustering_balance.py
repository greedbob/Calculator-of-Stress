import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster as cluster
import sklearn as sk


def read_data(data_name):
    data = pd.read_csv(data_name, sep=',', header=None)
    return data


def clean_data(data):
    index_need_drop = []
    for index, row in data.iterrows():
        for num in list(row):
            if np.isnan(num):
                index_need_drop.append(index)
                break
    data_clean = data.drop(index_need_drop)
    return data_clean


def convert_data(data, dimension_convert):
    data_converted = data.copy()
    situation_list = []
    for i, item in enumerate(list(data_converted.iloc[:, dimension_convert])):
        if item not in situation_list:
            situation_list.append(item)
        data_converted.iloc[i, dimension_convert] = situation_list.index(item)
    return data_converted


def plot_distribution(data):
    if isinstance(data, np.ndarray):
        data_array = data
    elif isinstance(data, pd.DataFrame):
        data_array = np.array(data)
    else:
        raise TypeError
    for i in range(len(data_array[0])):
        plt.subplot(1, len(data_array[0]), i+1)
        sns.distplot(data_array[:, i])
    plt.show()


def pca(dimension, data):
    meandata = np.mean(data)
    features = data - meandata
    cov = np.cov(features.transpose())
    eigVals, eigVectors = np.linalg.eig(cov)
    pca_mat = eigVectors[:, :dimension]
    data_pca = np.dot(features, pca_mat)
    return data_pca


def evaluation(method, pca_data, true_lables, pred_lables):
    score = dict()
    # ARI: adjusted Rand index
    score['ARI'] = sk.metrics.adjusted_rand_score(true_lables, pred_lables)
    score['homo'] = sk.metrics.homogeneity_score(true_lables, pred_lables)
    score['comp'] = sk.metrics.completeness_score(true_lables, pred_lables)

    return score


def show_labels_different(true_labels_, predict_labels):
    for i in range(len(true_labels_)):
        print('#1: {0}, #2: {1}'.format(true_labels_[i], predict_labels[i]))


def show_result(data_clean, data_pca, true_labels, method, n_clusters, dimension_show):
    predict_labels = method.labels_
    labels = []
    color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    markers = [".", "v", "^", "<", ">", "s", "*"]
    for i in range(n_clusters):
        labels.append(data_clean[predict_labels == i])
        plt.scatter(labels[i].iloc[:, dimension_show[0]], labels[i].iloc[:, dimension_show[1]],
                    c=color[i], marker=markers[i], label='label' + str(i))
    plt.xlabel('label {0}'.format(dimension_show[0]))
    plt.ylabel('label {0}'.format(dimension_show[1]))
    plt.legend(loc=2)
    plt.show()
    # show_labels_different(true_labels, kmeans.labels_)
    score = evaluation(true_labels, method.labels_)
    print('The score of method {} is:\n{}'.format(method, score))


def main():
    data_origin = read_data('balance-scale.data')
    data_converted = convert_data(data_origin, 0)
    true_labels = data_converted.iloc[:, 0]
    data_clean = clean_data(data_converted.iloc[:, 1:])
    plot_distribution(data_clean)

    dimension = 2
    data_pca = pca(dimension, data_clean)
    plot_distribution(data_pca)

    n_clusters = 3
    dimension_show = [1, 2]

    kmeans = cluster.KMeans(n_clusters=n_clusters).fit(data_clean)
    show_result(data_clean, data_pca, true_labels, kmeans, n_clusters, dimension_show)

    dbscan = cluster.DBSCAN(eps=0.38, min_samples=10).fit(data_clean)
    show_result(data_clean, data_pca, true_labels, dbscan, n_clusters, dimension_show)
    return 0


if __name__ == '__main__':
    main()
