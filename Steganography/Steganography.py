
import cv2
import numpy as np
import random


# Encryption function
def encrypt():
    # img1 and img2 are the two input images

    img1 = cv2.imread('test1.PNG')
    img2 = cv2.imread('test2.PNG')

    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            for l in range(3):
                # v1 and v2 are 8-bit pixel values of img1 and img2 respectively

                v1 = format(img1[i][j][l], '08b')
                v2 = format(img2[i][j][l], '08b')

                # Taking 4 MSBs of each image
                v3 = v1[:4] + v2[:4]

                img1[i][j][l] = int(v3, 2)

    cv2.imwrite('pic3in2.png', img1)


# Decryption function
def decrypt():
    # Encrypted image
    img = cv2.imread('pic3in2.png')
    width = img.shape[0]
    height = img.shape[1]

    # img1 and img2 are two blank images
    img1 = np.zeros((width, height, 3), np.uint8)
    img2 = np.zeros((width, height, 3), np.uint8)

    for i in range(width):
        for j in range(height):
            for l in range(3):
                v1 = format(img[i][j][l], '08b')
                v2 = v1[:4] + chr(random.randint(0, 1) + 48) * 4
                v3 = v1[4:] + chr(random.randint(0, 1) + 48) * 4

                # Appending data to img1 and img2
                img1[i][j][l] = int(v2, 2)
                img2[i][j][l] = int(v3, 2)

    # These are two images produced from
    # the encrypted image
    cv2.imwrite('pic2_re.png', img1)
    cv2.imwrite('pic3_re.png', img2)



def countObject(imageName):

    image = cv2.imread(imageName)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 200)

    contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    number_of_objects_in_image = len(contours)

    print("The number of objects in this image: ", str(number_of_objects_in_image))



print("Before Encryption ")
encrypt()
countObject("C:/ui3.PNG")
decrypt()
print("After Decryption ")
countObject("pic3in2.png")

