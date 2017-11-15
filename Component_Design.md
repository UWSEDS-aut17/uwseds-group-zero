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
2. read_video
3. read_live_camera
4. object_detect
5. effect showcase
6. team info
7. reference
8. return

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
- What it does: Transt the labeling info of all tseting images to a config file for train.
- Input: label_test.txt; Images
- Output: a .record file as config
2. test
- What it does: Test our NN.
- Input: label_test.txt; (Images)
- Output: result of object detection
3. test_evaluation
- What it does: Calculate the accuracy of our deep learning NN.
- Input: label_test.txt; (Output of objection dection from NN)
- Output: accuracy in percentage
### Software interface
1. read_photo
* What it does: read a photo for detection.
* Input: file path of the photo
* Output: photo
2. read_video
* What it does: read a video for detection.
* Input: file path of the video
* Output: video
3. read_live_camera
* What it does: read a default live camera for detection.
* Input: None
* Output: video stream
4. object_detect
* What it does: detect object from a photo or a video or a live camera stream.
* Input: read_photo / read_video / read_live_camera
* Output: detection_result
5. effect showcase
* What it does: simply show some pictures of the detection effect (boxed around the detected object).
* Input: client clicking the button
* Output: a well-chosen picture with detected objects
6. team info
* What it does: list out each member of our team with their own ambitious.
* Input: client clicking the button
* Output: the info of our team
7. reference
* What it does: list out the materials that we referred.
* Input: client clicking the button
* Output: the references used in this project
8. return
* What it does: return to the original interface from the detection result
* Input: Click
* Output: None
