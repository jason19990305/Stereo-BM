# Stereo BM Algorithm

This project demonstrates the implementation of the Stereo Block Matching (BM) algorithm for stereo vision using Python. The algorithm is used to generate disparity maps and visualize point clouds.

## Libraries Used

- **Python**
- **OpenCV**
- **Matplotlib**
- **Numpy**

## Overview

Stereo BM is a block matching algorithm used in stereo vision to find the disparity between two images. This disparity is then used to generate a depth map, which can be visualized as a point cloud.

## Dataset

The dataset used in this project consists of images captured by a camera mounted on a robotic arm. The camera takes a photo every 5mm, providing a series of stereo images for processing.

## Installation

To run this project, you need to have Python installed along with the following libraries:

```bash
pip install opencv-python matplotlib numpy
```

## Usage

1. **Generate Disparity Map**: The script uses the Stereo BM algorithm to generate a disparity map from a pair of stereo images.
2. **Visualize Point Cloud**: The disparity map is then used to create a point cloud, which is visualized using Matplotlib.

## Example

Here's a basic example of how to use the script:

```bash
python StereoBM.py
```

![DepthMap](https://github.com/jason19990305/Stereo-BM/blob/main/PointCloud.png)


