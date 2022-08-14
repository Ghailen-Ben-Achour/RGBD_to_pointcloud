import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def outlierRemoval(pcd, nb_neighbors=20, std_ratio=2.0):
    print("Statistical oulier removal")
    _, ind = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors,
                                            std_ratio=std_ratio)
    inlier_cloud = pcd.select_by_index(ind)

    o3d.visualization.draw_geometries([inlier_cloud])
    return inlier_cloud


def pcdClustering(pcd, eps=0.05, min_points=10):
    with o3d.utility.VerbosityContextManager(
            o3d.utility.VerbosityLevel.Debug) as cm:
        labels = np.array(
            pcd.cluster_dbscan(eps=eps, min_points=min_points, print_progress=True))

    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcd])
