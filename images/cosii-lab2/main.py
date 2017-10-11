import json

from cars import processing
from processing import kmeans

if __name__ == '__main__':

    history = processing.mark('./resources/car-types.jpeg')
    for i in range(len(history)):
        history[i].save('./resources/history/car-types.{}.jpeg'.format(i))

    mrk_image = history[-1]

    mrk_image.save('./resources/car-types.mrk.jpeg', 'JPEG', quality=100)

    stat = processing.geom_stat(mrk_image)
    stat = {k: v for k, v in stat.iteritems() if v['area'] >= 250}

    clusters = kmeans.k_means(stat, n_clusters=6)

    i = 0
    for k in stat.keys():
        stat[k]['cluster'] = clusters[i] + 1
        i += 1

    print json.dumps(stat, indent=2, separators=(',', ': '))

    processing.colour_by_clusters(mrk_image, stat, 6).save('./resources/car-types.clst.jpeg', 'JPEG', quality=100)
