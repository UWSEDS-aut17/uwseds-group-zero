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
