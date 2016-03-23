from evdev import InputDevice, list_devices, ecodes, categorize, AbsEvent
import robot

devices = [InputDevice(device) for device in list_devices()]
keyboard = devices[0]
print(keyboard)

keypress_actions = {
    ecodes.KEY_W: robot.forward,
    ecodes.KEY_S: robot.reverse,
    ecodes.KEY_A: robot.left,
    ecodes.KEY_D: robot.right,
    ecodes.BTN_Y: robot.forward,
    ecodes.BTN_A: robot.reverse,
    ecodes.BTN_X: robot.left,
    ecodes.BTN_B: robot.right,
}

try:
  for event in keyboard.read_loop():
    if event.code in keypress_actions:
      keypress_actions[event.code]()
except KeyboardInterrupt:
    robot.stop()
