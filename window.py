import tkinter as tk
import pyttsx3 as pytxt

# seting engie to TextToVoice
engine = pytxt.init();

#Function to playVoice
def playVoice():
    text = TextInput.get("1.0", tk.END);
    engine.say(text)
    engine.runAndWait()

# Function to clear TextInput
def clearText():
    TextInput.delete("1.0", tk.END);

# Create a window
window = tk.Tk();

# Setting Name and Size
window.title("Texto a voz");
window.geometry("720x370");

# Input
TextInput = tk.Text(window, width=80, height=15);
TextInput.pack(pady=10);

# Play Button
PlayButton = tk.Button(window, text="Reproducior", command=playVoice);
PlayButton.pack(pady=10);

# Clear Button
DeletePlay = tk.Button(window, text="Borrar", command=clearText);
DeletePlay.pack(pady=10);

# Window Show
window.mainloop();