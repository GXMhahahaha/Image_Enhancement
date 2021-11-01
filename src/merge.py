# Name : merge.py
# Time : 2021/10/27 11:23
import matplotlib.pyplot as plt
import numpy as np
import cv2


def merge_run(pic_gamma, pic_mrscr):
    img1 = pic_gamma.astype(np.float)
    img2 = pic_mrscr.astype(np.float)
    new_img = np.add(0.7 * img1, 0.3 * img2).astype(np.int)
    return new_img

