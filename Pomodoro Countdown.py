#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        frame = tk.Frame(root, bd=5, relief="sunken")
        frame.pack()
        self.time_left = 25*60 # 25 minutes in seconds
        self.break_time = 5*60 # 5 minutes in seconds
        self.array_point=[]
        self.running = False
        self.break_running = False
        
        self.label01=tk.Label(master, font=("Tahoma",20,"bold"))
        self.label01.pack()
        self.label01.configure(text="COME ON!")
        
        self.point=tk.Label(master, text="YOUR POINT : 0", font=("Tahoma",20,"bold"))
        self.point.pack()
        
        # Create label to display time
        self.label = tk.Label(frame, text="25:00", font=("Helvetica", 36))
        self.label.pack()

        # Create start button
        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack(side="left", fill="both", expand=True)

        # Create stop button
        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", fill="both", expand=True)

        # Create reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", fill="both", expand=True)
        
        

    def start(self):
        if not self.running:
            self.running = True
            self.countdown()

    def stop(self):
        self.running = False
        self.break_running = False

    def reset(self):
        self.time_left = 25*60
        self.break_time = 5*60
        self.label.configure(text="25:00")
        self.label01.configure(text="GO AGAIN?")
        self.running = False
        self.break_running = False
        
    def perhitungan_point(self):
        point = len(self.array_point)*5
        self.point.configure(text="YOUR POINT : {:01d}".format(point))
    
    def countdown(self):
        if self.running:
            self.label01.configure(text="STUDY TIME!")
            # Update label with time left
            minutes, seconds = divmod(self.time_left, 60)
            self.label.configure(text="{:02d}:{:02d}".format(minutes, seconds))
            self.time_left -= 1

            # Start break if timer reaches 0
            if self.time_left == 0:
                self.array_point.append(1)
                self.perhitungan_point()
                self.break_running = True
                self.break_countdown()
            else:
                self.master.after(1000, self.countdown) # repeat every second

    def break_countdown(self):
        if self.break_running:
            self.label01.configure(text="BREAK TIME!")
            # Update label with break time left
            minutes, seconds = divmod(self.break_time, 60)
            self.label.configure(text="{:02d}:{:02d}".format(minutes, seconds))
            self.break_time -= 1

            # Reset timer if break reaches 0
            if self.break_time == 0:
                self.reset()
            else:
                self.master.after(1000, self.break_countdown) # repeat every second

# Create tkinter window and add PomodoroTimer widget
root = tk.Tk()
root.title("Pomodoro Timer")
timer = PomodoroTimer(root)
root.mainloop()


# In[ ]:




