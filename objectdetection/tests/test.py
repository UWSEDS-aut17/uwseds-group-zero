import pathmagic  # noqa
# prevents pycodestyle/pep8 from complaining about an unused import.
import unittest
import cv2
import numpy as np
from function import appfunction as appfun
from . import user_interface as ui

'''
This class tests main functions of this detector.
'''


class Object_detector_test(unittest.TestCase):
    '''
    Test the function of detecting static image
    '''
    def test_input_image(self):
        img_input = "test_image.jpg"
        modelPath = '../ssd_mobilenet_v1_coco_11_06_2017' + \
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
        modelPath = '../submodule/ssd_mobilenet_v1_coco_11_06_2017/' + \
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
        modelPath = '../submodule/ssd_mobilenet_v1_coco_11_06_2017/' + \
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


# if __name__ == '__main__':
suite = unittest.TestLoader().loadTestsFromTestCase(Object_detector_test)
unittest.TextTestRunner(verbosity=2).run(suite)
