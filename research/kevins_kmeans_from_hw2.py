import random 
import numpy as np
import matplotlib.pyplot as plt

def l2_dist(x1,x2):
    l2_dist = np.sqrt(np.sum((np.array(x1) - np.array(x2))**2))
    return l2_dist

def kmeans(df, k, tol):
    """
    Usage: input
        df=data frame,
        k=# of clusters
        tol=tolerance for L_2 convergance check on centroids
    """
    tuples = [tuple(row) for row in selected_df.itertuples(index=False)]
    random_k_rows = random.sample(tuples, k)
    centroids = random_k_rows

    cluster_assignments = np.array([-1]*len(tuples))

    prev_error = float("inf")
    curr_error = float("inf")

    # PUT IN while LOOP
    while True:
        # get nearest assignments
        for i in range(len(cluster_assignments)):
            dists = [l2_dist(tuples[i], centroid) for centroid in centroids]
            assignment = dists.index(min(dists))
            cluster_assignments[i] = assignment

        # update centroids
        X = np.array([list(tup) for tup in tuples])

        for centroid_num in range(k):
            x_mean = np.sum(X[cluster_assignments==centroid_num,0])
            y_mean = np.sum(X[cluster_assignments==centroid_num,0])
            z_mean = np.sum(X[cluster_assignments==centroid_num,0])
            if x_mean != 0:
                x_mean = np.mean(X[cluster_assignments==centroid_num,0])
            if y_mean != 0:
                y_mean = np.mean(X[cluster_assignments==centroid_num,1])
            if z_mean != 0:
                z_mean = np.mean(X[cluster_assignments==centroid_num,2])
            centroids[centroid_num]=(x_mean,y_mean,z_mean)

        # meanerror
        meanerror = 0
        for i in range(len(X)):
            meanerror += l2_dist(X[i], centroids[cluster_assignments[i]])**2
        meanerror = meanerror / len(X)
        curr_error = meanerror

        if abs(curr_error - prev_error) <= tol: break
        prev_error = curr_error

    # print(meanerror)
    clusters = X
    return centroids, clusters, cluster_assignments, meanerror

# get a df
selected_df = df[["HP","Attack","Defense"]]
centroids, clusters, cluster_assignments, meanerror = kmeans(selected_df, k=4, tol=0.05)

# scatter plot
colors = ['red', 'green', 'blue', 'orange']
# clusters
for i in range(len(clusters)):
    plt.scatter(clusters[i][1], clusters[i][2], color=colors[cluster_assignments[i]])
# centroids
plt.scatter([x[1] for x in centroids], [x[2] for x in centroids], c='black', marker='+')

plt.xlabel("Attack")
plt.ylabel("Defense")
plt.show()