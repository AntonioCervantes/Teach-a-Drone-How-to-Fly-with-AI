""" This program generates a ArUco Tag, based on the compatible dictionaries. 
    Please modify user arguments to modify the ArUco tag generated.

    Author:         Christian Pedrigal, pedrigalchristian@gmail.com
    Last modified:  3/12/2022
"""
import cv2
import numpy as np
import os

from aruco_dict import ARUCO_DICT

# Global Constants
DEBUG: bool = False
SIZE: int   = 300
BORDER: int = 1
OUT_PATH: str = r"C:\Users\pedri\Desktop\ME 297-01_Deep_Learning\Aruco-classification\ArUco Tags"

# User Arguments
tag_dict: str  = "DICT_6X6_50"
tag_id: int    = 1
filename: str = "DICT_6X5_50_id1.png"
if DEBUG: print(os.path.join(OUT_PATH, filename))

# 1. Import ArUco Dictionary considering: (1) Size, (2) Number of IDs
arctype: cv2.aruco_Dictionary = cv2.aruco.Dictionary_get(ARUCO_DICT[tag_dict])
if DEBUG: print(arctype)

# 2. Draw marker, based on four arguments: (1) Aruco type, (2) ID, (3) size, (4) input image, (5) borderline type
in_image: np  = np.zeros((SIZE, SIZE, 1), dtype = "uint8")
cv2.aruco.drawMarker(arctype, tag_id, SIZE, in_image, BORDER)
if DEBUG: print(type(tag_id))

# 3. Show image
cv2.imshow("ArUco Tag", in_image)
cv2.imwrite(os.path.join(OUT_PATH, filename), in_image)
cv2.waitKey(0)