from evdev import InputDevice, list_devices, ecodes
import robot

devices = [InputDevice(device) for device in list_devices()]
keyboard = devices[0]
print(keyboard)

keypress_actions = {
    ecodes.ABS_X: store_x,
    ecodes.ABS_Y: store_y
}

current_y = 0
current_x = 0

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
    robot.left (limit_value((current_y / 32768 * 100) + (current_x / 32768 * 100)))
    robot.right(limit_value((current_y / 32768 * 100) - (current_x / 32768 * 100)))

try:
    #with open("values.txt", "w") as log:
        for event in keyboard.read_loop():
            if event.code in keypress_actions:
                keypress_actions[event.code](event.value)
                update_motor_powers()
except KeyboardInterrupt:
    robot.stop()
