import submodule.appfunction as af
import tkinter.filedialog
from tkinter import *
import tkinter as tk
import numpy as np
import PIL.ImageTk
import PIL.Image
from PIL import *
import cv2
import os

class ObjectDetection_ui(tk.Tk):

    def __init__(self):
        self.window = tk.Tk() 
        self.window.title("Object Detection")
        af.tf_version_check();
        self.modelPath = ""
        self.labelMapPath = ""

    # Open a file dialog asking for the input image file
    def askopenimgfile(self):
        path = filedialog.askopenfilename()
        # got back the detected image
        img_processed = af.input_image(path, self.modelPath, self.labelMapPath) 
        img = img_processed.resize((800, 600))
        photo = PIL.ImageTk.PhotoImage(img)
        # open the image in a new window
        self.new_window = tk.Toplevel()
        self.new_window.title("Image")
        self.img_import = Label(self.new_window, image=photo, height=600, width=800)
        self.img_import.pack(fill=BOTH, expand=YES)
        self.img_import.bind("<Configure>", lambda event, arg=img: self.resize_image(event, arg))
        self.img_import.pack(fill=BOTH, expand=YES)
        self.new_window.mainloop()

    # image resize related to the window size 
    def resize_image(self, event, img):
        w, h = event.width, event.height
        img_copy = img.copy()
        resize_img = img_copy.resize((w,h))
        photo = PIL.ImageTk.PhotoImage(resize_img)
        self.img_import.config(image=photo)
        self.img_import.image=photo #avoid garbage collection

    # Open a file dialog asking for the input video file
    def askopenvideofile(self):
        path = filedialog.askopenfilename()
        stop = af.input_video(path, self.modelPath, self.labelMapPath)
        if stop == True:
            return
    # Open the webcam of the user's laptop
    def askcam(self):
        stop = af.input_cam(self.modelPath, self.labelMapPath);
        # stop streaming and release the camera 
        # if window close or "q" is pressed
        if (stop == True):
            return
    
    # Delete the placeholder when new input is indicated
    def delete_placeholder(self, entry):
        entry.delete(0, END)
    # Open a file dialog asking for the model file
    def askmodelfile(self, entry):
        path = filedialog.askopenfilename()
        if not af.file_is_exist(path) or not os.access(path, os.R_OK):
            raise Exception("Model file doesn't exist or is unreadable!")
        self.delete_placeholder(entry)
        entry.insert(0, path)
        self.modelPath = path

    # Open a file dialog asking for the label map file
    def asklabelfile(self, entry):
        path = filedialog.askopenfilename()
        if not af.file_is_exist(path) or not os.access(path, os.R_OK):
            raise Exception("Label map file doesn't exist or is unreadable!")
        self.delete_placeholder(entry)
        entry.insert(0, path)
        self.labelMapPath = path

    # main function where the ui runs
    def main(self):
        self.group_1 = Frame(self.window)
        self.group_1.pack()
        self.modelGroup = Frame(self.group_1)
        self.modelGroup.pack(fill=X, expand=YES)
        self.labelGroup = Frame(self.group_1)
        self.labelGroup.pack(fill=X, expand=YES)
        # display the path of model used and label map data file
        custPath = StringVar(None)
        pretext_model = "Please indicate the path to your detection model (*.pbtxt)"
        self.model_path = Entry(self.modelGroup, width=54, textvariable=custPath)
        self.model_path.insert(0, pretext_model)
        self.model_path.pack(side=LEFT)
        self.model_path.bind("<Button-1>", lambda event, arg=self.model_path: self.delete_placeholder(arg))

        # browse for a model
        self.model_input = Button(self.modelGroup, text = "Browse", command = lambda: self.askmodelfile(self.model_path))
        self.model_input.pack(side=LEFT)

        # label map data file
        custPath_label = StringVar(None)
        pretext_label = "Please indicate the path to your label map file (*.pb)"
        self.label_path = Entry(self.labelGroup, width=54, textvariable=custPath_label)
        self.label_path.insert(0, pretext_label)
        self.label_path.pack(side=LEFT)
        self.label_path.bind("<Button-1>", lambda event, arg=self.label_path: self.delete_placeholder(arg))
        # browse for a label map file
        self.label_input = Button(self.labelGroup, text = "Browse", command = lambda: self.asklabelfile(self.label_path))
        self.label_input.pack(side=LEFT)

        # Buttons of 3 input-type options and Quit
        self.group_2 = Frame(self.window)
        self.group_2.pack(fill=X, expand=YES)
        self.group_btn = Frame(self.group_2)
        self.group_btn.pack()
        # define all buttons
        image_input = Button(self.group_btn, text = "Image", command = self.askopenimgfile)
        image_input.pack(side=LEFT)
        video_input = Button(self.group_btn, text = "Video", command = self.askopenvideofile)
        video_input.pack(side=LEFT)
        cam_input = Button(self.group_btn, text = "Camera", command = self.askcam)
        cam_input.pack(side=LEFT)
        quitBtn = Button(self.group_btn, text="Quit", command = quit)
        quitBtn.pack(side=LEFT)

        self.window.mainloop()

# start the user interface
start = ObjectDetection_ui()
start.main()

if __name__ == "__main__":
    ObjectDetection_ui().main()
