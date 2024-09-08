from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip

controller = Controller()


def fix_current_line():
    controller.pressed(Key.ctrl)
    controller.pressed(Key.shift)
    controller.pressed(Key.left)
    
    controller.release(Key.ctrl)
    controller.release(Key.shift)
    controller.release(Key.left)
    
    fix_selection()

def fix_text(text):
    fixed_test = text.lower()
    
    return fixed_test

def fix_selection():
    # *1. Copy to the clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')
        
    # *2. get the text from the clipboard
    text = pyperclip.paste()
    print(text)
    
    # *3. fixing the text
    fixed_text = fix_text(text)
    print(fixed_text)    
    
    # *4. copy back to the clipboard
    pyperclip.copy(fixed_text)
    print("Text recieved")
    
    # *5. inserting the text
    with controller.pressed(Key.ctrl):
        controller.tap('v')
        

def on_f9():
    fix_current_line()

def on_f10():
    fix_selection()

with keyboard.GlobalHotKeys({
        '<120>': on_f9,
        '<121>': on_f10}) as h:
    h.join()