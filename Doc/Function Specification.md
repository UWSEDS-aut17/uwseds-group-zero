
## Problem Statement Summary
### Goal: Perform object detection on static photos, dynamic videos or live cameras.
1. Neural Network Object Detector
* Set up a repository of easily accessed the labeled training dataset(object-labelled pictures)
* Build a proper neural network via 'tensorflow' on python 3.5
* Use test dataset (labeled images) to get model accuracy; use connected web camera to evaluate detection speed.
2. Software Interface Construction
* Create an application with an interface so that users can choose one of the three options of input data form
* All three input options have a "Start" button for user to start the detection.
* Print a message indicating whether the input is loaded successful or not.
* Link the input from the interface to the algorithm and exhibit the output(labelled and visualized) on the interface
* Output may have two separate colums, one is the object-labelled result and the other is the original input, for comparison.
* Each input option will prompt the user to a new interface where the output is shown with a "Stop" button for the video and live camera options to stop playing and a "Return" button for all three options to return to the input interface, in case the user wants another job of detection. 
* Store output option for user
3. Software Test
* Unit tests are needed (for example, input loaded successful or not, test set or input doesn't have the object that the application can detect, wrong user interact actions, invalid user inputs, continual inputs, large inputs,etc)


## User Profile
*  User knows how to browse a web page and interact with an application interface. (Web UI)
*  User heard about machine learning and deep learning and knows they cannot behave 100% correct.  
*  User understands this model can only detect objects which have been fed to training process.
(The followings are what the users don't know---the techniques behind)
*  This application is excuted under the environment of python 3.5.
*  The object detector builds up a neural network by tensorflow and implements Faster-RCNN to precisely detect the objects in the screen(pictures, videos or streaming camera). 


## Elements of the problem statement
* How to read a photo/ a video/ a camera stream as a input.
* How to make the machine learn to recognize the objects we are interested in.
* How to find region proposals (regions we might be interested in) in a raw image.
* How to classify the object in a region proposal.
* How to revise the bounding box after recognizing a object. 


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

