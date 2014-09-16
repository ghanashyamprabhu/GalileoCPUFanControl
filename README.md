GalileoCPUFanControl
====================
This project includes python code to control the PWM output of an 
Intel Galileo Gen 1 board so as to control the speed of the cooling 
fan attached on a DIY case for the Galileo itself. 
See picture at https://plus.google.com/102013789165949124655/posts/Pnabd8xvcce for DIY case

TODO - Fritzing Link for driver circuit.

The code is quite rudimentary at this point in time. 
The code runs a periodic check on the CPU temperature and locates an index of the temperature
Basic parameters include
	CONST_MAX_TEMP - maximum temperature
	CONST_MIN_TEMP - minimum temperature
	CONST_STEP_TEMP - value of the step size when analyzing the current CPU temperature

Once, the index is located, this is scaled to adjust the PWM duty cycle to control the voltage
at the GPIO - the GPIO drives the base of a P2222 transistor in common emitter configuration
which results in having a current gain at the collector on which the CPU Fan is connected

Math used here
	Minimum PWM value to keep the motor running  + (index / number of steps between min & max)* Rest of the PWM duty cycle span count
	
Testing and Validation 
As with all the open source code, if you are using my code, you are on whole 
and sole responsible for your board, beard and beer and what not. Don't blame me

Wishlist features 
a) enhance code to shut off motor if temperature below 
b) testing when CPU temperature exceeds max 
c) Polling should be on interrupt ? rather than based on sleep 


