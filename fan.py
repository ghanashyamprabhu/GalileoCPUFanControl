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



class CPUFAN():
    
    
    
    def __init__(self, __DefaultName=None):
        
        """
        FIXME - add verbose/debug parsing code
        """
        if __DefaultName == None:
            self.name = "CPUFan"
        else:
            self.name = __DefaultName
            
    print "Initializing cpu fan object:". self.name
        

    
    """ 
    CPUFAN is a class that monitors the temperature of the CPU and 
    control the speed of the cooling fan to cool off the CPU
    """

    
    """
    function to read the CPU temperature
    """
    def ReadCPUTemperature(self):
        f=os.popen('cat /sys/class/thermal/thermal_zone0/temp')
        CPUTemperature = f.read()
        f.close()
        
        return CPUTemperature

    """pick range and mapping to speed"""
    
    """set run loop"""


cpufanctrl = CPUFAN(self, "cpufanctrl")    
    

    
    

        

    






