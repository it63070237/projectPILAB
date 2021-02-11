import cv2
import numpy as np

def get_gradient(im) :
    grad_x = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(im, cv2.CV_32F, 0, 1, ksize=3)

    grad = cv2.addWeighted(np.absolute(grad_x), 0.5, np.absolute(grad_y), 0.5, 0)
    return grad

if __name__ == '__main__':

    red = cv2.imread('red.jpg', cv2.IMREAD_GRAYSCALE)
    green = cv2.imread('green.jpg', cv2.IMREAD_GRAYSCALE)
    blue = cv2.imread('blue.jpg', cv2.IMREAD_GRAYSCALE)

    red = red[0:1032, 0:1188]
    blue = blue[0:1032, 0:1188]
    green = green[0:1032, 0:1188]

    sz = red.shape
    print(sz)
    height = int(sz[0])
    width = sz[1]


    im_color = np.zeros((height, width, 3), dtype=np.uint8)

    im_color[:, :, 2] = red[:, :]
    im_color[:, :, 0] = blue[:, :]
    im_color[:, :, 1] = green[:, :]

    im_aligned = np.zeros((height,width,3), dtype=np.uint8 )

    im_aligned[:, :, 2] = im_color[:, :, 2]

    warp_mode = cv2.MOTION_HOMOGRAPHY

    if warp_mode == cv2.MOTION_HOMOGRAPHY :
            warp_matrix = np.eye(3, 3, dtype=np.float32)
    else :
            warp_matrix = np.eye(2, 3, dtype=np.float32)

    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5000,  1e-10)

    for i in range(0,2) :
        (cc, warp_matrix) = cv2.findTransformECC(get_gradient(im_color[:, :, 2]), get_gradient(im_color[:, :, i]), warp_matrix, warp_mode, criteria, None, 1)

        if warp_mode == cv2.MOTION_HOMOGRAPHY :
            im_aligned[:, :, i] = cv2.warpPerspective (im_color[:, :, i], warp_matrix, (width, height), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
        else :
            im_aligned[:, :, i] = cv2.warpAffine(im_color[:, :, i], warp_matrix, (width, height), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);
        print(warp_matrix)

    cv2.imshow("Color Image test", im_color)
    cv2.imshow("Aligned Image test", im_aligned)
    cv2.waitKey(0)

