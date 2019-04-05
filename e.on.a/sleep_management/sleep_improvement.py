import numpy as np

class Improvement:
    '''
    This class is used to find the best condition for person to sleep with MLE.
    Assume sleep quality is influenced by temperature, humidity, CO2, pressure...
    and obey Multivariate Gaussian Distribution with each variate independent
    with each other.
    '''
    def __init__(self):
        self.min_temp = 18#max temperature
        self.max_temp = 23#min temperature
        self.best_temp = 20#best temperature
        self.min_humi = 45
        self.max_humi = 65
        self.best_humo = 50
        self.min_CO2 = 0.05
        self.max_CO2 = 0.1
        self.best_CO2 = 0.05
        self.cov = [[1,0,0],[0,3,0],[0,0,0.002]]#covariance matrix for Gaussian Distribution
        self.data = np.array([])#history of daily data
        self.score = np.array([])#history of sleep quality

    def getParameter(self):
        parameter = np.random.multivariate_normal([self.best_temp, self.best_humo, self.best_CO2], \
        cov)
        #limit the parameter in the range of comfort
        parameter = np.maximum(parameter, [self.min_temp, self.min_humi, self.min_CO2])
        parameter = np.minimum(parameter, [self.max_temp, self.max_humi, self.max_CO2])
        np.append(self.data, [parameter])#save the parameter
        return parameter

    def train(self, score):
        #reduce the cov to gradually close to best parameter as we get more data
        self.cov = self.cov * 0.95
        np.append(self.score, score)
        self.best_temp, self.best_humo, self.best_CO2 = self.MLE(self.data, self.score)

    def MLE():
        #MLE algorithm
