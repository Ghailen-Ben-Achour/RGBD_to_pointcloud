from utils import rgbd

rgbd_img = rgbd("./img/rgb/000000-0.png", "./img/depth/000000-0.png")
rgbd_img.rgbd_to_pcd("./img/intrinsic/000000-0.txt", "./img/extrinsic/000000-0.txt")
