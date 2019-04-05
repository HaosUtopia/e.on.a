import time
from central_control.control import Control

IDLE = 0
ENABLED = 1
DISABLED = 2

class Prepare:
	'''
	This class control the room condition to have faster and easier sleep/wakeup
	'''
	def __init__(self,Tstart,Tend,UserMode):
		self.Tstart = Tstart
		self.Tend = Tend
		self.UserMode = UserMode
		self.SystStat = IDLE

		self.Illuminance = 500
		self.LightColor = 5600
		self.Temp = 25

		self.ModTimeStart = self.Tstart
		self.ModTimeStart[0] = self.ModTimeStart[0]-1

		self.ModTimeEnd = self.Tend
		self.ModTimeEnd[0] = self.ModTimeEnd[0]-1
		self.room_condition = []#not defined

	def activate(self):
		self.SystStat = ENABLED

	def deactivate(self):
		self.SystStat = DISABLED

	def getState(self):
		return self.SystStat

	def getTime(self):
		fmt = "%H %M"
		t = time.strftime(fmt,time.localtime())
		now = t.split(' ')
		now[0] = int(now[0])
		now[1] = int(now[1])
		return now

	def compareTime(self,myTime):
		now = self.getTime();
		#print now,myTime
		print abs(now[0]*60+now[1]-myTime[0]*60-myTime[1])
		if(abs(now[0]*60+now[1]-myTime[0]*60-myTime[1])<60):
			return 1
		else:
			return 0

	def Update(self):

		now = self.getTime()

		#control the room condition
		if(self.compareTime(self.ModTimeStart)):
			Illuminance_tmp = (200-500)/(30)*(now[0]*60+now[1]-self.ModTimeStart[0]*60-self.ModTimeStart[1])+500
			#print now[0]*60+now[1]
			self.Illuminance = max([200,Illuminance_tmp])

			LightColor_tmp = (3000-5600)/(30)*(now[0]*60+now[1]-self.ModTimeStart[0]*60-self.ModTimeStart[1])+5600
			self.LightColor = max([3000,LightColor_tmp])

			Temp_tmp = (22-25)/(30)*(now[0]*60+now[1]-self.ModTimeStart[0]*60-self.ModTimeStart[1])+25
			self.Temp = max([22,Temp_tmp])

		if(self.compareTime(self.ModTimeEnd)):
			Illuminance_tmp = (300-0)/(0)*(now[0]*60+now[1]-self.ModTimeStart[0]*60-self.ModTimeStart[1])+0
			self.Illuminance = min([300,Illuminance_tmp])

			self.LightColor = 5600

			Temp_tmp = (22-25)/(30)*(now[0]*60+now[1]-self.ModTimeStart[0]*60-self.ModTimeStart[1])+25
			self.Temp = min([25,Temp_tmp])

		#print type(now[1]),type(now[0])
		if(now[0]*60+now[1]-self.ModTimeStart[0]*60-self.ModTimeStart[1]>30):
			self.SystStat = IDLE

		self.room_condition = [self.Illuminance, self.LightColor, self.Temp, self.SystStat...]
		control.setCondition(self.room_condition)
