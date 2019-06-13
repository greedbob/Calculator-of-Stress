import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster as cluster
import sklearn.metrics as metrics
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


def plot_distribution(data, size, title='distribution'):
    if isinstance(data, np.ndarray):
        data_array = data
    elif isinstance(data, pd.DataFrame):
        data_array = np.array(data)
    else:
        raise TypeError
    for i in range(len(data_array[0])):
        plt.subplot(size[0], size[1], i+1)
        sns.distplot(data_array[:, i])
    plt.suptitle(title)
    plt.show()


def evaluation(true_labels, pred_labels):
    score = dict()
    score['AMI'] = metrics.adjusted_mutual_info_score(true_labels, pred_labels)
    score['ARI'] = metrics.adjusted_rand_score(true_labels, pred_labels)
    score['homo'] = metrics.homogeneity_score(true_labels, pred_labels)
    score['comp'] = metrics.completeness_score(true_labels, pred_labels)
    return score


def show_labels_different(true_labels_, predict_labels):
    for i in range(len(true_labels_)):
        print('#1: {0}, #2: {1}'.format(true_labels_[i], predict_labels[i]))


def show_scatter(title, df, method, n):
    color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    markers = [".", "v", "^", "<", ">", "s", "*"]
    for i in range(n):
        temp = df[method.labels_ == i]
        plt.scatter(temp[df.columns[0]], temp[df.columns[1]], c=color[i], marker=markers[i], label='label' + str(i))
    plt.title(title)
    plt.legend()
    plt.show()


def show_result(data_clean, data_pca, true_labels, method, n_clusters, dimension_show):
    tsne = sk.manifold.TSNE(learning_rate=100)
    tsne.fit_transform(data_pca)
    df_tsne = pd.DataFrame(tsne.embedding_)
    show_scatter('scatter of TSNE', df_tsne, method, n_clusters)

    df_show = data_clean.iloc[:, dimension_show]
    df_show.columns = [0, 1]
    show_scatter('scatter of dimension {}'.format(dimension_show), df_show, method, n_clusters)

    score = evaluation(true_labels, method.labels_)
    print('The score of method {} is:\n{}'.format(method, score))
    return score


def compare_scores(scores):
    df = pd.DataFrame(zip(scores['kmeans'].values(), scores['ap'].values(), scores['dbscan'].values(), scores['birch'].values()),
                      columns=['KMeans', 'AffinityPropagation', 'DBSCAN', 'Birch'], index=['AMI', 'ARI', 'homo', 'comp'])
    df.plot.bar()
    plt.show()


def main():
    data_origin = read_data('wine.data')
    data_converted = convert_data(data_origin, 0)
    true_labels = data_converted.iloc[:, 0]
    data_clean = clean_data(data_converted.iloc[:, 1:])
    plot_distribution(data_clean, size=[4, 4], title='data_clean distribution')

    scaler = sk.preprocessing.StandardScaler().fit(data_clean)
    data_standard = scaler.transform(data_clean)
    plot_distribution(data_standard, size=[4, 4], title='data_standard distribution')

    pca_components = 4
    pca = sk.decomposition.PCA(n_components=pca_components)
    pca.fit(data_standard)
    print('The sum of explained_variance_ratio_ is": ', sum(pca.explained_variance_ratio_))
    data_pca = pca.fit_transform(data_standard)
    plot_distribution(data_pca, size=[1, pca_components], title='data_pca distribution')
    plt.scatter(data_pca[:, 0], data_pca[:, 1])
    plt.show()

    n_clusters = 3
    dimension_show = [0, 1]
    scores = dict()
    kmeans = cluster.KMeans(n_clusters=n_clusters).fit(data_pca)
    scores['kmeans'] = show_result(data_clean, data_pca, true_labels, kmeans, n_clusters, dimension_show)

    ap = cluster.AffinityPropagation(preference=-200).fit(data_pca)
    scores['ap'] = show_result(data_clean, data_pca, true_labels, ap, max(ap.labels_)+1, dimension_show)

    dbscan = cluster.DBSCAN(eps=1.35, min_samples=10).fit(data_pca)
    scores['dbscan'] = show_result(data_clean, data_pca, true_labels, dbscan, n_clusters, dimension_show)

    birch = cluster.Birch(n_clusters=3).fit(data_pca)
    scores['birch'] = show_result(data_clean, data_pca, true_labels, birch, n_clusters, dimension_show)

    compare_scores(scores)
    return 0


if __name__ == '__main__':
    main()
