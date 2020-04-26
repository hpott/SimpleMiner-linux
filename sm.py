from Tkinter import *
import os
import subprocess


cmd='sh start.sh '



master = Tk()

e = Entry(master)
e.pack()

v = StringVar(master, value='default text')

e.focus_set()
def taskend():
   subprocess.call("killall -1 xmrig", shell=True)

def callback():
   xmr=e.get()
   print xmr
   subprocess.call(cmd+xmr)
start = Button(master, text="Start mining", width=10, command=callback)
start.pack()

stop = Button(master, text="Pause Mining", width=10, command=taskend)
stop.pack()



mainloop()
e = Entry(master, textvariable=v,  width=50)
e.pack()

text = e.get()



text = content.get()
content.set(text)
