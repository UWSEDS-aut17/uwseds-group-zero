from PIL import Image
import os
import tensorflow as tf
import cv2
import sys
from submodule import object_detection_main as od

def app_start():
	# check for version of tensorflow
  if tf.__version__ != '1.4.0':
    raise ImportError('Please upgrade your tensorflow installation to v1.4.0!')
  # This is needed since the notebook is stored in the object_detection folder.
  sys.path.append("..")
  text = input("Enter which type of file you want to input: (image, video or camera?)").lower()
  if text == "image":
    file_path = ask_for_file()
    img_input = cv2.imread(file_path)
    img_detected = od.detect_process(img_input, True)
    # img = Image.fromarray(img_detected, 'RGB')
    # img.show()
    cv2.imshow('object detection', img_detected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

  elif text == "video":
    file_path = ask_for_file()
    video_input = cv2.VideoCapture(file_path)
    video_open(video_input, False)
  elif text == "camera" or text == "webcam":
    # file_path = ask_for_file()
    cap = cv2.VideoCapture(0)
    video_open(cap, False)
  else:
    raise Exception("Input type out of range!")
  # if cv2.waitKey(25) & 0xFF == ord('q'):
  #   cv2.destroyAllWindows()

def file_is_exist(path):
  return os.path.isfile(path)

def ask_for_file():
  file_path = input("Enter the path of your file:")
  if not file_is_exist(file_path):
    raise Exception("File does not exist! Try again!")
  else:
    return file_path

def video_open(cap, flag):
  if not cap.isOpened():
    raise Exception("Error opening video stream or file!")
  while (cap.isOpened()):
      # sent to object detection
      od.detect_process(cap, flag)

# cv2.imshow('object detection', cv2.flip(cv2.resize(image_np, (1024, 768)), 1))
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#           cv2.destroyAllWindows()
#           break

