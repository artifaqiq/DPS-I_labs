from sklearn.cluster import KMeans


def k_means(data, n_clusters=4):
    stat_array = [[v['area'], v['perimeter'], v['compact']] for k, v in data.iteritems()]

    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(stat_array).labels_

    return kmeans
