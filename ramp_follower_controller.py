from controller import Robot
from controller import Motor
from controller import Altimeter
from controller import LED
import math



class MyController(Robot):
    def __init__(self):
        super(MyController, self).__init__()
        self.timeStep = 32  # set the control time step
        # get device tags
        # self.distanceSensor = self.getDistanceSensor('my_distance_sensor')
        # self.led = self.getLed('my_led')
        # self.distanceSensor.enable(timeStep)  # enable sensors to read data from them
        
        self.altimeter=self.getDevice("altimeter")
        self.altimeter.enable(self.timeStep)
        
        self.leftmotor = self.getDevice("left wheel motor");
        self.rightmotor = self.getDevice("right wheel motor");
        
        self.leftmotor.setPosition(math.inf);
        self.rightmotor.setPosition(math.inf);
        
        self.directionswitch = False;
        

    def run(self):
        while(self.step(self.timeStep) != 1):
            altitude = self.altimeter.getValue()
            
            if(not self.directionswitch):
                self.leftmotor.setVelocity(2.0);
                self.rightmotor.setVelocity(2.0);
                
                if(altitude <= 0.05):
                    self.directionswitch = True
            else:
                self.leftmotor.setVelocity(-2.0);
                self.rightmotor.setVelocity(-2.0);
                
                if(altitude >= 0.25):
                    self.directionswitch = False        
            
        
    
# main Python program
controller = MyController()
controller.run()
