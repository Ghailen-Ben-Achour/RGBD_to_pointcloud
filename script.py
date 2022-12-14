from rgbd_utils import rgbd
from pcd_utils import *
import argparse

def parse_args():
    parser = argparse.ArgumentParser('RGBD')
    parser.add_argument('--path_to_data', type=str, default='./img', help='path to data folder')
    parser.add_argument('--filename', type=str, default='000000-0', help='filename')
    return parser.parse_args()

def main(args):
    path_to_rgb = args.path_to_data + '/rgb/' + args.filename + '.png'
    path_to_depth = args.path_to_data + '/depth/' + args.filename + '.png'
    path_to_intrinsic = args.path_to_data + '/intrinsic/' + args.filename + '.txt'
    path_to_extrinsic = args.path_to_data + '/extrinsic/' + args.filename + '.txt'
    # rgbd_utils features
    rgbd_img = rgbd(path_to_rgb, path_to_depth)
    rgbd_img.visualize()
    pcd = rgbd_img.rgbd_to_pcd(path_to_intrinsic, path_to_extrinsic)
    # pcd utils features
    inliers = outlierRemoval(pcd, nb_neighbors=50, std_ratio=1.0)
    pcdClustering(inliers)

if __name__ == '__main__':
    args = parse_args()
    main(args)
