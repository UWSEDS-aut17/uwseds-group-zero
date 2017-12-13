## Problem Statement Summary ##
### Goal ###
Build a user interface to perform object detection on static photos, dynamic videos or live cameras.

1. Neural Network Object Detector
* Set up a repository of easily accessed the labeled training dataset(object-labelled pictures)
* Build a proper neural network via 'tensorflow' on python 3.5
* Use test dataset (labeled images) to get model accuracy; use connected web camera to evaluate detection speed.

2. Software Interface Construction
* Create an application with an interface so that users can choose one of the three options of input data form
* Before starting the detection process, user is able to choose/specify their own model and label map file to start with.
  Otherwise, it will use the default model we set.
* For all inputs, including model file, label map file, image or video,
  interface will restrict the input file to be specific file type so that the detector won't crash with invalid inputs.
* Print a message indicating whether the input is loaded successful or not. 
  (Video stream or camera stream successfully opened or not)
* For static image, user can click the checkbox to see the rate of the process after the detection is finished.
* User can press 'q' to exit the detection process of video or live camera.
* User can also choose to save the output before kicking off the process.

3. Software Test
* Unit tests on those three options: image, video and camera. 
* They will test the functionality and the ability to handle invalid inputs.


## User Profile ##
*  User knows how to open a terminal and run a python file. (i.e ">>python3 user_interface.py" to run the interface)
*  User that is in the area of auto-driving research and wants to compare different algorithms 
   and models before going further in the next step of object detection.
*  User can have his/her own models (".pb" type) and label map files (".pbtxt" type) 
   and ".jpg" for image inputs, ".mp4"/".avi" for video inputs, built-in webcam for camera input.
*  User understands this model can only detect objects which have been fed to training process.
*  This application is excuted under the environment of python 3.5, tensorflow 1.4.0 and opencv2. (More details on README.md)


## Elements of the problem statement ##
* How to read a photo/ a video/ a camera stream as a input.
* How to make the model and label map to be flexible to change.
* How to make the machine learn to recognize the objects we are interested in.
* How to find region proposals (regions we might be interested in) in a raw image.
* How to classify the object in a region proposal.
* How to revise the bounding box after recognizing a object.
* How to time the process rate for images.
* How to save the result (of video/camera detection) as a video file for users.


## Use cases ##
### 1. Researchers in self-driving ###
Researchers come up with a new algorithm and have it trained a model. Before going further on applying this new algorihtm and model,
such as for box bounding (shrinking boxes around detected objects to fit the profile of that object) and 3D depth image,
researchers should first evaluate the algorithm they used and model they trained using that algorithm (how accurate and how fast it is).
* Firstly, it should be able to work nicely on static images. Then users can choose an image to see the output result. (Human's eyes are the most reliable test tools on pictures. But there is also percentage of confidence on classifying what the detected object is on the bounding box)
* Secondly, if it works well on images, it should be tested on videos to see if it's fast enough and still maintaining the accuracy. Then user can give a test video to the application to see the result.
* Finally, if it works also well on video, without further ado, it should be tested on live camera for real time streaming detection.
After all three detection processes, users should have quite an impression on how well their models and algorithms perform. Based on these results/feedbacks, researcher users can adjust their models, algorithms, or even datasets to make the detection better.

### 2. Researchers in object detection ###
Researchers want to choose the best algorithm and model to implement or further develop. They need to evaluate the performance of those algorithms and models in three scenarios, image, video and live camera.
* Firstly, input each model and its label map file to perform image detection, video detection and live camera detection.
* Secondly, results can be saved for future referrence.
* Thirdly, make evaluations (fastness, accuracy) based on the comparison of the outputs.
Then they can choose the best one based on their judgements after investigating the results.

