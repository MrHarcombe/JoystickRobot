from evdev import InputDevice, list_devices, ecodes, categorize, AbsEvent
import robot

devices = [InputDevice(device) for device in list_devices()]
keyboard = devices[0]
print(keyboard)

keypress_actions = {
    ecodes.ABS_GAS: robot.right,
    ecodes.ABS_BRAKE: robot.left,
}

try:
  for event in keyboard.read_loop():
    if event.code in keypress_actions:
      keypress_actions[event.code](event.value)
except KeyboardInterrupt:
  robot.stop()
        
