import cv2
import numpy as np

def ssd(img1, img2):
    return float(np.sqrt(float(np.sum((np.array(img1).flatten()-np.array(img2).flatten())**2))))/(img1.shape[0]*img1.shape[1])


red = cv2.imread('red.jpg')
green = cv2.imread('green.jpg')
blue = cv2.imread('blue.jpg')

red = red[100:1000, 100:1050]
blue = blue[100:1000, 100:1050]
green = green[100:1000, 100:1050]

down_shape_red = red.copy()
for i in range(3):
    down_shape_red = cv2.pyrDown(down_shape_red)

down_shape_green = green.copy()
for i in range(3):
    down_shape_green = cv2.pyrDown(down_shape_green)

down_shape_blue = blue.copy()
for i in range(3):
    down_shape_blue = cv2.pyrDown(down_shape_blue)

sz_test = down_shape_red.shape
print(sz_test)
height = int(sz_test[0])
width = sz_test[1]

im_color_down = np.zeros((height, width, 3), dtype=np.uint8)
im_color_down[:, :, 2] = down_shape_red[:, :, 0]

u, v, ssd_now = 0, 0, 10
for hei in range(1, height):
    for wid in range(1, width):
        test_window = im_color_down.copy()
        ali = down_shape_green.copy()
        test_window[:-hei, :-wid, 1] = ali[hei:, wid:, 0]
        if ssd(test_window[:, :, 2], test_window[:, :, 1]) < ssd_now:
            ssd_now = ssd(test_window[:, :, 2], test_window[:, :, 1])
            u = hei*8
            v = wid*8


sz = red.shape
height_1 = int(sz[0])
width_1 = sz[1]
im_color = np.zeros((height_1, width_1, 3), dtype=np.uint8)
im_color[:, :, 2] = red[:, :, 0]
im_color[:-u, :-v, 1] = green[u:, v:, 0]
print(u,v)


cv2.imshow('test', im_color)
cv2.waitKey(0)
