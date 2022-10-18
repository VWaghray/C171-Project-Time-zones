from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("800x800")
root.title("Time Zones")


a_image = ImageTk.PhotoImage(Image.open ("australia map.jpg"))
j_image = ImageTk.PhotoImage(Image.open ("japan map.jpg"))
i_image = ImageTk.PhotoImage(Image.open ("india map.gif"))
c_image = ImageTk.PhotoImage(Image.open ("Canada Map.jpg"))

i_label = Label(root, text = "India", font = ("Snap ITC", 13, "bold"))
i_label.place(relx=.2, rely = .05, anchor = CENTER)

i_i = Label(root)
i_i["image"] = i_image
i_i.place(relx = .2, rely = .2, anchor = CENTER)

i_time = Label(root, font = ("Snap ITC", 15, "bold"))
i_time.place(relx = 0.2, rely=0.35, anchor = CENTER)

j_label = Label(root, text = "Japan", font = ("Snap ITC", 13, "bold"))
j_label.place(relx=.2, rely = .5, anchor = CENTER)

j_i = Label(root)
j_i["image"] = j_image
j_i.place(relx = .2, rely = .67, anchor = CENTER)

j_time = Label(root, font = ("Snap ITC", 13, "bold"))
j_time.place(relx = 0.2, rely=0.85, anchor = CENTER)

c_label = Label(root, text = "Canada", font = ("Snap ITC", 13, "bold"))
c_label.place(relx=.7, rely = .05, anchor = CENTER)

c_c = Label(root)
c_c["image"] = c_image
c_c.place(relx = .7, rely = .25, anchor = CENTER)

c_time = Label(root, font = ("Snap ITC", 13, "bold"))
c_time.place(relx = 0.7, rely=0.45, anchor = CENTER)

a_label = Label(root, text = "Australia", font = ("Snap ITC", 13, "bold"))
a_label.place(relx=.7, rely = .55, anchor = CENTER)

a_c = Label(root)
a_c["image"] = a_image
a_c.place(relx = .7, rely = .7, anchor = CENTER)

a_time = Label(root, font = ("Snap ITC", 13, "bold"))
a_time.place(relx = 0.7, rely=0.85, anchor = CENTER)

class India:
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        i_time["text"] = "Time: "+ current_time
        i_time.after(200,self.times)
        
class Japan:
    def times(self):
        home = pytz.timezone('Asia/Tokyo')
        local_time=datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        j_time["text"] = "Time: "+ current_time
        j_time.after(200,self.times)
        
class Canada:
    def times(self):
        home = pytz.timezone('America/Toronto')
        local_time=datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        c_time["text"] = "Time: "+ current_time
        c_time.after(200,self.times)
        
class Australia:
    def times(self):
        home = pytz.timezone('Australia/Sydney')
        local_time=datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        a_time["text"] = "Time: "+ current_time
        a_time.after(200,self.times)
        
obj_i = India()
obj_c = Canada()
obj_a = Australia()
obj_j = Japan()
btn1 = Button(root, text = "Show Time", command = obj_i.times, font = ("Snap ITC", 13, "bold"))
btn1.place(relx = .2, rely=.4, anchor = CENTER)

btn2 = Button(root, text = "Show Time", command = obj_c.times, font = ("Snap ITC", 13, "bold"))
btn2.place(relx = .7, rely=.5, anchor = CENTER)

btn3 = Button(root, text = "Show Time", command = obj_j.times, font = ("Snap ITC", 13, "bold"))
btn3.place(relx = .2, rely=.9, anchor = CENTER)

btn4 = Button(root, text = "Show Time", command = obj_a.times, font = ("Snap ITC", 13, "bold"))
btn4.place(relx = .7, rely=0.9, anchor = CENTER)

root.mainloop()

        
        




