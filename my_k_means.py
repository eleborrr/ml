import random
import matplotlib.pyplot as plt

def my_k_means_lokti(points):
    wcss = []
    results = []

    min_x = min(points, key=lambda i: i[0])[0]
    max_x = max(points, key=lambda i: i[0])[0]
    min_y = min(points, key=lambda i: i[1])[1]
    max_y = max(points, key=lambda i: i[1])[1]
    for i in range(1, len(points)):
        centroids = fill_centroids(i, min_x, max_x, min_y, max_y)
        clusters = assign_to_cluster(centroids, points)
        stabilized = False
        while not stabilized:
            stabilized = True
            for cluster_indx in clusters.keys():
                new_cluster_center = calculate_center_of_cluster(clusters[cluster_indx])
                if new_cluster_center != centroids[cluster_indx]:
                    stabilized = False
                    centroids[cluster_indx] = new_cluster_center
            clusters = assign_to_cluster(centroids, points)

        distances = 0
        for key, val in clusters.items():
            distances += calculate_cluster_distances_to_center(val, centroids[key])

        wcss.append(distances)
        results.append(clusters)

    optimal_clusters = find_optimal_clusters(wcss)
    return results[optimal_clusters]

def my_k_means(points, clusters):
    min_x = min(points, key=lambda i: i[0])[0]
    max_x = max(points, key=lambda i: i[0])[0]
    min_y = min(points, key=lambda i: i[1])[1]
    max_y = max(points, key=lambda i: i[1])[1]

    centroids = fill_centroids(clusters, min_x, max_x, min_y, max_y)
    clusters = assign_to_cluster(centroids, points)
    stabilized = False
    while not stabilized:
        stabilized = True
        for cluster_indx in clusters.keys():
            new_cluster_center = calculate_center_of_cluster(clusters[cluster_indx])
            if new_cluster_center != centroids[cluster_indx]:
                stabilized = False
                centroids[cluster_indx] = new_cluster_center
        clusters = assign_to_cluster(centroids, points)

    return clusters

def find_optimal_clusters(wcss):
    differences = [wcss[i] - wcss[i + 1] for i in range(len(wcss) - 1)]
    
    optimal_index = differences.index(max(differences)) + 1 
    return optimal_index + 1 
        

def fill_centroids(i, min_x, max_x, min_y, max_y):
    centroids = []
    for j in range (i):
        centroids.append((random.uniform(min_x, max_x), random.uniform(min_y, max_y)))

    return centroids

def assign_to_cluster(centroids, points):
    clusters = {}
    for point in points:
        distances = [(calculate_distance(point, centroids[indx]), indx) for indx in range(len(centroids))]
        min_distance = min(distances, key=lambda i : i[0])
        cluster_num = min_distance[1]
        if(cluster_num in clusters):
            clusters[cluster_num].append(point)
        else:
            clusters[cluster_num] = [point]
    return clusters

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def calculate_center_of_cluster(cluster):
    total_x = 0
    total_y = 0
    count = len(cluster)

    for point in cluster:
        total_x += point[0]
        total_y += point[1]

    central_x = total_x / count
    central_y = total_y / count

    return (central_x, central_y)

def calculate_cluster_distances_to_center(cluster, center):
    result = 0
    for point in cluster:
        result += calculate_distance(point, center)
    return result