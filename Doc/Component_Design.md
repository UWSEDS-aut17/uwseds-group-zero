# Component list #
### Train model ###
Used as a default model in the application
1. train_tfrecords_generation
2. train_config_generation
3. train


### Software interface ###
1. model input
		--- user can use different models
2. label map input
		--- relates to each model used
3. save output
		--- user can save the video/camera detection output as a mp4 video file
4. show process rate
		--- user can check out the process rate for image when the detection is done
5. read in image
		--- user inputs a static image to test the performance of the model and algorithm
6. read in video
		--- user inputs a video file to test the performance of the model and algorithm
7. read in webcam
		--- user uses the webcam to test the performance of the model and algorithm in real time detection
8. quit
		--- user exits the application

# Component specifications #
### Training model ###
1. train_tfrecords_generation
- Generate a tensorflow record (an input format in tensorflow) with image labels (containing class and bounding box).
- Input: .csv file which list all the train-set image names and objects' bounding box.
- Output: a train-set tfrecord file.
2. train_config_generation
- Generate a configuration file based on a sepecific algorithm, in this case, Faster-RCNN.
- Input: label_train.txt; Images
- Output: a .record file as config
3. train
- Get the training image trained in NN
- Input: label_test.txt; Images
- Output: an NN


### Software interface ###
1. model input
* What it does: read in a pre-trained model.
* Name: askmodelfile(self, entry)
* Input: entry widget that relates to the "Browse" button clicked by user
* Output: the string of the path to the inputed model file
* How it works:
	ask user to indicate the path to the model file (".pb" type) when user clicks "Browse" button
	if the path is None or ""
		do nothing and return
	else
		reset the text in the entry widget to be the path
		record the string of that path

2. label map input
* What it does: read in a label map file.
* Name: asklabelfile(self, entry)
* Input: entry widget that relates to the "Browse" button clicked by user
* Output: the string of the path to the inputed label map file
* How it works:
	ask user to indicate the path to the label map file (".pbtxt" type) when user clicks "Browse" button
	if the path is None or ""
		do nothing and return
	else
		reset the text in the entry widget to be the path
		record the string of that path

3. save output
* What it does: read a default live camera for detection.
* Name: def outputvideopath(self)
* Input: whether the checkbox is checked or not
* Output: the string of the path that will save the output
* How it works:
	if the checkbox is checked
		ask user to indicate the path where to save the output video
		if the path is None or "" or invalid
			throw an Exception
		else
			reset the text in the entry widget to be the path
			record the string of that path
	else
		do nothing to the entry text and return

4. show process rate
* What it does: show the process rate in the entry text on the interface
* Name: def showprocessrate(self)
* Input: whether the checkbox is checked or not
* Output: the process rate in the text of the entry widget
* How it works:
	if the checkbox is checked
		if the rate is None or ""
			return
		else
			show the rate in the text of the entry widget
	else
		do nothing to the entry text and return

5. read in image
* What it does: read in image and pass it to the detection process
* Name: def askopenimgfile(self)
* Input: event action of the "Image" button
* Output: a window that shows the detected image
* How it works:
	ask user to indicate the path to the image file (".jpg" type) when user clicks "Image" button
	if the path is None or ""
		do nothing and return
	else
		pass the image path along with model path and label map path to the processor
		resize the output image and show it in a new window

6. read in video
* What it does: read in video and pass it to the detection process
* Name: def askopenvideofile(self)
* Input: event action of the "Iideo" button
* Output: a window that plays the detected video stream
* How it works:
	ask user to indicate the path to the video file (".mp4" and ".avi" type) when user clicks "Video" button
	if the path is None or ""
		do nothing and return
	else
		pass the video path along with model path and label map path to the processor
		if a stop signal passed back from the processor
			return

7. read in webcam
* What it does: open the webcam and pass it to the detection process
* Name: def askcam(self)
* Input: event action of the "Camera" button
* Output: a window that plays the detected real time camera stream
* How it works:
	pass the model path and label map path to the processor
	tell the processor to read the streaming from user's webcam
	record the stop signal passed back from the processor
	once stop signal is back
	return

8. quit
* What it does: quit the user interface
* Name: quit
* Input: Click the "Quit" button
* Output: None
* How it works:
	when the user click the "Quit" button
		exit the interface and close the python program
