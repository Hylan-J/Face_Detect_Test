from config import opencv_haarcascade_detector, dlib_hog_detector


def detect_face_by_opencv_haarcascade(image):
    faces = opencv_haarcascade_detector.detectMultiScale(image)
    return faces


def detect_face_by_dlib_hog(image):
    faces = dlib_hog_detector(image, 1)
    return faces
