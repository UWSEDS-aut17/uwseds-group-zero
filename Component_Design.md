## Component list
### Training function
1. train_config_generation
2. train.py
### Test(Evaluate) function
1. test_config_generation
2. test.py
3. test_evaluation
### Software interface

### Camera interface

## Component specifications
### Training function
1. train_config_generation
- Transt the labeling info of all training images to a config file for train
- Input: label_train.txt; Images
- Output: a .record file as config
2. train.py
- Get the training image trained in NN
- Input: label_test.txt; Images
- Output: an NN

### Test(Evaluate) function
1. test_config_generation
- Transt the labeling info of all tseting images to a config file for train
- Input: label_test.txt; Images
- Output: a .record file as config
2. test.py
- Test our NN
- Input: label_test.txt; Images
- Output: result of object detection
3. test_evaluation
- Calculate the accuracy of our deep learning NN.
- Input: label_test.txt; Output of objection dection from NN
- Output: accuracy in percentage.
### Software interface

### Camera interface
