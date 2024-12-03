import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from my_k_means import my_k_means 

flowers = load_iris()

colors = {
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'pink',
    4: 'black',
    5: 'yellow',
    6: 'purple'
}

data = flowers["data"]

target = flowers.target

pl = [x[0] for x in data]
pw = [x[1] for x in data]
sl= [x[2] for x in data]
sw= [x[3] for x in data]

sets = [pl, pw, sl, sw]

fig, ax = plt.subplots(4, 4)

for i in range(4):
    for j in range(4):
        kmeans = my_k_means([(sets[i][s], sets[j][s]) for s in range(len(sets[i]))], 4)

        for cluster_id, points in kmeans.items():
            x_coords = [point[0] for point in points]
            y_coords = [point[1] for point in points]
            ax[i][j].scatter(x_coords, y_coords ,color=colors[cluster_id]) # scatter(data[:, i:i+1], data[:, j:j+1])


plt.show()


