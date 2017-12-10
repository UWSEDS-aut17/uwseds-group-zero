## Requirements ##
The data required for this project is a set of precisely labeled images in a particular scenario. 

- Same scenario  
Out machine focus on learning from images in a particular scenario. The choice of scenarios could be wide, which is decided by what we expect to detach after training the machine. One of the most typical scenarios is the perception part in self-driving cars, which is to recognize cars, pedestrian, road and etc from photos taken on the real road.
- Precisely labeled   
 Images' label plays a significant role in our project, which indicates the category and position of objects we eager to detach. The label for one particular image has to include the following information: objects' category names, the coordinates of their bounding box. Each image may contain more than one objects. 

## Sources ##
- Road images from UCar Technology Inc.  
There are 10000 labeled images in training set and 2000 unlabeled images in test set. There are 4 classes of objects: vehicle, pedestrian, cyclist and traffic lights. The coordinates of bounding boxes and class names are stored in a .idl file.  
Training_set: https://s3-us-west-2.amazonaws.com/us-office/competition/training.zip  
Test_set: https://s3-us-west-2.amazonaws.com/us-office/competition/testing.zip  
- KITTI: Object Detection Evaluation 2012  
The object detection and object orientation estimation benchmark consists of 7481 training images and 7518 test images, comprising a total of 80.256 labeled objects. All images are color and saved as png.
link: http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark

## Evaluation ##
|  Requirements | Road images from UCar Technology Inc. | KITTI: Object Detection Evaluation 2012|
| :------------------   |:-----------------:|:------:|
| Same Scenario | Yes |  Yes|
| Precisely labeled     | Yes    |Yes| 
                         
