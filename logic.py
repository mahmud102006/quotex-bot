import numpy as np
from PIL import Image
import cv2

def analyze_image(img: Image.Image):
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    h, w = cv_img.shape[:2]
    crop = cv_img[h//4:3*h//4, w//6:5*w//6]

    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    mask_green = cv2.inRange(hsv, (40,50,50), (80,255,255))
    mask_red1 = cv2.inRange(hsv, (0,50,50), (10,255,255))
    mask_red2 = cv2.inRange(hsv, (170,50,50), (180,255,255))
    green_px = cv2.countNonZero(mask_green)
    red_px = cv2.countNonZero(mask_red1) + cv2.countNonZero(mask_red2)

    if green_px > red_px:
        return "📈 CALL signal", "Green dominant (↑ trend)"
    else:
        return "📉 PUT signal", "Red dominant (↓ trend)"
