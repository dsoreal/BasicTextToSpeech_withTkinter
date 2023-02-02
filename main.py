import tkinter as tk
import pyttsx3


def textToSpeech():
    window = tk.Tk()
    label = tk.Label(text='Text to Speech Generator', foreground='white', background='black', width=100)
    entry = tk.Text()

    def getTextThenTalk():
        whatToSay = entry.get('1.0', tk.END)
        entry.delete('1.0', tk.END)
        engine = pyttsx3.init()
        engine.setProperty('rate', 105)
        engine.say(whatToSay)
        engine.runAndWait()

    button = tk.Button(text='Submit Text for Speech', foreground='black', background='white', command=getTextThenTalk)

    label.pack()
    entry.pack()
    button.pack()
    window.mainloop()


if __name__ == '__main__':
    textToSpeech()
