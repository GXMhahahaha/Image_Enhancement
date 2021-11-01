import cv2
import numpy as np


# gamma correction
def gamma_correction(img, c=1, g=1.5):
    img_new = img.astype(np.float)
    out = img_new.copy()
    out /= 255.
    out = (1 / c * out) ** (1 / g)

    out *= 255
    out = out.astype(np.uint8)

    return out

