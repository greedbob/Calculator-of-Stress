import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster as cluster
import sklearn as sk


data = pd.read_csv('glass.data', header=None, names=['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type'])
data_glass = data[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
print(data_glass)


index_need_drop = []
for index, row in data.iterrows():
    for num in list(row):
        if np.isnan(num):
            index_need_drop.append(index)
            break
data_clean = data_glass.drop(index_need_drop)
print(data_clean)


for i, col in enumerate(list(data_clean.columns)):
    plt.subplot(2, 4, i+1)
    sns.distplot(data_clean[col],)
plt.show()


dimension = 2
meandata = np.mean(data_clean)
features = data_clean - meandata
# features = (data_glass - np.min(data_glass)) / (np.max(data_glass) - np.min(data_glass))
cov = np.cov(features.transpose())
eigVals, eigVectors = np.linalg.eig(cov)
pca_mat = eigVectors[:, :dimension]
pca_data = np.dot(features, pca_mat)
for j in range(dimension):
    plt.subplot(1, dimension, j+1)
    sns.distplot(pca_data[:, j],)
plt.show()




# pca_data = pd.DataFrame(pca_data, columns=['pca1', 'pca2'])
# fig = plt.figure(figsize=(16, 9))
# plt.subplot(111)
# plt.scatter(pca_data['pca1'], pca_data['pca2'])
# plt.xlabel('pca_1')
# plt.ylabel('pca_2')
# plt.show()

# pca_data = data_iris_selected
def evaluation(method, pca_data, true_lables, pred_lables):
    score = dict()
    score['silhouette'] = sk.metrics.silhouette_score(pca_data, method)
    score['homo'] = sk.metrics.homogeneity_score(true_lables, pred_lables)
    score['comp'] = sk.metrics.completeness_score(true_lables, pred_lables)
    # ARI: adjusted Rand index
    score['ARI'] = sk.metrics.adjusted_rand_score(true_lables, pred_lables)
    # AMI: adjusted mutual information
    # score['AMI'] = sk.metrics.adjusted_mutual_info_score(true_lables, pred_lables)
    return score


true_lables = data['Type']
kmeans = cluster.KMeans(n_clusters=7).fit(pca_data)
pred_lables_kmeans = kmeans.labels_
kmeans_score = evaluation(kmeans, pca_data, true_lables, pred_lables_kmeans)
print('kmeans_score is: ', kmeans_score)


# DBSCAN
dbscan = cluster.DBSCAN(eps=3, min_samples=5).fit(pca_data)
pred_lables_dbscan = dbscan.labels_
dbscan_score = evaluation(dbscan, pca_data, true_lables, pred_lables_dbscan)
print('DBSCAN score is: ', dbscan_score)


birch = cluster.Birch(n_clusters=None).fit(pca_data)
pred_lables_birch = birch.labels_
birch_score = evaluation(birch, pca_data, true_lables, pred_lables_birch)
print('Birch score is: ', birch_score)


# for i in range(len(true_lables)):
#     print('#1: {0}, #2: {1}'.format(true_lables[i], pred_lables_birch[i]))
