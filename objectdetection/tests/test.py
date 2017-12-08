import unittest
import cv2
import os
import sys
import numpy as np
sys.path.insert(0, '../')
from submodule import appfunction as appfun

class Object_detector_test(unittest.TestCase):
    # '''
    # This class tests main function used in this detector.
    # ''' 
    def test_input_image(self):
        img_input = "test_image.jpg"
        modelPath = '../submodule/ssd_mobilenet_v1_coco_11_06_2017/frozen_inference_graph.pb'
        labelMapPath = '../data/mscoco_label_map.pbtxt'
        testval, image_done = appfun.input_image(img_input, modelPath, labelMapPath, None)
        self.assertTrue(np.isclose(testval, -1))
    
    def test_input_cam(self):
        modelPath = '../ssd_mobilenet_v1_coco_11_06_2017/frozen_inference_graph.pb'
        labelMapPath = '../data/mscoco_label_map.pbtxt'
        self.assertTrue(np.isclose(appfun.input_cam(modelPath, labelMapPath, None, True), 1))

# if __name__ == '__main__':
#     unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(Object_detector_test)
unittest.TextTestRunner(verbosity=2).run(suite)