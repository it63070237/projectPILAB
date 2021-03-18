import cv2
import numpy as np

def ssd(img2, img1):
    return float(np.sqrt(float(np.sum((np.array(img1).flatten()-np.array(img2).flatten())**2))))/(img2.shape[0]*img2.shape[1])


red = cv2.imread('red.jpg')
green = cv2.imread('green.jpg')
blue = cv2.imread('blue.jpg')

red = red[33:1033, 94:1094]
blue = blue[32:1033, 94:1094]
green = green[33:1033, 94:1094]


sz_test = red.shape
print(red.shape)
print(blue.shape)
print(green.shape)
height = int(sz_test[0])
width = sz_test[1]

im_color = np.zeros((100, 100, 3), dtype=np.uint8)
im_color[:, :, 2] = red[(height//2)-50:(height//2)+50, (width//2)-50:(width//2)+50, 0]
im_color_slide = np.zeros((height, width, 3), dtype=np.uint8)
im_color_slide[:, :, 2] = red[:, :, 0]

u, v, ssd_now = 0, 0, 10
for hei in range(-15, 16, 1):
    for wid in range(-15, 16, 1):
        test_window = im_color.copy()
        test_window[:, :, 1] = green[(height//2)-50+hei:(height//2)+50+hei, (width//2)-50+wid:(width//2)+50+wid, 0]
        if ssd(test_window[:, :, 2], test_window[:, :, 1]) < ssd_now:
            ssd_now = ssd(test_window[:, :, 2], test_window[:, :, 1])
            u = hei
            v = wid

cv2.imshow('test1', test_window)
print(ssd_now)
print('ans1 : ',u ,v)
if u <= 0 and v <= 0:
    im_color_slide[:height-abs(u), :width-abs(v), 1] = green[abs(u):, abs(v):, 0]
elif u <= 0 and v > 0:
    im_color_slide[:height - abs(u), v:, 1] = green[abs(u):, :width-abs(v), 0]
elif u > 0 and v <= 0:
    im_color_slide[u:, :width - abs(v), 1] = green[:height-abs(u), abs(v):, 0]
elif u > 0 and v > 0:
    im_color_slide[:-u, :-v, 1] = green[u:, v:, 0]


u, v, ssd_now = 0, 0, 10
for hei in range(-15, 16, 1):
    for wid in range(-15, 16, 1):
        test_window = im_color.copy()
        test_window[:, :, 0] = blue[(height//2)-50+hei:(height//2)+50+hei, (width//2)-50+wid:(width//2)+50+wid, 0]
        if ssd(test_window[:, :, 2], test_window[:, :, 0]) < ssd_now:
            ssd_now = ssd(test_window[:, :, 2], test_window[:, :, 0])
            u = hei
            v = wid

cv2.imshow('test2', test_window)
print(ssd_now)
print('ans2 : ',u ,v)
if u <= 0 and v <= 0:
    im_color_slide[abs(u):, abs(v):, 0] = blue[:u, :v, 0]
elif u <= 0 and v > 0:
    im_color_slide[:height - abs(u), v:, 0] = blue[abs(u):, :width-abs(v), 0]
elif u > 0 and v <= 0:
    im_color_slide[u:, :width - abs(v), 0] = blue[:height-abs(u), abs(v):, 0]
elif u > 0 and v > 0:
    im_color_slide[:-u, :-v, 1] = green[u:, v:, 0]

cv2.imshow('real', im_color_slide)
cv2.waitKey(0)

