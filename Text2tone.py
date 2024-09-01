import tkinter as tk
from tkinter import messagebox, filedialog
import pyttsx3

def speak_text():
    text = text_input.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text to speak.")
        return

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voice_var.get() == "Male":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def save_text():
    text = text_input.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)
        messagebox.showinfo("Success", "Text saved successfully!")

def exit_app():
    window.destroy()

# Main window
window = tk.Tk()
window.title("Jahnavi's Text2Tone")
window.geometry("650x450")
window.configure(bg="#F9F3DF")  


# Text input box
text_input = tk.Text(window, wrap=tk.WORD, height=10, font=("Comic Sans MS", 14), bg="#FFFCF9", fg="#4C4B63", bd=2, relief=tk.GROOVE)
text_input.pack(pady=20)

# Male/Female Voice Option
voice_var = tk.StringVar(value="Male")
male_radio = tk.Radiobutton(window, text="Male", variable=voice_var, value="Male", bg="#F9F3DF", font=("Comic Sans MS", 12, "bold"), fg="#2F2E41")
female_radio = tk.Radiobutton(window, text="Female", variable=voice_var, value="Female", bg="#F9F3DF", font=("Comic Sans MS", 12, "bold"), fg="#2F2E41")
male_radio.pack(side=tk.LEFT, padx=20)
female_radio.pack(side=tk.LEFT, padx=20)

# Button Frame
button_frame = tk.Frame(window, bg="#F9F3DF")
button_frame.pack(pady=20)

# Buttons
speak_button = tk.Button(button_frame, text="Speech", command=speak_text, font=("Comic Sans MS", 12, "bold"), bg="#FF6F61", fg="white", bd=0, width=12)
speak_button.grid(row=0, column=0, padx=10)

save_button = tk.Button(button_frame, text="Save", command=save_text, font=("Comic Sans MS", 12, "bold"), bg="#6B5B95", fg="white", bd=0, width=12)
save_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, font=("Comic Sans MS", 12, "bold"), bg="#88B04B", fg="white", bd=0, width=12)
exit_button.grid(row=0, column=2, padx=10)

window.mainloop()
