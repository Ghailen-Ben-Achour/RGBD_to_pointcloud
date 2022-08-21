# RGBD_to_pointcloud
Tutorial on how to convert RGBD into pointcloud using calibration

## Dataset
 Dataset can be found [here](https://3dvision.princeton.edu/projects/2017/arc/#datasets)
 This tutorial on RGBD to pointcloud is using the parallel-jaw-grasping-dataset for grqsping tasks.
 To format of the data should be as follows:
 ```plain
└── img
       ├── rgbd
       |   ├── 00000.png
       |   ├── 00001.png
       |   └── ...
       └── depth
       |   ├── 00000.png
       |   ├── 00001.png
       |   └── ...
       └── intrinsic
       |   ├── 00000.txt
       |   ├── 00001.txt
       |   └── ...
       └── extrinsic
       |   ├── 00000.png
       |   ├── 00001.png
       |   └── ...
```
