## Requirements ##
The data we need for this project is a set of precisely labeled images in the same scenario.

### Same scenario
Our learning algorithm focus on learning from images in one particular scenario. The choice of the scenario could be broad, which is decided by what we expect to detect after training the model. One of the most typical scenarios is the perception part in self-driving cars, which is to detect cars, pedestrian, road, etc from the perspective of cars on the road.

### Precisely labeled
The labels of images play a significant role in our project, which denotes the category and position of objects we would like to detect. The labels has to include the following information: objects' category number and the coordinates of their bounding boxes. Each image may contain multiple objects.

## Sources ##
### Road images from UCar Technology Inc.
There are 10000 labeled images in training set and 2000 unlabeled images in test set. There are 4 classes of objects: vehicle, pedestrian, cyclist and traffic lights. The coordinates of bounding boxes and class names are stored in a .idl file.

- Training_set: https://s3-us-west-2.amazonaws.com/us-office/competition/training.zip
- Test_set: https://s3-us-west-2.amazonaws.com/us-office/competition/testing.zip

### KITTI: Object Detection Evaluation 2012
The object detection and object orientation estimation benchmark consists of 7481 training images and 7518 test images, comprising a total of 80.256 labeled objects. All images are color and saved as png.
link: http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark

## Evaluation ##
|  Requirements | Road images from UCar Technology Inc. | KITTI: Object Detection Evaluation 2012|
| :------------------   |:-----------------:|:------:|
| Same Scenario | Yes |  Yes|
| Precisely labeled     | Yes    |Yes|                                            |
