## Project Description

### Problem

Our projects aims at the problem of objection detection and labeling, this appears in fields like robot manipulation, self driving car, etc. We will first use the data to train a model, then use the model to detect four different objecs(vehicle, pedestrian, cyclist and traffic lights) with different media.

![](/1.png)

1.) Behind the scene, we will first implement a neural network to train on the labelled image dataset and perform object detections on the test dataset and labeling them. Let it be our pre-trained model.

2.) Nowadays, there are many algorithms of deep neuro network, specially on object detection. People should know how their model behaves and how fast does it perform when being applied in a real detection process, before going further in object detection research (i.e narrowing down the boxes, 3D detection, etc). Then we decided to build a handy tool of this topic so that researcher users can evaluate their models, trained by a specific algorithm.

3.) We are trying to build a user interface and link the algorithm behind to the interface so that users can have 3 options --- detect objects on a) a photo; b) a video; c) via live camera.

Potentially, there are several difficulties that need to be addressed:
1. Trained our model and setup the tensorflow neuro net for detection;
2. Precisely label objects in the training dataset --- nice label map data are needed;
3. Fix up settings and configurations for ourselves;
4. Setup cloud environment to use GPU in training;
4. Build a user interface as a handy tool for evauate deep neuro net models.
5. Make the ui more interactive with more flexible setup options --- choosing user's own model and data, saving output, etc;
6. Make unit tests on those 3 functionalities(photo, video, live camera);

### Environment Requirements
* Pip (and Pip3)
* Python3.5
* Tensorflow1.4.0
* Pillow
* Opencv
* Tkinter
* matplotlib
* pycodestyle

### Usage ###
Go into the folder of uwseds-group-zero as the root of our application. Run the following code.
* > python3 setup.py install </br>
--- this should install all required packages so that our application can be run.
* > cd objectdetection </br>
--- where our interface python file lives
* > python3 user_interface.py </br>
--- execute the interface
Then our interface of the object detection application should show up for user.

#### Installing Opencv ####
In order to use the video input capturing property of opencv, here are some strategies that are provided for making opencv work like a charm.
(Just for referencing, no guarantees. If want fully install, please directly go to the link in step 9.)
1. > cd (to any folder)
2. > git clone https://github.com/Itseez/opencv.git
3. > cd opencv
4. > mkdir release
5. > cd release
6. > cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -DPYTHON_EXECUTABLE=~/path/to/<my_virtualenv>/bin/python3.5 ..
7. > make
8. > sudo make install
9. For full installaiton, please refer to: https://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/
10. Go back to the opencv git repo
11. > cd 3rdparty/ffmpeg
12. > cp opencv_ffmpeg_64.dll opencv_ffmpeg.dll to your opencv_dir/bin
13. Copy this bin folder to ~/path/to/<my_virtualenv>/lib/python3.5/site-packages/cv2
14. Run: </br>
		 * export LD_LIBRARY_PATH=/ffmpeg_install_path/lib/ </br>
		 * export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/ffmpeg_install_path/lib/pkgconfig </br>
		 * export PKG_CONFIG_LIBDIR=$PKG_CONFIG_LIBDIR:/ffmpeg_install_path/lib/ </br>
15. Step 10 to 14 will be done after you install opencv to your device (if step1 to 9 doesnot install opencv successfully (validate by running import cv2 in a python file), try brew install to your machine and pip install in your virtualenv environment --- this works for me to read video file (avi and mp4) using cv2.VideoCapture())

### Test ###
* Go into the tests folder in objectdetection directory
* Run nosetests --with-coverage test.py
* If want to run: python3 test.py, change the first line of importing in test.py to be: "import pathmagic  # noqa" to aviod import issue

Feedback to instructor's suggestion of testing our user_interface.py: 

- For the test of all UI functions, when we tried to test them (i.e., askopenimgfile(), resize_image(), askopenvideofile(), askcam(), delete_placeholder(), askmodelfile(), asklabelfile(), outputvideopath()), we found it's really hard to give a real input and test the result, because the input should be the dynamic interface and output is also function of actions like showing, bindding. 
- On the other part, in these UI functions, the packages we used include tkinter, PIL, cv2 and appfunction.py (written by our own). For tkinter, PIL and cv2, they are all well-developed packages, and there are uinittests for appfunction.py. 

- For the issue of wrong file types, we limited the file types in the input function, i.e. jpg for image, avi & mp4 for video, .pbtxt for labelmap and .pb for object detection frozen model. So wrong file type will not be expected to appear.

In conclusion, because we suppose our UI interface is robost enough and UI interface test will destroy our function structure, we decided not to test the functions in UI.


### Example ###
In the example folder, the Example.md is the thorough usage guidance of our application --- how to interact with the user interface to get desired results.

If user wants to use the main functions live in appfunction.py in uwseds-group-zero/function which contains the main functionalities of our app in the source code, there is a simple ipython jupyter notebook example.ipynb for reference.
User can also refer to the function specification in Doc/ for more details.
