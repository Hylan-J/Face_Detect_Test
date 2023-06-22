import detect_functions
from utils import auto_test

if __name__ == '__main__':
    video_path = "test_data/video/out.avi"
    detector_types = [detect_function for detect_function in dir(detect_functions) if
                      detect_function.startswith('detect_face_by_')]
    print(detector_types)
    auto_test(video_path, detector_types)
