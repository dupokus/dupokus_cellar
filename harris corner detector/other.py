import cv2 as cv2
import numpy as np
import scipy as sp
import skimage as sk
from scipy import signal
from scipy.ndimage import gaussian_filter
filename = 'D:/Studying/projects/LAB2/img/img_chess.png'
filename2 = 'D:/Studying/projects/LAB2/img/img_chess.png'
img = cv2.imread(filename)
img2 = cv2.imread(filename2)
# переводимо зображення у сірий
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
def harris_corners(img, gray):
    dx = [[1,0, -1]]
    dy = [[1],[0],[-1]]
    # згорткою шукаємо Іх Іу за допомогою DoG
    img_gaussian_blur = cv2.GaussianBlur(gray, (3, 3), 0.4)
    # Horizontal Derivative
    der_x = sp.signal.convolve2d(img_gaussian_blur, dx, mode='same')
    # Vertical Derivative
    der_y = sp.signal.convolve2d(img_gaussian_blur, dy, mode='same')
    # згорткою Іх2 Іу2 Іху через ядро Гауса отримуємо Sx2 Sy2 Sxy
    Ix2 = der_x*der_x + (0-0)
    Iy2 = der_y*der_y
    Ixy = der_x*der_y
    Sx2 = gaussian_filter(Ix2, 0.8)
    Sy2 = gaussian_filter(Iy2, 0.8)
    Sxy = gaussian_filter(Ixy, 0.8)
    # створення матриці М(з відомої формули), яку ми будем обчислювати
    matr = np.array([[Sx2, Sxy],
                     [Sxy, Sy2]])

    det_matr = Sx2 * Sy2 - Sxy * Sxy
    trace_matr = np.trace(matr)
    # шукаємо відклики харіса по формулі
    responce = det_matr - 0.05 * (trace_matr*trace_matr)
    # встановимо поріг на 0
    resp_pos = responce
    np.place(resp_pos, resp_pos < 80000, [0])

    maxima = sk.morphology.local_maxima(resp_pos) # душимо немаксимуми і отримуємо масив True False
    result = np.zeros(np.shape(maxima))
    # zlob loop
    for i in range(len(maxima)):
        for j in range(len(maxima)):
            if maxima[i, j]: # там де тру, ставимо 255 для яскравості
                result[i,j] = 255
                #cv2.circle(img, (j, i), 3, (50, 255, 0), 2)
    #cv2.imshow("", img)
    return result
def patch_descriptors(result_h, gray_im):
    des_size = 3 # розмір дескриптора
    w, h = gray_im.shape # розміри чб фото
    descriptors = [] # потрібний нам масив
    size = int(np.ceil(des_size/2))# ніхто не взнає, що я дружу з Владом Микулою
    for x in range(1, w-1):
        for y in range(1, h-1):
            if result_h[x][y]>0:
               descriptor = np.reshape(gray_im[x-size+1: x+size, y-size+1: y+size],(des_size ** 2,1))
               descriptors.append([descriptor.ravel(), y, x])

    return np.array(descriptors)
def match_patch_descriptors(descriptors1, descriptors2):
    match_coords = []  # список координат точок, що співпадуть

    for desc1, desc1_y, desc1_x in descriptors1:
        euclid_dist = []  # список евклідових відстаней між дескрипторами
        for desc2, desc2_y, desc2_x in descriptors2:
            distance = np.linalg.norm(desc1 - desc2)
            euclid_dist.append([distance, desc2_y, desc2_x])

        # перевіряємо щоб не було пустого списку
        if not euclid_dist:
            continue
        euclid_dist.sort()  # сортуємо список відстаней від найменшої до найбільшої
        last_dist = euclid_dist[0]  # отримуємо найменшу відстань
        last_dist_plus1 = euclid_dist[1]  # отримуємо відстань, яка майже найменша
        result = last_dist[0] / last_dist_plus1[0]

        if result < 0.8:
            match_coords.append([[desc1_y, desc1_x], [last_dist[1], last_dist[2]]])  # додаємо координати точок у список
    return match_coords

arrr = match_patch_descriptors(patch_descriptors(harris_corners(img, gray), gray),
                                   patch_descriptors(harris_corners(img2, gray2), gray2))
for [desc1_y, desc1_x], [desc2_y, desc2_x] in arrr:
    cv2.circle(img2, (desc2_y, desc2_x), 3, (50, 255, 0), 2)
    cv2.circle(img, (desc1_y, desc1_x), 3, (50, 255, 0), 2)

    cv2.imshow("1", img)
    cv2.imshow("2", img2)
harris_corners(img, gray)
cv2.waitKey()