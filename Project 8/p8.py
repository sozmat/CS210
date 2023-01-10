import random
import math
import csv
import matplotlib.pyplot as plt

def load_numerical_data(filename: str, column_titles: list) -> dict:
    """Load data from a CSV file and return a dictionary with keys being the
    row number and values as tuples of the data in each row, converted to float.
    Args:
        filename: The name of the CSV file to load.
        column_titles: A list of columns to load. v  
    Returns:
        A dictionary where each element corresponds to a data point, with keys 
        corresponding to the row number and values as a tuple of floats.
    Example:
        If column_titles = ['Col1', 'Col3'], and the CSV file has the following data:
            Col1, Col2, Col3
             2.4,  5.6,  7.8
            10.0, 42.5, -3.2
            31.4,  0.5, 12.3
        Then the return dictionary will be:
            {0: (2.4, 7.8), 1: (10, -3.2), 2: (31.4, 12.3)}
    """
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file)
        titles = next(reader) # read and skip column names
        print(titles)
        data = {}
        index = 0
        first_tuple = titles.index(column_titles[0])
        second_tuple = titles.index(column_titles[1])
        for row in reader:
            data[index] = (float(row[first_tuple]), float(row[second_tuple]))
            
               
            index += 1
    print(data)    
    return data


def euclid_dist(point1: tuple, point2: tuple) -> float:
    """Compute the Eucledian distance between two points represented as tuples.
    Listing 7.1 in PPC, with modifications for compliance to PEP8

    Args:
        point1: A tuple representing a point in n-dimensional space.
        point2: A tuple representing a point in n-dimensional space.

    Returns:
        float: The Euclidean distance between the two points.

    Example:
        euclid_dist((1, 2.5), (2.1, 4)) should return 1.86 (approximately).

    >>> euclid_dist((1, 2.5), (2.1, 4))
    1.86
    """
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff
    euclid_dist = math.sqrt(total)
    return round(euclid_dist, 2)

def create_centroids(k: int, data: dict) -> list:
    """Create k centroids by picking random points from the data until 
    you have k unique centroids.
 
    Args:
        k: The number of centroids to create.
        data: A dictionary where each element corresponds to a data point, with keys
            corresponding to the row number and values as tuples of floats.
 
    Returns:
        list: a list of centroids, each centroid is a tuple of floats.
    """
    centroids = []
    centroid_count = 0
    centroid_keys = []  # list of unique keys
 
    while centroid_count < k:
        r_key = random.randint(1, len(data))
        if r_key not in centroid_keys:  # if the key hasn't already been selected
            centroids.append(data[r_key])   # add to centroids
            centroid_keys.append(r_key) # add key to selected keys
            centroid_count = centroid_count + 1
 
    return centroids
 
 
def create_clusters(k: int, centroids: list, data: dict, repeats=100) -> list:
    """Create clusters using the k-means algorithm
    From Listing 7.8, modified to comply with PEP8
    Args:
        k:
        centroids:
        values: list of tuples
        repeats:
 
    Returns:
        dict: a list of clusters
    """
    for a_pass in range(repeats):
        print('****PASS', a_pass + 1, '****')
        clusters = []   # create list of k empty lists
        for i in range(k):
            clusters.append([])
        for a_key in data: # calculate distance to centroid
            distances = []
            for cluster_index in range(k):
                d_to_c = euclid_dist(data[a_key], centroids[cluster_index])
                distances.append(d_to_c)
            min_dis = min(distances)    # find minimum distance
            index = distances.index(min_dis)
 
            clusters[index].append(a_key)   # add to cluster
 
        dimensions = len(data[1])   # recompute clusters
        for cluster_index in range(k):
            sums = [0] * dimensions     # init sum for each dimension
            for a_key in clusters[cluster_index]:
                data_points = data[a_key]
                for ind in range(len(data_points)):
                    sums[ind] = sums[ind] + data_points[ind]
            for ind in range(len(sums)):    # calculate average
                cluster_len = len(clusters[cluster_index])
                if cluster_len != 0:
                    sums[ind] = sums[ind] / cluster_len
            
            centroids[cluster_index] = sums     # assign avg to centroids
 
        for c in clusters:  #output the clusters
            print('CLUSTER')
            for key in c:
                print(data[key], end = "")
            print()
            
    return clusters, centroids
 


def visualize_clusters(dataset_name: str, titles: list, clusters: list,
                       centroids: list) -> plt.Figure:
    """OPTIONAL - Extra credit (up to 50xp)
    Visualize the clusters and centroids. Use a different color for each cluster. 
    Args: 
        dataset_name: The name of the dataset
        titles: list of string column titles
        clusters: list of lists of tuples
        centroids: list of tuples
    Returns:
        matplotlib.pyplot.Figure: The figure object
    """
    pass


def main():
    """ Main driver for the program."""

    # Specifies the files and columns to analyze in the keys, and the number
    # of clusters in the values.
    datasets = {('earthquakes-proj8', ('latitude', 'longitude')): 5,
                ('earthquakes-proj8', ('depth', 'mag')): 5,
                ('cis210-scores', ('Projects', 'Exams')): 5}
    # Feel free to add more datasets or column pairs and experiment with different values of k

    # Compute clusters for all datasets
    for (dataset, titles), k in datasets.items():
        print(f'\nDataset: {dataset} {titles}')
        # Part 8.1
        data = load_numerical_data(dataset + '.csv', column_titles=titles)

        # Part 8.3
        centroids = create_centroids(k, data)
        print("Initialized the centroids.")

        # Parts 8.2 and 8.4 (create_clusters calls euclid_dist)
        clusters, centroids = create_clusters(k, centroids, data)
        print("\nCreated the clusters.")

        # Optional extra-credit 8.5
        visualize_clusters(dataset, titles, clusters, centroids)
        print("Visualized the clusters.")


if __name__ == '__main__':
    main()