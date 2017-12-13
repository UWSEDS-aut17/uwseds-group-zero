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

#### Installing Opencv ####
In order to use the video input capturing property of opencv, here are some strategies that are provided for making opencv work like a charm. 
(Just for referencing, no guarantees. If want fully install, please directly go to the link in step 9.)
1. > cd (to any folder)
2. > git clone [link](https://github.com/Itseez/opencv.git)
3. > cd opencv
4. > mkdir release
5. > cd release
6. > cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -DPYTHON_EXECUTABLE=~/path/to/<my_virtualenv>/bin/python3.5 ..
7. > make
8. > sudo make install
9. For full installaiton, please refer to: [link](https://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/)
10. go back to the opencv git repo
11. > cd 3rdparty/ffmpeg
12. > cp opencv_ffmpeg_64.dll opencv_ffmpeg.dll to your opencv_dir/bin
13. copy this bin folder to ~/path/to/<my_virtualenv>/lib/python3.5/site-packages/cv2
14. run: export LD_LIBRARY_PATH=/ffmpeg_install_path/lib/
		 export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/ffmpeg_install_path/lib/pkgconfig
		 export PKG_CONFIG_LIBDIR=$PKG_CONFIG_LIBDIR:/ffmpeg_install_path/lib/
15. step 10 to 14 will be done after you install opencv to your device (if step1 to 9 doesnot install opencv successfully (validate by running import cv2 in a python file), try brew install to your machine and pip install in your virtualenv environment --- this works for me to read video file (avi and mp4) using cv2.VideoCapture())