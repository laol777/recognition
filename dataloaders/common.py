from PIL import Image
import cv2
import random 
import numpy as np 
from huepy import red 

def is_image_file(filename):
    return any(filename.lower().endswith(extension) for extension in [".png", ".jpg", ".jpeg"])

def get_image_cv2(path):
    img = cv2.imread(path, -1)
    if img is None:
        print(red(path))
    img = img[:, :, :3]
    img = img[:, :, ::-1]
    return img

def get_image_pil(path):
    img = Image.open(path).convert('RGB')
    return img

def inin_w(worker_id):
    np.random.seed(random.randint(0, 2**31))

def uint2float(img):
    out = img.astype(np.float32)
    if img.dtype == np.uint16:
        out /= 65535.
    elif img.dtype == np.uint8:
        out /= 255

    return out