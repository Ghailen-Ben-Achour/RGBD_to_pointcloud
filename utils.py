import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

class rgbd():
    def __init__(self, color_path, depth_path):
        print("Read data")
        self.color_raw = o3d.io.read_image(color_path)
        self.depth_raw = o3d.io.read_image(depth_path)
        self.rgbd_image =  o3d.geometry.RGBDImage.create_from_color_and_depth(
                            self.color_raw, self.depth_raw)

    def show_info(self):
        print(self.rgbd_image)
    
    def visualize(self):
        plt.subplot(1, 2, 1)
        plt.title('Color image')
        plt.imshow(self.rgbd_image.color)
        plt.subplot(1, 2, 2)
        plt.title('Depth image')
        plt.imshow(self.rgbd_image.depth)
        plt.show()
    
    def rgbd_to_pcd(self, path_to_intrinsic, path_to_extrinsic):
        intrinsic_data = np.loadtxt(path_to_intrinsic, dtype=float)
        extrinsic_data = np.loadtxt(path_to_extrinsic, dtype=float)
        cam = o3d.camera.PinholeCameraIntrinsic()
        cam.intrinsic_matrix = intrinsic_data
        
        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
            self.rgbd_image, 
            cam,
            extrinsic = extrinsic_data
        )
        # Flip it
        pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
        o3d.visualization.draw_geometries([pcd])
    


