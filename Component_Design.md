# Component list
### Training function
1. train_config_generation
2. train
### Test(Evaluate) function
1. test_config_generation
2. test
3. test_evaluation
### Software interface
1. read_photo 
2. read_vedio
3. read_live_camera
4. object_detect
5. detection_result
6. return

# Component specifications
### Training function
1. train_config_generation
- Transt the labeling info of all training images to a config file for train
- Input: label_train.txt; Images
- Output: a .record file as config
2. train
- Get the training image trained in NN
- Input: label_test.txt; Images
- Output: an NN

### Test(Evaluate) function
1. test_config_generation
- Transt the labeling info of all tseting images to a config file for train
- Input: label_test.txt; Images
- Output: a .record file as config
2. test
- Test our NN
- Input: label_test.txt; Images
- Output: result of object detection
3. test_evaluation
- Calculate the accuracy of our deep learning NN.
- Input: label_test.txt; Output of objection dection from NN
- Output: accuracy in percentage.
### Software interface
1. read_photo
* what it does: read a photo for detection.
* input: file path of the photo
* output: photo
2. read_video
* what it does: read a video for detection.
* input: file path of the video
* output: video
3. read_live_camera
* what it does: read a default live camera for detection.
* input: None
* output: video stream
4.  object_detect
*  what it does: detect object from a photo or a video or a live camera stream.
* input: read_photo / read_video / read_live_camera
* output: detection_result
5. return
* what it does: return to the original interface from the detection result
* input: Click
* output: None
