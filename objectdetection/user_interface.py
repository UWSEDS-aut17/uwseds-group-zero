import sys
import os
# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
# import submodule.appfunction as af
# import submodule.object_detection_main as od
from function import appfunction as af
from function import object_detection_main as od
import tkinter.filedialog
from tkinter import *
import tkinter as tk
import numpy as np
import PIL.ImageTk
import PIL.Image
from PIL import *
import cv2

'''
Class for an object detection user interface
'''


class ObjectDetection_ui(tk.Tk):

    '''
    Initialization of the ui window
    '''

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Object Detection")
        af.tf_version_check()
        self.modelPath = ""
        self.labelMapPath = ""
        self.savepath = ""

    '''
    Open a file dialog asking for the input image file
    When the entry button is clicked
    '''

    def askopenimgfile(self):
        path = filedialog.askopenfilename(
            filetypes=(
                ("jpeg files", "*.jpg"),
                ("all files", "*.*")
                )
            )
        if path is None or path == "":
            return
        save = False
        if self.var.get() == 1:
            save = True
        # got back the detected image
        img_processed, testval = af.input_image(path,
                                                self.modelPath,
                                                self.labelMapPath,
                                                self.savepath,
                                                save
                                                )
        img = img_processed.resize((800, 600))
        photo = PIL.ImageTk.PhotoImage(img)
        # open the image in a new window
        self.new_window = tk.Toplevel()
        self.new_window.title("Image")
        self.img_import = Label(self.new_window,
                                image=photo,
                                height=600,
                                width=800)
        self.img_import.pack(fill=BOTH, expand=YES)
        self.img_import.bind("<Configure>",
                             lambda event, arg=img:
                             self.resize_image(event, arg))
        self.img_import.pack(fill=BOTH, expand=YES)
        self.new_window.mainloop()

    '''
    Image resizing dynamically to the window size
    '''

    def resize_image(self, event, img):
        w, h = event.width, event.height
        img_copy = img.copy()
        resize_img = img_copy.resize((w, h))
        photo = PIL.ImageTk.PhotoImage(resize_img)
        self.img_import.config(image=photo)
        self.img_import.image = photo  # avoid garbage collection

    '''
    Open a file dialog asking for the input video file
    When the entry button is clicked
    '''

    def askopenvideofile(self):
        path = filedialog.askopenfilename(
            filetypes=(
                ("mp4 files", "*.mp4"),
                ("avi files", "*.avi"),
                ("all files", "*.*")
                )
            )
        if path is None or path == "":
            return
        stop = af.input_video(path,
                              self.modelPath,
                              self.labelMapPath,
                              self.savepath,
                              False)
        if stop is True:
            return

    '''
    Open the webcam of the user's laptop
    When the entry button is clicked
    '''

    def askcam(self):
        stop = af.input_cam(self.modelPath,
                            self.labelMapPath,
                            self.savepath,
                            False)
        return

    '''
    Delete the placeholder of the given entry
    when new input is indicated
    '''

    def delete_placeholder(self, entry):
        entry.delete(0, END)

    '''
    Open a file dialog asking for the model file
    '''

    def askmodelfile(self, entry):
        path = filedialog.askopenfilename(
            filetypes=(
                ("pb files", "*.pb"),
                ("all files", "*.*")
                )
            )
        if path is None or path == "":
            return
        self.delete_placeholder(entry)
        entry.insert(0, path)
        self.modelPath = path

    '''
    Open a file dialog asking for the label map file
    When the entry button is clicked
    '''

    def asklabelfile(self, entry):
        path = filedialog.askopenfilename(
            filetypes=(
                ("pbtxt files", "*.pbtxt"),
                ("all files", "*.*")
                )
            )
        if path is None or path == "":
            return
        self.delete_placeholder(entry)
        entry.insert(0, path)
        self.labelMapPath = path

    '''
    Specify the output path that is indicated by the user
    '''

    def outputvideopath(self):
        if self.var.get() == 1:
            self.savepath = filedialog.askdirectory()
            if (self.savepath is None or
                    self.savepath == "" or
                    os.path.isdir(self.savepath) is False):
                raise Exception("Invalid path!")
            self.video_out_path.configure(state='normal')
            self.delete_placeholder(self.video_out_path)
            self.video_out_path.insert(0, self.savepath)
            # pass to saving the output as a video
        else:
            self.delete_placeholder(self.video_out_path)
            self.video_out_path.insert(0, self.videoOutText)
            self.video_out_path.configure(state='disabled')
            return

    '''
    Print the rate of processing in the entry
    if the user checks the checkbox button after
    detection is over
    '''

    def showprocessrate(self):
        if self.rate_var.get() == 1:
            rate_copy = od.rate
            if rate_copy is None or str(rate_copy) == "":
                return
            self.rate_out.configure(state='normal')
            self.delete_placeholder(self.rate_out)
            outrate = StringVar(None)
            outrate = "Rate is: " + \
                str(round(rate_copy, 2)) + \
                " seconds."
            self.rate_out.insert(0, outrate)
            self.rate_out.configure(state='readonly')
        else:
            self.rate_out.configure(state='normal')
            self.delete_placeholder(self.rate_out)
            tmp = StringVar(None)
            tmp = "Rate of Processing per Image (s)."
            self.rate_out.insert(0, tmp)
            self.video_out_path.configure(state='readonly')
            return

    '''
    Main function where the ui runs
    '''

    def main(self):
        self.group_1 = Frame(self.window)
        self.group_1.pack()
        self.modelGroup = Frame(self.group_1)
        self.modelGroup.pack(fill=X, expand=YES)
        self.labelGroup = Frame(self.group_1)
        self.labelGroup.pack(fill=X, expand=YES)
        self.videoout = Frame(self.group_1)
        self.videoout.pack(fill=X, expand=YES)
        self.rate = Frame(self.group_1)
        self.rate.pack(fill=X, expand=YES)
        # display the path of model used and label map data file
        custPath = StringVar(None)
        pretext_model = "Please indicate the path" + \
            "to your detection model (*.pb)"
        self.model_path = Entry(self.modelGroup,
                                width=54,
                                textvariable=custPath)
        self.model_path.insert(0, pretext_model)
        self.model_path.pack(side=LEFT)
        self.model_path.bind("<Button-1>",
                             lambda event,
                             arg=self.model_path:
                             self.delete_placeholder(arg)
                             )

        # browse for a model
        self.model_input = Button(self.modelGroup,
                                  text="Browse",
                                  command=lambda:
                                  self.askmodelfile(self.model_path)
                                  )
        self.model_input.pack(side=LEFT)

        # label map data file
        custPath_label = StringVar(None)
        pretext_label = "Please indicate the path" + \
            "to your label map file (*.pbtxt)"
        self.label_path = Entry(self.labelGroup,
                                width=54,
                                textvariable=custPath_label)
        self.label_path.insert(0, pretext_label)
        self.label_path.pack(side=LEFT)
        self.label_path.bind("<Button-1>",
                             lambda event,
                             arg=self.label_path:
                             self.delete_placeholder(arg)
                             )
        # browse for a label map file
        self.label_input = Button(self.labelGroup,
                                  text="Browse",
                                  command=lambda:
                                  self.asklabelfile(self.label_path)
                                  )
        self.label_input.pack(side=LEFT)

        # Entry path for saving the output video file
        self.videoOutText = StringVar(None)
        self.videoOutText = "Please indicate the path" + \
            "to output the saved video file."
        self.video_out_path = Entry(self.videoout,
                                    width=54,
                                    textvariable=self.videoOutText)
        self.video_out_path.insert(0, self.videoOutText)
        self.video_out_path.configure(state="disabled")
        self.video_out_path.pack(side=LEFT)
        self.video_out_path.bind("<Button-1>",
                                 lambda event,
                                 arg=self.video_out_path:
                                 self.delete_placeholder(arg)
                                 )
        # Checkbutton for whether output an video or not
        self.var = IntVar()
        self.video_out = Checkbutton(self.videoout,
                                     text="Save Video Output",
                                     variable=self.var,
                                     command=self.outputvideopath
                                     )
        self.video_out.pack(side=LEFT)

        # Rate for image processing
        self.rate_text = StringVar(None)
        self.rate_text = "Rate of Processing per Image (s)."
        self.rate_out = Entry(self.rate,
                              width=30,
                              textvariable=self.rate_text
                              )
        self.rate_out.insert(0, self.rate_text)
        self.rate_out.configure(state="readonly")
        self.rate_out.pack(side=LEFT)
        # Checkbutton for whether show the rate of processing an image ot not
        self.rate_var = IntVar()
        self.rate_btn = Checkbutton(self.rate,
                                    text="Show process rate" +
                                    "(Check after detection is finished)",
                                    variable=self.rate_var,
                                    command=self.showprocessrate
                                    )
        self.rate_btn.pack(side=LEFT)

        # Buttons of 3 input-type options and Quit
        self.group_2 = Frame(self.window)
        self.group_2.pack(fill=X, expand=YES)
        self.group_btn = Frame(self.group_2)
        self.group_btn.pack()
        # define all buttons
        image_input = Button(self.group_btn,
                             text="Image",
                             command=self.askopenimgfile
                             )
        image_input.pack(side=LEFT)
        video_input = Button(self.group_btn,
                             text="Video",
                             command=self.askopenvideofile
                             )
        video_input.pack(side=LEFT)
        cam_input = Button(self.group_btn,
                           text="Camera",
                           command=self.askcam
                           )
        cam_input.pack(side=LEFT)
        quitBtn = Button(self.group_btn,
                         text="Quit",
                         command=quit
                         )
        quitBtn.pack(side=LEFT)

        self.window.mainloop()


if __name__ == "__main__":
    ObjectDetection_ui().main()
