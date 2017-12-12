# coding: utf-8

# This file builds a object detection tensorflow 
# using tensorflow api and the process of building 
# the deep neural net is derived from 
# object_detection_tutorial.ipynb

# Needed libraries
import sys
import os
sys.path.insert(0, 
                os.path.abspath(os.path.dirname(__file__))
                )
from utils import visualization_utils as vis_util
from utils import label_map_util
from matplotlib import pyplot as plt
import six.moves.urllib as urllib
import tensorflow as tf
from io import StringIO
from PIL import Image
import numpy as np
import tarfile
import zipfile
import time
import sys
import cv2
import os

rate = ""

'''
Class for a new object detection process
'''
class objectDetection:
    def __init__(self, modelPath, labelMapPath):
        self.modelPath = modelPath
        self.labelMapPath = labelMapPath

    # model setup:
    # 1. Specify which tensorflow model to use
    # 2. Locate label files and 
    #    indicate how many classes in the labels
    # 3. Load in label map using the label file
    # 4. Return the category indices 
    #    which correspond to the digital labels
    def model_setup(self):
        PATH_TO_CKPT = ""
        PATH_TO_LABELS = ""
        # if model is not specified, use default ssd_mobilenet_v1_coco
        if self.modelPath == None or \
           self.modelPath == "":
            # What model to download.
            MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
            MODEL_FILE = MODEL_NAME + '.tar.gz'
            DOWNLOAD_BASE = 'http://download.tensorflow.org/' + \
                             'models/object_detection/'
            # Path to frozen detection graph. 
            # This is the actual model that is used for the object detection.
            PATH_TO_CKPT = "./submodule/" + \
                            MODEL_NAME + \
                            '/frozen_inference_graph.pb'
            if os.path.isfile(PATH_TO_CKPT) and \
               os.access(PATH_TO_CKPT, os.R_OK):
                pass
            else:
                # Download Model
                opener = urllib.request.URLopener()
                opener.retrieve(DOWNLOAD_BASE + \
                                MODEL_FILE,
                                MODEL_FILE)
                tar_file = tarfile.open(MODEL_FILE)
                for file in tar_file.getmembers():
                    file_name = os.path.basename(file.name)
                    if 'frozen_inference_graph.pb' in file_name:
                        tar_file.extract(file, os.getcwd() + "/submodule")
        else:
            if not os.path.isfile(self.modelPath) or not \
                   os.access(self.modelPath, os.R_OK):
                raise Exception("Model file doesn't " + \
                                "exist or is unreadable!")
            PATH_TO_CKPT = self.modelPath

        if self.labelMapPath == None or \
           self.labelMapPath == "":
            # List of the strings that is used to add correct label for each box.
            PATH_TO_LABELS = os.path.join('data',
                                          'mscoco_label_map.pbtxt'
                                          )
        else:
            if not os.path.isfile(self.labelMapPath) or not \
                   os.access(self.labelMapPath, os.R_OK):
                raise Exception("Model file doesn't exist" + \
                                " or is unreadable!")
            PATH_TO_LABELS = self.labelMapPath

        NUM_CLASSES = 90

        # Load a (frozen) Tensorflow model into memory.
        # Use pre-trained model
        global detection_graph
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        # Loading label map
        # Label maps map indices to category names, 
        # so that when our convolution network predicts `5`,
        # we know that this corresponds to `airplane`.  
        # Here we use internal utility functions,
        # but anything that returns a dictionary mapping integers 
        # to appropriate string labels would be fine
        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(
            label_map,
            max_num_classes=NUM_CLASSES,
            use_display_name=True
            )
        category_index = label_map_util.create_category_index(categories)
        return category_index

    # By default we use an "SSD with Mobilenet" model here.
    # See the [detection model zoo]
    # (https://github.com/tensorflow/models/blob/master/research/\
    # object_detection/g3doc/detection_model_zoo.md) 
    # for a list of other models that can be run out-of-the-box 
    # with varying speeds and accuracies.

    '''
    Detection process (Keep detecting if input stream continues)
    a.Startup tensorflow process and 
    b.Draw boxes around detected objects in the pictures/videos/camera
    stream with predicted name of the detected object and 
    percentage of correctness confidence

    Argument: 1. cap refers to the input to be detected 
              (can be images, videos, or streaming camera)
              2. imgflag refers to a boolean indicating 
              whether the input is a static image or not
              3. save Indicates whether users want to save the output
                 or not (True if so)
              4. savepath The path where users want to save their output
              5. test_video Indicates whether the process is called in a 
                 test or not. (True if so)
    Return: * -1 and the detected image in array form 
              if the process is to detect a static image
            * test_video flag (True if it's for test and false otherwise) 
              if the process is to detect a video or live camera
    '''
    def detect_process(self, cap, imgflag, save, savepath, test_video):
        category_index = self.model_setup()
        if save == True:
            fps = 30
            # this is the size of my source video
            capSize = (1024, 768)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.videoSave = cv2.VideoWriter(
                                    os.path.join(savepath, 
                                                 "savedOutputStream.mp4"
                                                 ),
                                    fourcc,
                                    fps,
                                    capSize,
                                    True
                                    )
        with detection_graph.as_default():
            with tf.Session(graph=detection_graph) as sess:
                # Definite input and 
                # output Tensors for detection_graph
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                # Each box represents a part of the image 
                # where a particular object was detected.
                detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                # Each score represent how level of confidence 
                # for each of the objects.
                # Score is shown on the result image, 
                # together with the class label.
                detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
                detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')

                # detection process loop
                while True:
                    # input is video or camera
                    if imgflag == False:
                        ret, frame = cap.read()
                        if ret == True:
                            image_np = frame
                        # If input stream is lost,
                        # terminate the process by return the last frame 
                        # that is after detection
                        else:
                            break
                    # input is a static image
                    else:
                        image_np = cap
                    # Expand dimensions since the model 
                    # expects images to have shape: [1, None, None, 3]
                    image_np_expanded = np.expand_dims(image_np, axis=0)
                    startper = time.perf_counter()
                    # Actual detection.
                    (boxes, scores, classes, num) = sess.run(
                        [
                            detection_boxes,
                            detection_scores,
                            detection_classes,
                            num_detections
                        ],
                        feed_dict={image_tensor: image_np_expanded}
                        )
                    endper = time.perf_counter()
                    # Visualization of the results of a detection.
                    image_done = vis_util.visualize_boxes_and_labels_on_image_array(
                        image_np,
                        np.squeeze(boxes),
                        np.squeeze(classes).astype(np.int32),
                        np.squeeze(scores),
                        category_index,
                        use_normalized_coordinates=True,
                        line_thickness=8)
                    # if input is an image, just return the detected version once it comes
                    # back from the tensorflow graph
                    if imgflag == True:
                        output_img = cv2.resize(image_done, (1024, 768))
                        global rate
                        rate = endper - startper
                        # return the test_val for image, image
                        return -1, output_img

                    else:
                        if test_video == True:
                            cv2.destroyAllWindows()
                            # return test
                            return test_video
                        image_resize = cv2.resize(image_done, (1024, 768))
                        cv2.imshow('object detection', image_resize)
                        if save == True:
                            start = time.clock()
                            self.videoSave.write(image_resize)
                        # Quit detection if user interrupts it by pressing the key 'q'
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            cap.release()
                            cv2.destroyAllWindows()
                            # return test
                            break
                if save == True:
                    self.videoSave.release()
                cap.release()
                cv2.destroyAllWindows()
                return test_video
                
