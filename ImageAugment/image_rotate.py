import numpy as np
import cv2

def rotate_90(image_path,angle):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    matRotate = cv2.getRotationMatrix2D((height * 0.5, width * 0.5), angle, 1)
    dst = cv2.warpAffine(img, matRotate, (width*2, height*2))
    rows, cols = dst.shape[:2]
    for col in range(0, cols):
        if dst[:, col].any():
            left = col
            break
    for col in range(cols-1, 0, -1):
        if dst[:, col].any():
            right = col
            break
    for row in range(0, rows):
        if dst[row,:].any():
            up = row
            break
    for row in range(rows-1,0,-1):
        if dst[row,:].any():
            down = row
            break
    res_widths = abs(right - left)
    res_heights = abs(down - up)
    res = np.zeros([res_heights ,res_widths, 3], np.uint8)
    for res_width in range(res_widths):
        for res_height in range(res_heights):
            res[res_height, res_width] = dst[up+res_height, left+res_width]
    return res

if __name__ =='__main__':
    res = rotate_90('test.jpg',-90)
    print(res.shape)