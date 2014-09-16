#!/usr/bin/python

""" Fan control

Monitors the CPU temperature and controls PWM output connected to a fan
Use the /sys/class/thermal/thermal_zone0/temp to red the CPU temperature
and use the PWM to control fan speed. 

Function Wishlist
 
a) exits fan
b) 
"""

import os
import time

#constants declaration 
CONST_MIN_TEMP = 35
CONST_MAX_TEMP = 80
CONST_STEP_TEMP = 3

# CPUFAN Class
#CPUFAN is a class that monitors the temperature of the CPU and 
#control the speed of the cooling fan to cool off the CPU
class CPUFAN():
        
    def __init__(self, __DefaultName=None):
        
        #FIXME - add verbose/debug parsing code
        if __DefaultName == None:
            self.name = 'CPUFan'
        else:
            self.name = __DefaultName
            
        print "-INFO- :Creating CPUFAN object:", self.name,"\n"
        print "-INFO- :INIT DONE\n"

        #FIXME: check if fan on or off or available
        #       If exits, initialize fan 

        # Kick start with required vg to turn it ON
        
        f=os.popen('echo -n "4" > /sys/class/pwm/pwmchip0/export')
        f.close
        f=os.popen('echo -n "1000000" > /sys/class/pwm/pwmchip0/pwm4/period')
        f.close
        f=os.popen('echo -n "900000" > /sys/class/pwm/pwmchip0/pwm4/duty_cycle')
        f.close
        f=os.popen('echo -n "1" > /sys/class/pwm/pwmchip0/pwm4/enable')
        f.close

        # calculate total gears
        self.Gears = (CONST_MAX_TEMP - CONST_MIN_TEMP)/CONST_STEP_TEMP
        
    #Function to read the CPU temperature
    def ReadCPUTemperature(self):
        f=os.popen('cat /sys/class/thermal/thermal_zone0/temp')
        self.CPUTemperature = f.read()
        f.close()
        return int(self.CPUTemperature)/1000

    #Pick range and mapping to speed
    def FindGearLevel(self):

        #read temperature
        self.tempCelsius = self.ReadCPUTemperature()

        #find range 
        GearLevel = 0
        if (self.tempCelsius < CONST_MIN_TEMP):
            self.GearLevel = 0
        else:
            self.GearLevel = 1
            for i in range(CONST_MIN_TEMP, CONST_MAX_TEMP, CONST_STEP_TEMP):
                if (self.tempCelsius in range (i,i+CONST_STEP_TEMP)):
                    break
                else:
                    self.GearLevel+=1
    
        return self.GearLevel

    #fan control 
    def FanSpeedControl(self):
        self.GearLevel = self.FindGearLevel();
        
        if(self.GearLevel == 0):
            # Turn Off fan 
            print self.Gears
            # not required to turn ON the fan
            # turn OFF fan
            self.cmdstring = ('echo -n \"0\" > /sys/class/pwm/pwmchip0/pwm4/duty_cycle')
            return
        
        else:
            
            self.Offset = 400000 + self.GearLevel*600000/self.Gears
            print self.GearLevel
            print self.Gears
            
        self.cmdstring = ('echo -n \"' + str(self.Offset) + '\" > /sys/class/pwm/pwmchip0/pwm4/duty_cycle')
        print self.cmdstring
        print 'CPU temperature at ' + str(self.tempCelsius)

        f=os.popen(self.cmdstring)
        f.read()
        f.close

    def run(self):
        while 1:
            time.sleep(3)
            self.FanSpeedControl();




#run program
cpufanctrl = CPUFAN('cpufanctrl')
cpufanctrl.run()



  
    

    
    

        

    






