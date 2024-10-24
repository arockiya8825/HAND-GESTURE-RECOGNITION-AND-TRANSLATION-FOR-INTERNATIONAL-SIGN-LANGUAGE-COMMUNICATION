import tkinter as tk

import final_pred as fp
import final_rev as fr

class Main:
    bgColor = "#333c4d"
    btnbgColor = "white"
    root = tk.Tk()

    def __init__(self):
        self.root.state('zoomed')
        self.root.title("Hand Gesture Voice Bridge")
        frame = tk.Frame(self.root, bg=self.bgColor)
        frame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)
        self.root.configure(bg=self.bgColor)

        app_name_label = tk.Label(frame, text="Hand Gesture Voice Bridge", font=("Helvetica", 24), bg=self.bgColor, fg="white")
        app_name_label.pack(padx=50, pady=30)

        button_frame = tk.Frame(frame, bg=self.bgColor) 
        button_frame.pack(pady=10)  

        gestureBtn = tk.Button(button_frame, text="Gesture to Voice", command=self.gesture, font=("Helvetica", 16), bg=self.btnbgColor, fg="black", bd=0, relief=tk.FLAT, borderwidth=0, highlightthickness=0, padx=10, pady=5,width=15, height=2)
        gestureBtn.pack(side=tk.LEFT, padx=10)

        reverseBtn = tk.Button(button_frame, text="Voice to Gesture", command=self.reverse, font=("Helvetica", 16), bg=self.btnbgColor, fg="black", bd=0, relief=tk.FLAT, borderwidth=0, highlightthickness=0, padx=10, pady=5,width=15, height=2)
        reverseBtn.pack(side=tk.RIGHT)

    def gesture(self):
        print("-- Gesture Screen --")
        fp.Application().root.mainloop()
    
    def reverse(self):
        print("-- Reverse Screen --")
        (fr.ReverseApplication()).root.mainloop()

Main().root.mainloop()