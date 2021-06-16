import tkinter as tk

import pyttsx3 

engine = pyttsx3.init()
class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title ("TTS")
        self.root.resizable(0,0)
        self.root.configure(background="blue")
        self.label = tk.Label(text = "what do you want me to say?",bg="blue",fg="black",font= "Arial 35")
        self.label.pack()
        self.entry = tk.Entry(font="Algerian 25",width=30)
        self.entry.pack()
        self.button =tk.Button(text="SPEAK",bg="red",fg="white",font="Arial 30 bold",command=self.clicked)
        self.button.pack()
        self.root.mainloop()
    
    def clicked(self):
        text = self.entry.get()
        self.speak(text)
    
    def speak(self,text):
        engine.say(text)
        engine.runAndWait()



if __name__ == "__main__":
    temp = Widget()



