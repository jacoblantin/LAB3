"""!
@file motor_driver.py
This file contians a class implementation to drive the ME 405 motors for use in lab01 and further labs.
This file also contains testing code to run the motor.

@author Jacob Lantin, Devon Lau, Filippo Maresca Denini
@date 21-Feb-2024

"""

import utime
import pyb

class MotorDriver:
    """!
    This class contains the constructor and methods for intializing and driving the ME 405 motors.
    The class allows for driving the motor at different speeds in either direction as well as allowing
    the user to disable the motor.
    """
    
    def __init__(self):
        """!
        This constructor initliazes the pins, timer, and timer channels for use in the motor driver.
        """        
        # configures timer for PWM
        pyb.Timer.PWM
        
        # configure pins B4 and B5 for output to motor driver
        pinIN1A = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
        pinIN2A = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
        
        # configure timer and channels
        tim3 = pyb.Timer(3, freq=1000)
        ch1 = tim3.channel(1, pyb.Timer.PWM, pin=pinIN1A)
        ch2 = tim3.channel(2, pyb.Timer.PWM, pin=pinIN2A)
    
        # configure pin A10
        pinENA = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
        
        # global variables
        self.ch1 = ch1
        self.ch2 = ch2
        self.pinENA = pinENA    
    
    def set_duty_cycle(self, level):
        """!
        This method sets the duty cycle for the motor to spin at.
        Negative values are allowed and thus spin the motor in the opposite direction.
        @param level - PWM level to set motor at
        """        
        # enables motor
        self.pinENA.high()
        
        # motor spins one direction
        if level > 0: 
            self.ch1.pulse_width_percent (level)
            self.ch2.pulse_width_percent (0)
        
        # motor spins other direction
        elif level < 0:
            self.ch1.pulse_width_percent (0)
            self.ch2.pulse_width_percent (abs(level))
            
    def disable_motor(self):
        """!
        This method disables the motor.
        """        
        # disables motor
        self.pinENA.low()


# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program.
if __name__ == "__main__":
    
    # initialize motor
    moe = MotorDriver()
    
    # drive motor forward
    moe.set_duty_cycle(25)
    
    
    
    
    