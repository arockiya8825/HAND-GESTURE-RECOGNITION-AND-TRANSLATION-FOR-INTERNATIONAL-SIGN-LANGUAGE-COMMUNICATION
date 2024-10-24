import tkinter  as tk
from tkvideo import tkvideo
import pyttsx3
import numpy as np
import cv2
from PIL import Image
import speech_recognition as sr  
import pyttsx3 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

class ReverseApplication:
    engine.setProperty('rate',125)
    engine.setProperty('voice', voices[1].id);
    SpeechText = "";
    bgColor = "#333c4d"
    btnbgColor = "white"
    root = tk.Tk()

    def __init__(self):         
        self.root.title("Gesture Voice Bridge")
        frame = tk.Frame(self.root,bg=self.bgColor)
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.root.configure(bg=self.bgColor)

        app_name_label = tk.Label(frame, text="Voice To Gesture", font=("Helvetica", 24),bg=self.bgColor,fg="white")
        app_name_label.pack(padx=30,pady=10)
        my_label = tk.Label(frame,bg=self.bgColor)
        my_label.pack(padx=50,pady=40)
        self.player = tkvideo("output.mp4", my_label, loop = 0, size = (430,430))
        self.player.play()

        button_frame = tk.Frame(frame,bg=self.bgColor)
        button_frame.pack()

        repeat_button = tk.Button(button_frame, text="Talk", command=self.inputVoice, font=("Helvetica", 16),bg=self.btnbgColor, fg="black",bd=0, relief=tk.FLAT, borderwidth=0, highlightthickness=0, padx=10, pady=5)
        repeat_button.pack(side=tk.LEFT, padx=10)

        speak_button = tk.Button(button_frame, text="Play Again", command=self.repeatVideo, font=("Helvetica", 16),bg=self.btnbgColor, fg="black",bd=0, relief=tk.FLAT, borderwidth=0, highlightthickness=0, padx=10, pady=5)
        speak_button.pack(side=tk.LEFT)

        speak_button = tk.Button(button_frame, text="Voice Output", command=self.speakText, font=("Helvetica", 16),bg=self.btnbgColor, fg="black",bd=0, relief=tk.FLAT, borderwidth=0, highlightthickness=0, padx=10, pady=5)
        speak_button.pack(side=tk.LEFT,padx=10)

        self.text_label = tk.Label(frame, text="", width=30, font=("Helvetica", 18),bg=self.bgColor,fg="white")
        self.text_label.pack(pady=10)
        global engine;
        engine = pyttsx3.init()


    def generateVideo(self,text):
        text = text.lower().replace(" ","#")
        path = "alphabets"
        data = []
        for i in text:
            imgPath = path+"\\"+i+".jpg"
            data.append(imgPath)
        
        videodims = (400, 400)  # Set video dimensions to 400x400
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        FPS = 30
        video = cv2.VideoWriter('output.mp4', fourcc, FPS, videodims)

        frames_for_2_seconds = FPS * 2

        white_image = np.full((videodims[1], videodims[0], 3), 255, dtype=np.uint8)

        for _ in range(frames_for_2_seconds):
            video.write(white_image)

        for fidx, f in enumerate(data):
            print(f'Done: {round(fidx * 100 / len(data), 1)} % - {f}', end="\r")
            img = Image.open(f)
            img = img.resize((400, 400))  # Resize image to 400x400
            # Convert image to BGR format before writing to video
            img_array = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            # Write the same frame multiple times to achieve 2 seconds duration
            for _ in range(frames_for_2_seconds):
                video.write(img_array)
        video.release()


    def take_command(self):
        command = "Some Think Went Wrong"
        listener.pause_threshold = 3
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
        except :
            command = "Some Error Occured"

        self.SpeechText = command
        print("You Said : ",self.SpeechText)
        self.generateVideo(command)
        self.player.play()

    def repeatVideo(self):
        self.player.play()
        self.text_label.config(text="Repeating.....")

    def speakText(self):
        self.text_label.config(text="Speaking.....")
        engine.say(self.SpeechText)
        engine.runAndWait()

    def inputVoice(self):
        self.text_label.config(text="Listening.....")
        self.take_command()
        self.text_label.config(text="You Said : "+self.SpeechText)


(ReverseApplication()).root.mainloop()