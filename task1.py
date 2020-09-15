import numpy as np
import asyncio
import time



def Car (wheel_angle, speed):
    wheel_angle += np.random.uniform (-10, 10) * 0.5
    speed       += np.random.uniform (-10, 10)
    
    if (wheel_angle < 10):
        wheel_angle += np.absolute (wheel_angle - 10)
    if (wheel_angle > 170):
        wheel_angle -= np.absolute (wheel_angle - 170)
    if (speed < 0):
        speed += np.absolute (speed)
    if (speed > 120):
        speed -= np.absolute (speed - 120)
    
    return [wheel_angle, speed]


# problems with work of it
async def user_funcion ():
    await asyncio.sleep(3)
    command = input ("What to do? ")
    
    if command != 'stop':
        command = user_funcion()
    
    return command



if __name__ == '__main__':
    time_v   = 0
    angle    = 90.0
    velocity = 0.0
    our_car  = [angle, velocity]
    
    print ("Car stars working.")
    print ("If you want to stop write: stop")
    
    user_command = user_funcion()
    
    
    while True:
    
        if user_command == 'stop':
            print ("Car stopped.")
            break
        
        our_car = Car(our_car[0], our_car[1])
        print ("car agle: ", our_car[0], " car speed: ", our_car[1], "time: ", time_v)
        time_v += 1
        time.sleep(1)
    