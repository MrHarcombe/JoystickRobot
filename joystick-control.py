from evdev import InputDevice, list_devices, ecodes
import robot

devices = [InputDevice(device) for device in list_devices()]
keyboard = devices[0]
print(keyboard)

keypress_actions = {
    ecodes.ABS_X: store_x,
    ecodes.ABS_Y: store_y
}

current_x = 0
current_y = 0

power_l = 0
power_r = 0

def store_x(value):
    current_x = value;
  
def store_y(value):
    current_y = value;

def limit_value(value):
    if value > 100:
        value = 100
    elif value < -100:
        value = -100
    return value

def update_motor_powers():
    power_l = limit_value((current_y / 32768 * 100) + (current_x / 32768 * 100))
    power_r = limit_value((current_y / 32768 * 100) - (current_x / 32768 * 100))
    robot.left (power_l)
    robot.right(power_r)

try:
    #with open("values.log", "w") as log:
        for event in keyboard.read_loop():
            if event.code in keypress_actions:
                #print(categorized, categorized.event.code, categorized.event.sec, categorized.event.timestamp, categorized.event.type, categorized.event.usec, categorized.event.value, file=log)
                keypress_actions[event.code](event.value)
                update_motor_powers()
                #print("x:", current_x, "y:", current_y, "power_l:", power_l, "power_r:", power_r, file=log)
except KeyboardInterrupt:
    robot.stop()
