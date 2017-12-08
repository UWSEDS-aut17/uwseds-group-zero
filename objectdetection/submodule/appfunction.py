import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "/..")))
from submodule import object_detection_main as od
import tensorflow as tf
from PIL import Image
import os
import cv2

# Check for the tensorflow version

def tf_version_check():
        # check for version of tensorflow
    if tf.__version__ != '1.4.0':
        raise ImportError('Please upgrade your tensorflow installation to v1.4.0!')

# image detection

def input_image(img_input, modelPath, labelMapPath, savepath):
    img_input = cv2.imread(img_input)
    print("Processing...")
    new_img_Process = od.objectDetection(modelPath, labelMapPath)
    testval, img_detected = new_img_Process.detect_process(img_input, True, False, savepath, False)
    cv2.imwrite(os.path.join(savepath, 'savedimg.jpg'), img_detected)
    img_detected = Image.fromarray(img_detected, 'RGB')
    return img_detected, testval

# video detection

def input_video(video_file, modelPath, labelMapPath, savepath, test):
    video_input = cv2.VideoCapture(video_file)
    video_open(video_input, False, modelPath, labelMapPath, savepath, test)

# call for camera streaming

def input_cam(modelPath, labelMapPath, savepath, test):
    cap = cv2.VideoCapture(0)
    return video_open(cap, False, modelPath, labelMapPath, savepath, test)

def file_is_exist(path):
    return os.path.isfile(path)

def video_open(cap, flag, modelPath, labelMapPath, savepath, test):
    if not cap.isOpened():
        raise Exception("Error opening video stream or file!")
    print("Processing...")
    print("You can press 'q' to close the detection window after you see it pops up!")
    save = False
    if not savepath == None and not savepath == "" and os.path.isdir(savepath) == True:
        save = True
    new_video_Process = od.objectDetection(modelPath, labelMapPath)
    while (cap.isOpened()):
        # sent to object detection
        # stop streaming and release the camera if window close or "q" is pressed
        test_video = new_video_Process.detect_process(cap, flag, save, savepath, test)
        # for test
        if test_video == True:
            cap.release()
            return 1
        # test ends when return value from detect_process is false
        else:
            cap.release()
            return -1

