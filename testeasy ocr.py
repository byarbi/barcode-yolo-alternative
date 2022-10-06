import easyocr
import cv2

crop_img = cv2.imread('opencv_bar_crop.png')
reader = easyocr.Reader(['en'])
result = reader.readtext(crop_img)
print("ocr result : " + result[0][1])
