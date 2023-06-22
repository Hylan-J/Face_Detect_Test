import time
from detect_functions import *
import cv2


def test_detector_performance(video_path, detector_type):
    result = dict()
    result['fps'] = 0
    result['accuracy'] = 0

    fps_count = []
    frame_count = 0
    face_detected_frame_count = 0
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if ret:
            frame_count += 1
            start_time = time.time()
            faces = globals()[str(detector_type)](frame)
            end_time = time.time()
            fps_count.append(1 / (end_time - start_time))
            if len(faces) > 0:
                face_detected_frame_count += 1
        else:
            result['accuracy'] = face_detected_frame_count / frame_count
            result['fps'] = sum(fps_count) / len(fps_count)
            return result