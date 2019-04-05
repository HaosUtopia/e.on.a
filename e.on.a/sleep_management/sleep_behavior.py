import numpy as np

class Behavior:
    '''
    This class uses sensor data to train a marcov chain with deep learning, which
    can represant humans behavior. The observed behavior can identify people and
    give suggestion accordingly
    '''
    def __init__(self):
        self.behavior = []#behavior model(not defined)

    def getBehavior(self):
        return self.behavior

    def updateBehavior(self, data):
        #use Multisensor kalmanfilter with deep learning to update the behavior
        #model
