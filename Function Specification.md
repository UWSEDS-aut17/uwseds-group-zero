
## Problem Statement Summary
### Goal: Perform object detection on static photos and dynamic videos and live cameras.
1. Neural Network Object Detector
%* Perform object detection on static photos and dynamic videos and live cameras.
* Set up a repository of easily accessed the labelled trainning dataset(object-labelled pictures)
* Build a proper neural network via tensorflow on python 3.5
* Obtain testing dataset (picture without labels) to varify if the detector is robust and reliable
2. Software Interface Construction
* Create an application with an interface so that users can choose one of the three options of input data form
* All three input option have a "Start" button for user to start the detection.
* Print a message indicating whether the input is loaded successful or not.
* Link the input from the interface to the algorithm and exhibit the output(labelled and visualized) on the interface
* Output may have two separate colums, one is the object-labelled result and the other is the original input, for comparison.
* Each input option will prompt the user to a new interface where the output is shown with a "Stop" button for the video and live camera options to stop playing and a "Return" button for all three options to return to the input interface, in case the user wants another job of detection. 
* Store the output if the user wants
3. Software Test
* Unit tests are needed (for example, input loaded successful or not, test set or input doesn't have the object that the application can detect, wrong user interact actions, invalid user inputs, continual inputs, large inputs,etc)
%* Store the output if the user wants
%* Output may have two separate colums, one is the object-labelled result and the other is the original input, for comparison.
%* Each input option will prompt the user to a new interface where the output is shown with a "Stop" button for the video and live %camera options to stop playing and a "Return" button for all three options to return to the input interface, in case the user wants %another job of detection. 
%* All three input option have a "Start" button for user to start the detection.
%* Print a message indicating whether the input is loaded successful or not.

## User Profile
 (两个选择)
*  User knows how to browse a web page and interact with an application interface. (Web UI)
*  User needs to know how to execute a python file in command line. (UI)
*  User heard about machine learning and deep learning and knows they cannot behave 100% correct.
*  User should execute the application under the environment of python 3.5.
 (The followings are what the users don't know---the techniques behind)
*  The object detector builds up a neuro network by tensorflow and implements machine learning(deep learning) algorithm to learn to precisely detect the objects in the screen(pictures, videos or streaming camera)
(算法怎么实现比如神经元节点怎么处理，什么function要怎么设置之类的大腿补充一下)
*  ...
*  User can stop playing the output(just for video and live camera) and can also return to the input choosing interface by clicking "Return"
*  User can click "Start" button to start the detection if the input is successfully loaded.

## Elements of the problem statement
* Use the train data to build a dectector
* Use the test data to evaluate the detector
* Detect object from the input
* Read a photo/ a video/ a camera stream as a input

## Use cases
* User executes the python file in the command line to run the application. The application interface should show up and indicate there are three input options for user to choose.
 The app remains doing nothing until the user clicks "exit" button or  clicks one button out of three.
* When the user clicks the "photo" button, the application prompts the user to input a photo to be detected.
* When the user clicks the "video" button, the application prompts the user to input a video to be detected.
* When the user clicks the "live camera" button, the application will open the build-in camera of the user's laptop or the external camera connected to the computer that is running this application. Then the application will detect the object shown in the scene capture by the camera in real time and simultaneously shows it on the interface output area(left column) with the non-label live scene right next to it for comparison.
* After the user loads the input, the system will print out a message indicating whether it's successfully loaded and ready to start detection or not. 
* When the user clicks "Stop" button, the output of the video or the live camera will stop playing.
* When the user clicks "Return" button,  the application will prompt the use back to the very first interface for anthor detection if the user wants.
* When the user clicks the exit button or terminate the application in the command line, the application will be ended and disappear, so does the interface.

