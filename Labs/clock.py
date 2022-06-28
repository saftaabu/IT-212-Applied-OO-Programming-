# Syed Aftaabuddin
# Lab 2
# April 27, 2020

class Clock:

    #Initialize instance variables
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
        
    #Convert Clock object to str
        
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hr, self.min, self.sec)
        format(self.hr, self.min, self.sec)

    #Advance clock by one second, update
    #minutes and hours if necessary


    def tick(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
        if self.min == 60:
            self.hr = (self.hr + 1) % 24
            self.min = 0





