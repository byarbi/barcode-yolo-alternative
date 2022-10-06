import cv2
from pyzbar.pyzbar import decode

cam_port = 0
cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)


def capture_key_pressed():

    cv2.namedWindow("test")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        for barcode in decode(frame):
            myData = barcode.data.decode('utf-8')
            print(myData)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    return img_name


