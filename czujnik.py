#--------------------------------------------------------------------------------------------------------------#
#                                               BIBLIOTEKI                                                     #
#--------------------------------------------------------------------------------------------------------------#
import os
import sys

#--------------------------------------------------------------------------------------------------------------#
#                                      INICJALIZACJA KLAS I FUNKCJI                                            #
#--------------------------------------------------------------------------------------------------------------#

class DistanceSensor:

    def __init__(self, model:str, max_distance:float, current_distance:float):
        self.model = model
        self.max_distance = max_distance
        self.current_distance = max_distance

    def update_reading(self, new_value:float):
        self.new_value = new_value
        if self.new_value != self.current_distance and self.new_value >= 0:
            self.current_distance = new_value
        elif self.new_value < 0:
            self.current_distance = 0
        else:
            print(f"ERROR")

    def __str__(self) -> str:
        return f"{self.model} // Zasięg: {self.max_distance} mm // Aktualny odczyt: {self.current_distance} mm"

class RobotArm:

    def __init__(self, model:str, xpos:float, ypos:float, zpos:float):
        self.model = model
        self.xpos = 0.0
        self.ypos = 0.0
        self.zpos = 0.0

    def __str__(self) -> str:
        return f"[{self.model}] Aktualna pozycja: X:{self.xpos}|Y:{self.ypos}|Z:{self.zpos}"

    def move(self, distance:float):
        self.xpos += distance
        self.ypos += distance
        self.zpos += distance

class RobotGripper:

    def __init__(self, number: int, max_force: float, current_force: float, is_closed: bool, stan: str):
        self.max_force = max_force
        self.current_force = current_force
        self.is_closed = 0
        self.stan = "CLOSED"
        self.number = number

    def __str__(self) -> str:
        return f" // Maksymalna siła: {self.max_force} N // Stan: {self.stan}"

class Robot(RobotArm, RobotGripper):
    pass

#--------------------------------------------------------------------------------------------------------------#
#                                               MAIN                                                           #
#--------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    sensor_yaka = DistanceSensor("YAKA",101.5,20)
    print(sensor_yaka)
    sensor_yaka.update_reading(43.4)
    print(sensor_yaka)

    robot_Fanuc = Robot()




