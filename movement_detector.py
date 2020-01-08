#MAIN PROGRAM
import imgs_ops
import data_train
import time

class Timer():
    def __init__(self, freq):
        self.t0_ = time.time()
        self.tf_ = None
        self.freq_ = freq

    def sleep(self):

        self.tf_ = time.time()
        elapsed = self.tf_ - self.t0_
        t = 1.0 / float(self.freq_)
        wait_time = t - elapsed
        self.t0_ = self.tf_ + wait_time
        if(wait_time > 0):
            time.sleep(wait_time)


if __name__ == "__main__":

    data_learning = data_train.Train()
    MovementThreshold_ = None

    try:

        MovementThreshold_ = data_learning.train_data()

        img = imgs_ops.Images(MovementThreshold_, output= True)

        #Reactive system
        rate = Timer(20) #20 Hz
        while(1):

            img.update()
            print("Update\n")
            rate.sleep()

    except KeyboardInterrupt:
        pass
