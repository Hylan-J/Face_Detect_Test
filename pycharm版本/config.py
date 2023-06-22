import cv2
import dlib

opencv_haarcascade_detector = cv2.CascadeClassifier("resource/haarcascade_frontalface_default.xml")
dlib_hog_detector = dlib.get_frontal_face_detector()