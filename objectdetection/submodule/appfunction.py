import sys
import os
sys.path.insert(
    0, 
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "/..")
        )
    )
from submodule import object_detection_main as od
import tensorflow as tf
from PIL import Image
import os
import cv2

# Check for the tensorflow version
def tf_version_check():
        # check for version of tensorflow
    if tf.__version__ != '1.4.0':
        raise ImportError('Please upgrade your' + \
                           'tensorflow installation to v1.4.0!'
                          )

'''
Static image detection
Argument: 1. img_input refers to the path to the input image
          2. modelPath refers to the path to your model file
          3. labelMapPath refers to the path to your label map file
             (corresponding to your model file)
          4. savepath is the  path where users want to save thes output
Return: *  An array - The detected image
           (with boxes around detected objects in the image)
        *  -1 - for test value as an indicator of testing
'''
def input_image(img_input, modelPath, labelMapPath, savepath):
    img_input = cv2.imread(img_input)
    print("Processing...")
    new_img_Process = od.objectDetection(modelPath, labelMapPath)
    testval, img_detected = new_img_Process.detect_process(
                                img_input,
                                True,
                                False,
                                savepath,
                                False
                                )
    cv2.imwrite(os.path.join(savepath, 
                             'savedimg.jpg'), 
                             img_detected
                             )
    img_detected = Image.fromarray(img_detected, 'RGB')
    return img_detected, testval

'''
Video detection
Argument: 1. video_file refers to the path to your input video
          2. modelPath refers to the path to your model file
          3. labelMapPath refers to the path to your label map file
             (corresponding to your model file)
          4. savepath is the  path where users want to save thes output
          5. test refers whether the process is called in a
             test file or not. (True if so)
Return: *  -1 if the camera stream ends or terminated by user
        *  1 if it has test flag being True (i.e it's called in a test)
'''
def input_video(video_file, modelPath, labelMapPath, savepath, test):
    video_input = cv2.VideoCapture(video_file)
    return video_open(video_input,
               False,
               modelPath,
               labelMapPath,
               savepath,
               test
               )
'''
Live camera detection
Argument: 1. modelPath refers to the path to your model file
          2. labelMapPath refers to the path to your label map file
             (corresponding to your model file)
          3. savepath is the  path where users want to save thes output
          4. test refers whether the process is called in a
             test file or not. (True if so)
Return: *  -1 if the camera stream ends or terminated by user
        *  1 if it has test flag being True (i.e it's called in a test)
'''
def input_cam(modelPath, labelMapPath, savepath, test):
    cap = cv2.VideoCapture(0)
    return video_open(cap,
                      False,
                      modelPath,
                      labelMapPath,
                      savepath,
                      test)

'''
Check for the existence of the given path
Return True if exists. False otherwise
'''
def file_is_exist(path):
    return os.path.isfile(path)

'''
Helper method for video/camera detection
Argument: 1. cap refers to the path to your input video or live camera capture
          2. flag refers to whethe given cap is an image
          2. modelPath refers to the path to your model file
          3. labelMapPath refers to the path to your label map file
             (corresponding to your model file)
          4. savepath is the  path where users want to save thes output
          5. test refers whether the process is called in a
             test file or not. (True if so)
Return: *  -1 if the video/camera stream ends or terminated by user
        *  1 if it has test flag being True (i.e it's called in a test)

Exceptions: If the given video/camera stream (cap) cannot be opened, 
            Exception thrown
'''
def video_open(cap, flag, modelPath, labelMapPath, savepath, test):
    if not cap.isOpened():
        raise Exception("Error opening video stream or file!")
    print("Processing...")
    print("PRESS 'q' to CLOSE the detection window" + \
          "after you see it pops up!")
    save = False
    if not savepath == None and not \
           savepath == "" and \
           os.path.isdir(savepath) == True:
        save = True
    new_video_Process = od.objectDetection(modelPath, labelMapPath)
    while (cap.isOpened()):
        # sent to object detection
        # stop streaming and release the camera if window close or "q" is pressed
        test_video = new_video_Process.detect_process(
                        cap,
                        flag,
                        save,
                        savepath,
                        test
                        )
        # for test
        if test_video == True:
            cap.release()
            return 1
        # Streaming ends
        else:
            cap.release()
            return -1

