# Component list
### Train  model
1. train_tfrecords_generation
2. train_config_generation
3. train
### Test(Evaluate) model
1. test_tfrecords_generation
2. test_config_generation
3. test evaluation
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
### Training model
1. train_tfrecords_generation
- Generate a tensorflow record (an input format in tensorflow) with image labels (containing class and bounding box).
- Input: .csv file which list all the train-set image names and objects' bounding box.
- Output: a train-set tfrecord file.
2. train_config_generation
- Generate a configuration file based on a sepecific algorithm, in this case, Faster-RCNN.
- Input: label_train.txt; Images
- Output: a .record file as config
3. train
- Get the training image trained in NN
- Input: label_test.txt; Images
- Output: an NN

### Test(Evaluate) model
1. test_tfrecords_generation (similar as above)
2. test_config_generation (similar as above)
3. test
- What it does: Test our NN.
- Input: label_test.txt; (Images)
- Output: result of object detection
4. test_evaluation
- What it does: Calculate the accuracy of our deep learning NN.
- Input: label_test.txt; (Output of objection detection from NN)
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
