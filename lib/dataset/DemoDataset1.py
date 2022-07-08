import glob
import os
import random
import shutil
import time
from pathlib import Path
from threading import Thread

import cv2
import math
import numpy as np
import torch
from PIL import Image, ExifTags
from torch.utils.data import Dataset
from tqdm import tqdm

from ..utils import letterbox_for_img

# img_formats = ['.bmp', '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.dng']
# vid_formats = ['.mov', '.avi', '.mp4', '.mpg', '.mpeg', '.m4v', '.wmv', '.mkv']

def LoadImages(img0):
    # Padded resize
    img_size = 640
    h0, w0 = img0.shape[:2]
    img, ratio, pad = letterbox_for_img(img0, new_shape=img_size, auto=True)
    h, w = img.shape[:2]
    shapes = (h0, w0), ((h / h0, w / w0), pad)
    img = np.ascontiguousarray(img)
    return img, img0, shapes

# class LoadImages:  # for inference
#     def __init__(self, image, img_size=640):
#         # p = str(Path(path))  # os-agnostic
#         # p = os.path.abspath(p)  # absolute path
#         # if '*' in p:
#         #     files = sorted(glob.glob(p, recursive=True))  # glob
#         # elif os.path.isdir(p):
#         #     files = sorted(glob.glob(os.path.join(p, '*.*')))  # dir
#         # elif os.path.isfile(p):
#         #     files = [p]  # files
#         # else:
#         #     raise Exception('ERROR: %s does not exist' % p)

#         # images = [x for x in files if os.path.splitext(x)[-1].lower() in img_formats]
#         # videos = [x for x in files if os.path.splitext(x)[-1].lower() in vid_formats]
#         # ni, nv = len(images), len(videos)

#         self.img_size = img_size
#         # self.files = images + videos
#         # self.nf = ni + nv  # number of files
#         # self.video_flag = [False] * ni + [True] * nv
#         # self.mode = 'images'
#         # if any(videos):
#         #     self.new_video(videos[0])  # new video
#         # else:
#         #     self.cap = None
#         # assert self.nf > 0, 'No images or videos found in %s. Supported formats are:\nimages: %s\nvideos: %s' % \
#         #                     (p, img_formats, vid_formats)

#     def __iter__(self):
#         self.count = 0
#         return self

#     def __next__(self):
#         if self.count == self.nf:
#             raise StopIteration
#         path = self.files[self.count]

#         # Read image
#         self.count += 1
#         img0 = cv2.imread(path, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)  # BGR
#         #img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
#         assert img0 is not None, 'Image Not Found ' + path
#         print('image %g/%g %s: \n' % (self.count, self.nf, path), end='')
#         h0, w0 = img0.shape[:2]

#         # Padded resize
#         img, ratio, pad = letterbox_for_img(img0, new_shape=self.img_size, auto=True)
#         h, w = img.shape[:2]
#         # print('h0, w0:\n', h0, w0)
#         # print('h, w:\n', h, w)
#         # print('pad:\n', pad)
#         shapes = (h0, w0), ((h / h0, w / w0), pad)

#         # Convert
#         #img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
#         img = np.ascontiguousarray(img)


#         # cv2.imwrite(path + '.letterbox.jpg', 255 * img.transpose((1, 2, 0))[:, :, ::-1])  # save letterbox image
#         return path, img, img0, self.cap, shapes

#     def new_video(self, path):
#         self.frame = 0
#         self.cap = cv2.VideoCapture(path)
#         self.nframes = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

#     def __len__(self):
#         return self.nf  # number of files

