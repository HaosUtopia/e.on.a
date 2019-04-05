import numpy as np
from keras.models import Sequential, load_model

class Detection:
    '''
    This class loads model which detect sleep quality(deep sleep, light sleep,
    awake) and snoring with sensor data(audio, accelerometer). The model is
    obtained from schlaflabor
    '''
    def __init__(self):
        self.model = Sequential()
        self.predicted_seq = []
        self.start()

    def load_model(self, filepath):
        print('Loading LSTM Model')
        self.model = load_model(filepath)

    def clear_data(self):
        self.predicted_seq = []

    def start(self):
        self.load_model('model/lstm_model.h5')

    def predict(self, audio_data, acc_data):
        data = audio_data + acc_data
        predicted = self.model.predict(data)
        self.predicted_seq.append(predicted)

    def end():
        return predicted_seq
