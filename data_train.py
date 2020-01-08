import time
import imgs_ops
from Tkinter import *

class Train():
    def __init__(self):
        self.master_tk_ = Tk()

        self.num_training_iterations_ = 200 #1000 iterations to train data
        self.MovementThreshold_ = None

    #PUBLIC METHODS

    def train_data(self):

        b = Button(self.master_tk_, text="Start With Training", command=self.start_trining_)
        b.pack()
        self.master_tk_.mainloop()

        print("Finish")
        self.restart_tk_()

        return self.MovementThreshold_

    #PRIVATE METHODS

    def restart_tk_(self):
        time.sleep(0.3)
        self.master_tk_ = Tk()
        time.sleep(0.3)

    def start_trining_(self):
        print("Wait until training is completed...")
        print("PLEASE, DON'T MOVE ANYTHING IN FRONT OF CAMERA")
        time.sleep(2)

        mean_no_move = 0

        img = imgs_ops.Images(1)
        try:
            for i in range(0, self.num_training_iterations_):
                dep_value = img.update()
                mean_no_move = mean_no_move + dep_value
                print "Iteration ", i
        except KeyboardInterrupt:
            pass

        mean_no_move = mean_no_move / self.num_training_iterations_
        print(mean_no_move)

        print("PLEASE, NOW, MOVE IN FRONT OF CAMERA")
        time.sleep(2)

        mean_move = 0
        try:
            for i in range(0, self.num_training_iterations_):
                dep_value = img.update()
                mean_move = mean_move + dep_value
                print "Iteration ", i
        except KeyboardInterrupt:
            pass

        mean_move = mean_move / self.num_training_iterations_
        self.MovementThreshold_ = mean_move + mean_no_move / 2.0
        print(mean_move)
