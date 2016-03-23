from evdev import InputDevice, list_devices, ecodes, categorize, AbsEvent
import time
import robot

devices = [InputDevice(device) for device in list_devices()]
keyboard = devices[0]
print(keyboard)

keypress_actions = {
    ecodes.ABS_X: robot.left,
    ecodes.ABS_Y: robot.right,
}

current_y = 0
current_x = 0

try:
    with open("values.txt", "w") as log:
        for event in keyboard.read_loop():
            if event.code in keypress_actions:
                categorized = categorize(event)
                if isinstance(categorized, AbsEvent) and \
                    (categorized.event.code == ecodes.ABS_X or categorized.event.code == ecodes.ABS_Y):
                    #print(categorized, categorized.event.code, categorized.event.sec, categorized.event.timestamp, categorized.event.type, categorized.event.usec, categorized.event.value, file=log)
                #if event.value != 0:
                    #print("Value:", event.value)
                    #keypress_actions[event.code](event.value / 32768 * 100)
                    if categorized.event.code == ecodes.ABS_Y:    
                        current_y = event.value 
                    elif categorized.event.code == ecodes.ABS_X:
                        current_x = event.value 

                    power_l = (current_y / 32768 * 100) + (current_x / 32768 * 100)
                    if power_l >100:
                        power_l = 100
                    elif power_l <-100:
                        power_l = -100
                    power_r = (current_y / 32768 * 100) - (current_x / 32768 * 100)
                    if power_r >100:
                        power_r = 100
                    elif power_r <-100:
                        power_r = -100

                    #print("x:", current_x, "y:", current_y, "power_l:", power_l, "power_r:", power_r, file=log)

                    robot.left(power_l)
                    robot.right(power_r)
except KeyboardInterrupt:
    robot.stop()
        
