import numpy as np

class Evaluation:
    '''
    This class uses sleep quality raw data to generate score and report
    '''
    def __init__(self):
        self.score = 0#current score number
        self.time = 0#current total sleep time
        self.awake_rate = 0#current percentage of time for awake
        self.lsleep_rate = 0#current percentage of time for light sleep
        self.dsleep_rate = 0#current percentage of time for deep sleep
        self.score_seq = np.array([])#history of score
        self.time_seq = np.array([])#history of sleep time
        self.awake_rate_seq = np.array([])#history of awake rate
        self.lsleep_rate_seq = np.array([])#history of light sleep
        self.dsleep_rate_seq = np.array([])#history of deep sleep
        self.behavior = []#behavior model

    def evaluate(self, predicted, behavior):
        #calculate the parameter for sleep and evaluate with them one time a day
        #in the morning
        predicted = np.array(predicted)
        awake = predicted[1,:] <= 0.3
        light_sleep = predicted[1,:] >= 0.3 and predicted[1,:] < 0.7
        deep_sleep = predicted[1,:] >= 0.7
        self.time = np.size(predicted, 1)
        self.awake_rate = np.size(awake, 1) / self.time
        self.lsleep_rate = np.size(light_sleep, 1) / self.time
        self.dsleep_rate = np.size(deep_sleep, 1) / self.time
        self.awake_rate_seq = np.append(self.awake_rate_seq, self.awake_rate)
        self.lsleep_rate_seq = np.append(self.lsleep_rate_seq, self.lsleep_rate)
        self.dsleep_rate_seq = np.append(self.dsleep_rate_seq, self.dsleep_rate)
        self.behavior = behavior
        #generate report and give suggestion
        self.one_day_report(awake, light_sleep, deep_sleep)
        self.long_term_report()
        self.expert_suggestion()

    def one_day_report(awake, light_sleep, deep_sleep):
        #analyze the one day data

    def long_term_report():
        #analyze the long term data(e.g. one month)

    def expert_suggestion(self):
        #use user's behavior model, analyze with behavior in the cloud and give
        #the expert suggestion
