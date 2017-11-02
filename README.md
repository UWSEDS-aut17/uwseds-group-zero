## Project Discription ##

### Problem ##

Our projects aims at the real problem of objection detection and labeling, which will appear in fields like Robot manipulation, driverless car, etc.

1.) Behind the scene, we implement a neuro network to train the dataset and make object detections on new dataset by labeling them. If the correctness is good enough, then the trained dataset can be a new/reusable dataset for further reference. 

2.) We are trying to build a user interface and link the algorithm behind to the interface so that users can have 3 options --- detect ojects on a) a photo; b) a video; c) via live camera.

Potentially, there are several difficulties that need to be addressed:
1. Find the suitable parameters when building up the neuro network;
2. Precisely label objects in the training dataset;
3. Fix up settings and adjust labels when the accuracy is not ideal; 
4. Prove that the output(detected) dataset is reusable;
5. Successfully connect the UI to the algorithm and data;
6. Make unit tests on those 3 functionalities(photo, video, live camera); 
