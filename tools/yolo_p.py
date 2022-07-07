from demo import detect
from lib.config import cfg
import torch
import cv2

vid_path = 'inference/rgb_streams/shortened_file-60fps.avi'
cap = cv2.VideoCapture(vid_path)
while cap.isOpened():
    ret, frame = cap.read()
    detect(cfg)