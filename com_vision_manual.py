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

sz = red.shape
print(sz)
height = int(sz[0])
width = sz[1]


im_color = np.zeros((height, width, 3), dtype=np.uint8)

im_color[:, :, 2] = red[:, :, 0]
im_color[:-15, :-15, 1] = green[15:, 15:, 0]
im_color[11:,:-23, 0] = blue[:-11, 23:, 0]

print(ssd(im_color[:, :, 2], im_color[:, :, 1]))

cv2.imshow('test', im_color)
cv2.imshow('red', red)
cv2.waitKey(0)