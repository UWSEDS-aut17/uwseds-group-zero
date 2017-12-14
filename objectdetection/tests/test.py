from . import pathmagic  # noqa
# prevents pycodestyle/pep8 from complaining about an unused import.
import unittest
import cv2
import numpy as np
from function import appfunction as appfun
from function import object_detection_main as od
from objectdetection import user_interface as ui

'''
This class tests main functions of this detector.
'''

modelPath = '../function/ssd_mobilenet_v1_coco_11_06_2017/' + \
                    'frozen_inference_graph.pb'
labelMapPath = '../data/mscoco_label_map.pbtxt'


class Object_detector_test(unittest.TestCase):

    global modelPath
    global labelMapPath
    '''
    Test the function of detecting static image
    '''
    def test_input_image(self):
        img_input = "test_image.jpg"
        modelPath = '../function/ssd_mobilenet_v1_coco_11_06_2017' + \
                    '/frozen_inference_graph.pb'
        labelMapPath = '../data/mscoco_label_map.pbtxt'
        image_done, testval = appfun.input_image(img_input,
                                                 modelPath,
                                                 labelMapPath,
                                                 "",
                                                 False
                                                 )
        self.assertTrue(np.isclose(testval, -1))

    '''
    Test the function of detecting video
    '''
    def test_input_video(self):
        modelPath = '../ssd_mobilenet_v1_coco_11_06_2017/' + \
                    'frozen_inference_graph.pb'
        labelMapPath = '../data/mscoco_label_map.pbtxt'
        video_file = 'test_video.mp4'
        self.assertTrue(
            np.isclose(appfun.input_video(video_file,
                                          modelPath,
                                          labelMapPath,
                                          "",
                                          True
                                          ), 1)
            )

    '''
    Test the function of detecting live camera
    '''
    def test_input_cam(self):
        modelPath = '../function/ssd_mobilenet_v1_coco_11_06_2017/' + \
                    'frozen_inference_graph.pb'
        labelMapPath = '../data/mscoco_label_map.pbtxt'
        self.assertTrue(
            np.isclose(appfun.input_cam(modelPath,
                                        labelMapPath,
                                        "",
                                        True
                                        ), 1)
            )

    '''
    Test the helper function of detecting video/live camera
    '''
    def test_video_open(self):
        modelPath = '../function/ssd_mobilenet_v1_coco_11_06_2017/' + \
                    'frozen_inference_graph.pb'
        labelMapPath = '../data/mscoco_label_map.pbtxt'
        cap = cv2.VideoCapture("")
        with self.assertRaises(Exception):
            appfun.video_open(cap,
                              False,
                              modelPath,
                              labelMapPath,
                              "",
                              True)
        self.assertTrue(True)

    '''
    Test the function of tf_check
    in object_detection_main.py
    '''
    def test_tf_check(self):
        appfun.tf_version_check()

    '''
    Test the function of file_is_exist
    in object_detection_main.py
    '''
    def test_file_is_exit(self):
        self.assertFalse(appfun.file_is_exist(''))

    '''
    Test the function of model_setup
    in object_detection_main.py
    '''
    def test_objectdetection(self):
        self.assertIsNotNone(od.objectDetection(
            modelPath,
            labelMapPath
            ).model_setup()
                            )

    '''
    Test the function of detect_process of image
    in object_detection_main.py
    '''
    def test_detect_process_img(self):
        testval, imgarray = od.objectDetection(
            modelPath,
            labelMapPath
            ).detect_process(cv2.imread("test_image.jpg"),
                             True,
                             False,
                             "",
                             False
                             )
        self.assertEqual(testval, -1)

    '''
    Test the function of detect_process of video
    in object_detection_main.py
    '''
    def test_detect_process_video(self):
        self.assertTrue(
          od.objectDetection(
              modelPath,
              labelMapPath
                            ).detect_process(
                                cv2.VideoCapture("test_video.mp4"),
                                False,
                                False,
                                "",
                                True
                                )
        )

    '''
    Test the function of detect_process of webcam
    in object_detection_main.py
    '''
    def test_detect_process_cam(self):
        self.assertTrue(
          od.objectDetection(
              modelPath,
              labelMapPath).detect_process(cv2.VideoCapture(0),
                                           False,
                                           False,
                                           "",
                                           True
                                           )
                     )


# if __name__ == '__main__':
suite = unittest.TestLoader().loadTestsFromTestCase(Object_detector_test)
unittest.TextTestRunner(verbosity=2).run(suite)
