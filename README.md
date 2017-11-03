## Project Description

### Problem

Our projects aims at the problem of objection detection and labeling, this appears in fields like robot manipulation, self driving car, etc. We will first use the data to train a model, then use the model to detect four different objecs(vehicle, pedestrian, cyclist and traffic lights) with different media. 

![](/1.png)

1.) Behind the scene, we will implement a neural network to train on the labelled image dataset and perform object detections on the test dataset and labeling them. If the accuracy is good enough, then the trained dataset can be a new/reusable dataset for further reference.

2.) We are trying to build a user interface and link the algorithm behind to the interface so that users can have 3 options --- detect objects on a) a photo; b) a video; c) via live camera.

Potentially, there are several difficulties that need to be addressed:
1. Find the suitable parameters when building up the neural network;
2. Precisely label objects in the training dataset;
3. Fix up settings and adjust labels when the accuracy is not ideal;
4. Prove that the output(detected) dataset is reusable;
5. Successfully connect the UI to the algorithm and data;
6. Make unit tests on those 3 functionalities(photo, video, live camera);
