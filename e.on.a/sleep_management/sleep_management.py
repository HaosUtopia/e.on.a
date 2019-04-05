'''
The Prototype of the idea in python. In reality it should be implemented with
hardware using some hardware properties like interrupt and parallel computing to
deal with time and exchange data with sensors and UI(app).
'''


import time
from sleep_prepare import Prepare
from sleep_detection import Detection
from central_control.control import Control
from sleep_improvement import Improvement
from sleep_behavior import Behavior
from sleep_evaluation import Evaluation
from sensor import Audio, Accelerometer, Light

def set_time(time):
    start_time = time[0]
    finish_time = time[1]
    activate()

def activate():
    #called by app when sleep schedule is set
    act_flag = 1

def deactivate():
    act_flag = 0

def getTime():
    #get current time
    fmt = "%H %M"
    t = time.strftime(fmt,time.localtime())
    now = t.split(' ')
    now[0] = int(now[0])
    now[1] = int(now[1])
    return now

def main():
    Prepare prepare()
    Detection detection()
    Control control()
    Improvement improvement()
    Behavior behavior()
    Evaluation evaluation()
    while (1):#The time management should be optimized when implement to hardware
        room_condition = improvement.getParameter()
        while (act_flag == 1):
            time = getTime()#update time
            #prepare for sleep before sleep
            if (abs(time + 30 - start_time) < 1):
                prepare.activate()
                #The prepare period will be end once the light is shut down, then
                #start the sleep detection and control part
            #during sleeping, get sensor data and detect sleep quality and behavior
            elif (time > start_time and time < finish_time and prepare.getState() == 0):
                #get sensor data
                audio_data = Audio.getData()
                acc_data = Accelerometer.getData()
                #detect sleep quality and behavior
                detection.predict(audio_data, acc_data)
                behavior.updateBehavior([[audio_data],[acc_data]])
                if (control_start == 0):
                    #Get the best parameter for room
                    room_condition = improvement.getParameter()
                    #set the condition(temperature, humidity, CO2, pressure...)
                    #of the room and the control part will try to keep the room
                    #condition by controlling the heating, windows etc.
                    control.setCondition(room_condition)
                    control.start()
                    control_start = 1
            else:
                #get the sleep quality data
                predicted = detection.end()
                #clear data for next run
                detection.clear_data()
                #stop the control part
                control.end()
                control_start = 0
                #get behavior
                behavior_model = behavior.getBehavior()
                #evaluate sleep quality and give suggestion accordingly
                score = evaluation.evaluate(predicted, behavior_model)
                #train the model with sleep score
                improvement.train(score)
                deactivate()

if __name__ == '__main__':
    main()
